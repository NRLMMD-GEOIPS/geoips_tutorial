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

'''Setup for geoips tutorial package'''

from os.path import realpath, join, dirname

import setuptools

with open(join(dirname(realpath(__file__)), 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name='geoips_tutorial',
    version=version,
    packages=setuptools.find_packages(),
    install_requires=['ipykernel',
                      'notebook',
                      'jupyter',
                      'python-dotenv',
                      ],
    entry_points={
        
      }
)
