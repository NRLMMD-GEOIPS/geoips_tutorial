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
    name='tutorial_plugin',
    version=version,
    packages=setuptools.find_packages(),
    install_requires=[
                      # Add pip installable python dependencies here if needed. For example:
                      # 'numpy',
                      # 'ipykernel',
                      ],
    entry_points={
        'geoips.readers': [
            # Add new interface module functions here. For example (note, anything in <> should be updated appropriately):
            # '<module func name>=<plugin name>.interface_modules.readers.<module file name>:<module func name>',
        ],
        'geoips.algorithms': [
            # Algorithm module interfaces
        ],
        'geoips.output_formats': [
            # Add output format interface modules here
        ],
        'geoips.procflows': [
            # Add procflow interface modules here
        ],
        'geoips.interpolation': [
            # Add interpolation interface modules here
        ],
        'geoips.user_colormaps': [
            # Add colormap interface modules here
        ],
        'geoips.filename_formats': [
            # Add filename interface modules here
        ],
        'geoips.title_formats': [
            # Add title interface modules here
        ],
      }
)
