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

#!/bin/bash

# This script will copy over some of the components from the geoips_template_plugin 
# repository to $GEOIPS_PACKAGES_DIR/plugin_tutorial

set -e

plugin_name=${1:-tutorial_plugin}

check_continue() {
    unset CONTINUE
    while [ -z "$CONTINUE" ]; do
        echo "Y or y to continue "
        echo "Q or q to quit plugin tutorial setup altogether?"
        read -r -p "[y/q]: " CONTINUE
    done
    if [[ $CONTINUE == "q" || $CONTINUE == "Q" ]]; then
        echo "Quitting"
        exit 1 
    elif [[ $CONTINUE == "y" || $CONTINUE == "Y" ]]; then
        echo "Continuing!"
        skip_next="no"
    else
        echo "*********************************"
        echo "Please enter one of [y/q]"
        echo "*********************************"
        check_continue
    fi
}

GEOIPS_TUTORIAL=$GEOIPS_PACKAGES_DIR/geoips_tutorial
PLUGIN_TUTORIAL=$GEOIPS_PACKAGES_DIR/$plugin_name

if [[ -d $PLUGIN_TUTORIAL ]]; then
    echo "WARNING: plugin directory already exists"
    echo $PLUGIN_TUTORIAL
    echo "This script may overwrite files. How would you like to proceed?"
    check_continue
fi

# Make the plugin_tutorial directory
PLUGIN_DIR=$PLUGIN_TUTORIAL/$plugin_name
echo "Creating plugin tutorial directory: $PLUGIN_TUTORIAL"
mkdir -pv $PLUGIN_DIR
touch $PLUGIN_DIR/__init__.py

echo ""

echo "Creating base interface module directories"
interface_module_dirs=(
    filename_formats
    interpolation
    output_formats
    procflows
    readers
    title_formats
    trackfile_parsers
    user_colormaps
)

for module_dir in ${interface_module_dirs[@]}; do
    mdir=$PLUGIN_DIR/interface_modules/$module_dir
    mkdir -p $mdir
    echo $mdir
    touch $mdir/__init__.py
done

echo ""

echo "Creating YAML config directories"
yaml_config_dirs=(
    plotting_params/boundaries
    plotting_params/gridlines
    product_inputs
    product_params
)
for yaml_dir in ${yaml_config_dirs[@]}; do
    ydir=$PLUGIN_DIR/yaml_configs/$yaml_dir
    mkdir -p $PLUGIN_DIR/yaml_configs/$yaml_dir
    echo $ydir
done

echo ""

echo "Copying geoips_tutorial example interface modules"
tutorial_module_dirs=(
    filename_formats
    readers
)
for interface_dir in ${tutorial_module_dirs[@]}; do
    cp -v $GEOIPS_TUTORIAL/geoips_tutorial/interface_modules/$interface_dir/* $PLUGIN_DIR/interface_modules/$interface_dir/
done

echo ""

echo "Copy version file from geoips_tutorial"
cp -v $GEOIPS_TUTORIAL/VERSION $PLUGIN_TUTORIAL/VERSION

echo ""

echo "Copy over tutorial setup.py from geoips_tutorial"
cp -v $GEOIPS_TUTORIAL/plugin/tutorial_setup.py $PLUGIN_TUTORIAL/setup.py
