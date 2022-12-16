# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

'''Standard TC filename production'''

# Python Standard Libraries
import logging

from os.path import join as pathjoin, splitext as pathsplitext
from os.path import dirname as pathdirname, basename as pathbasename, exists as pathexists
from datetime import datetime, timedelta
from glob import glob
from os import unlink as osunlink

from geoips.filenames.base_paths import PATHS as gpaths
from geoips.data_manipulations.merge import minrange

LOG = logging.getLogger(__name__)

filename_type = 'standard'


def tutorial_tc_fname(area_def, xarray_obj, product_name, coverage, output_type='png', output_type_dir=None,
             product_dir=None, product_subdir=None, source_dir=None, basedir=gpaths['TCWWW'],
             extra_field=None, output_dict=None):
    from geoips.interface_modules.filename_formats.tc_fname import tc_fname_remove_duplicates, assemble_tc_fname

    from geoips.sector_utils.utils import is_sector_type
    if area_def and not is_sector_type(area_def, 'tc'):
        LOG.warning('NOT a TC sector, skipping TC output')
        return None

    if not product_dir:
        product_dir = product_name

    if not output_type_dir:
        output_type_dir = output_type

    # This allows you to explicitly set matplotlib parameters (colorbars, titles, etc).  Overrides were placed in
    # geoimgbase.py to allow using explicitly set values rather than geoimgbase determined defaults.
    # Return reused parameters (min/max vals for normalization, colormaps, matplotlib Normalization)
    from geoips.filenames.base_paths import PATHS as gpaths
    from geoips.xarray_utils.timestamp import get_min_from_xarray_timestamp

    # start_dt = get_min_from_xarray_timestamp(xarray_obj, 'timestamp')
    start_dt = xarray_obj.start_datetime

    if area_def.sector_info['vmax']:
        intensity = '{0:0.0f}kts'.format(area_def.sector_info['vmax'])
    else:
        # This is pulling intensity directly from the deck file, and sometimes it is not defined - if empty, just 
        # use "unknown" for intensity
        intensity = 'unknown'

    from geoips.interface_modules.filename_formats.utils.tc_file_naming import update_extra_field
    extra = update_extra_field(output_dict,
                               xarray_obj,
                               area_def,
                               product_name,
                               extra_field_delimiter='-',
                               existing_extra_field=extra_field,
                               extra_field_resolution=True,
                               extra_field_coverage_func=True,
                               extra_field_provider=True,
                               include_filename_extra_fields=True)

    web_fname = assemble_tc_fname(basedir=basedir,
                                  tc_year=int(area_def.sector_info['storm_year']),
                                  tc_basin=area_def.sector_info['storm_basin'],
                                  tc_stormnum=int(area_def.sector_info['storm_num']),
                                  output_type=output_type,
                                  product_name=product_name,
                                  product_dir=product_dir,
                                  product_subdir=product_subdir,
                                  source_name=xarray_obj.source_name,
                                  platform_name=xarray_obj.platform_name,
                                  coverage=coverage,
                                  product_datetime=start_dt,
                                  intensity=intensity,
                                  extra=extra+'-tutorial',
                                  output_type_dir=output_type_dir)
    return web_fname


