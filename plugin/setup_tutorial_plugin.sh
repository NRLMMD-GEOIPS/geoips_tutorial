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

plugin_name=${1:-plugin_tutorial}

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

template_plugin=$GEOIPS_PACKAGES_DIR/geoips_template_plugin
plugin_tutorial=$GEOIPS_PACKAGES_DIR/$plugin_name

if [[ ! -d $template_plugin ]]; then
    echo "GeoIPS template plugin not cloned, running $GEOIPS/setup/repo_clone_update_install.sh"
    internal_plugins="geoips_template_plugin"
    $GEOIPS/setup/repo_clone_update_install.sh repo_clone
fi

if [[ -d $plugin_tutorial ]]; then
    echo "WARNING: plugin tutorial directory already exists"
    echo "This script may overwrite files. How would you like to proceed?"
    check_continue
fi

# Make the plugin_tutorial directory
echo "Creating plugin tutorial directory: $plugin_tutorial"
mkdir -p $plugin_tutorial/$plugin_name

echo "Copying template setup scripts"
cp -r $template_plugin/setup* $plugin_tutorial/
cp $template_plugin/VERSION $plugin_tutorial/

echo "Copying template interface modules"
rsync -a $template_plugin/geoips_template_plugin/interface_modules/ $plugin_tutorial/$plugin_name/ --exclude "*pycache*"

echo "Copying template YAML configs"
cp -r $template_plugin/geoips_template_plugin/yaml_configs $plugin_tutorial/$plugin_name/

echo "Copying over tests"
mkdir $plugin_tutorial/tests
cp $template_plugin/tests/test_all.sh $plugin_tutorial/tests/
cp -r $template_plugin/tests/scripts $plugin_tutorial/tests/

