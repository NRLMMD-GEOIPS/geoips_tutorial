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

'''Example setup for a new plugin package'''

from os.path import realpath, join, dirname

import setuptools

with open(join(dirname(realpath(__file__)), 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name='plugin_example',
    version=version,
    packages=setuptools.find_packages(),
    install_requires=[
                      # Add pip installable python dependencies here if needed.
                      'xarray',
                      'netcdf4',
                      'rasterio',
                      ],
    entry_points={
        'geoips.readers': [
            # Add new interface module functions here. For example (note, anything in <> should be updated appropriately):
            # '<reader func name>=<plugin name>.interface_modules.readers.<reader file/module name>:<reader func name>',
        ],
        'geoips.algorithms': [
            # Algorithm module interfaces
            # '<algorithm func name>=<plugin name>.interface_modules.algorithms.<algorithm file/module name>:<algorithm func name>',
            'my_color89_alg=my_plugin.interface_modules.algorithms.my_color89_alg:my_color89_alg',
        ],
        'geoips.output_formats': [
            # Add output format interface modules here
            'my_geotiff_output=my_plugin.interface_modules.output_formats.my_geotiff_output:my_geotiff_output',
        ],
        'geoips.user_colormaps': [
            # Add colormap interface modules here
            'my_89pct_cmap=my_plugin.interface_modules.user_colormaps.my_89pct_cmap:my_89pct_cmap',
        ],
        'geoips.filename_formats': [
            # Add filename interface modules here
            'my_fname_format=my_plugin.interface_modules.filename_formats.my_fname_format:my_fname_format',
        ],
      }
)
