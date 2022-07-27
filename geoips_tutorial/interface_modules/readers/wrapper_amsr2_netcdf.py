# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # # 
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # # 
# # # This program is free software:
# # # you can redistribute it and/or modify it under the terms
# # # of the NRLMMD License included with this program.
# # # 
# # # If you did not receive the license, see
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/
# # # for more information.
# # # 
# # # This program is distributed WITHOUT ANY WARRANTY;
# # # without even the implied warranty of MERCHANTABILITY
# # # or FITNESS FOR A PARTICULAR PURPOSE.
# # # See the included license for more details.

'''Wrapper for AMSR2 data products reader'''
import logging
from os.path import basename
LOG = logging.getLogger(__name__)


reader_type = 'standard'


def wrapper_amsr2_netcdf(fnames, metadata_only=False, chans=None, area_def=None, self_register=False):
    ''' This is a wrapper around the AMSR2 netcdf data products reader. 
    This is part of the tutorial that adds a new reader interface module

    All GeoIPS 2.0 readers read data into xarray Datasets - a separate
    dataset for each shape/resolution of data - and contain standard metadata information.

    Args:
        fnames (list): List of strings, full paths to files
        metadata_only (Optional[bool]):
            * DEFAULT False
            * return before actually reading data if True
        chans (Optional[list of str]):
            * DEFAULT None (include all channels)
            * List of desired channels (skip unneeded variables as needed)
        area_def (Optional[pyresample.AreaDefinition]):
            * NOT YET IMPLEMENTED
                * DEFAULT None (read all data)
                * Specify region to read
        self_register (Optional[str]):
            * NOT YET IMPLEMENTED
                * DEFAULT False (read multiple resolutions of data)
                * register all data to the specified resolution.

    Returns:
        dict of xarray.Datasets: dict of xarray.Dataset objects with required
            Variables and Attributes: (See geoips/docs :doc:`xarray_standards`),
            dict key can be any descriptive dataset id
   '''
    from geoips.stable.reader import get_reader
    amsr2_netcdf_reader = get_reader('amsr2_netcdf')
    xarrays = amsr2_netcdf_reader(fnames, metadata_only=metadata_only, chans=chans, 
                                  area_def=area_def, self_register=self_register)
    return xarrays
