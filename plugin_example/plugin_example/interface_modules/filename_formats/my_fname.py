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

'''Standard geoips filename production'''

# Python Standard Libraries
import logging

from os.path import join as pathjoin

from geoips.filenames.base_paths import PATHS as gpaths

LOG = logging.getLogger(__name__)

filename_type = 'standard'


def my_fname(area_def, xarray_obj, product_name, coverage, output_type='png', output_type_dir=None,
             product_dir=None, product_subdir=None, source_dir=None, basedir=gpaths['ANNOTATED_IMAGERY_PATH']):

    fname = os.path.join(basedir, '_'.join(xarray_obj.strftime('%Y%m%d.%H%M%S'),
                                           area_def.name,
                                           product_name,
                                           )
    return fname+'.'+output_type
