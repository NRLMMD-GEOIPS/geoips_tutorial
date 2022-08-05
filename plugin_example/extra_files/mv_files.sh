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
