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

#!/bin/sh

if [ -e ../plugin_example ]; then
    mv ../plugin_example ../my_plugin
fi

mkdir -p ../my_plugin/yaml_configs/product_params
mkdir -p ../my_plugin/yaml_configs/product_inputs
mkdir -p ../my_plugin/interface_modules/algorithms

cp my_89pct.yaml ../my_plugin/yaml_configs/product_params/
cp amsr2.yaml ../my_plugin/yaml_configs/product_inputs
cp my_89pct_alg.py ../my_plugin/interface_modules/algorithms
cp setup.py ../
