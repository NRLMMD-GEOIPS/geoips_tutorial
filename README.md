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

Installation Guide
==================

This installation guide has installation steps specific to installing the geoips_tutorial plugin, including
the base geoips conda install if not already installed.

Setup System Environment Variables
----------------------------------

```bash

    # Set up appropriate environment variables for all conda-based geoips_tutorial setup steps
    # within this geoips_tutorial README below

    # These steps will need to be copied and pasted into your shell any time you want to run the 
    # setup commands within this README.
    
    # Typical users do not have to make any modifications to the commands
    # within this README, and can copy and paste directly.

    # Once geoips_tutorial has been installed, the "GEOIPS_CONFIG_FILE" specified below will be
    # sourced when running geoips_tutorial, and the direct environment variable assignments
    # within this section are no longer required.

    # If you would like to have the GEOIPS_CONFIG_FILE automatically sourced so you do not have to manually run the 
    # source command for every new shell, you can add 
    # source </full/path/to/config/file>
    # to your ~/.bashrc file

    git lfs install  # Required to clone Git Large File Storage tracked data files

    # GEOIPS_REPO_URL should point to the base URL for git clone commands
    export GEOIPS_REPO_URL=https://github.com/NRLMMD-GeoIPS

    # GEOIPS_BASEDIR will contain all source, output, and external dependencies
    # Ensure this is consistently set for all installation / setup steps below
    export GEOIPS_BASEDIR=$HOME/geoproc

    # This config file must be sourced ANY TIME you want to run the geoips geoips_tutorial plugin
    export GEOIPS_CONFIG_FILE=$GEOIPS_BASEDIR/geoips_packages/geoips/setup/config_plugin

```

Clone geoips_tutorial git repositories required for setup scripts
-----------------------------------------------------------
```bash
    mkdir -p $GEOIPS_BASEDIR/geoips_packages/

    git clone $GEOIPS_REPO_URL/geoips.git $GEOIPS_BASEDIR/geoips_packages/geoips
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips pull
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips checkout -t origin/main
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips checkout main
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips pull

    git clone $GEOIPS_REPO_URL/geoips_tutorial.git ${GEOIPS_BASEDIR}/geoips_packages/geoips_tutorial
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_tutorial pull
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_tutorial checkout -t origin/main
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_tutorial checkout main
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_tutorial pull
```

IF REQUIRED: Install and test base geoips conda environment
------------------------------------------------------------
```bash
    # SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS CONDA ENVIRONMENT 
    # This prompts you through all the steps of installing the geoips conda environment from scratch,
    # using the parameters specified above.  This only needs to be done once per system, skip if you
    # already ran this command and successfully installed the geoips conda environment.
    $GEOIPS_BASEDIR/geoips_packages/geoips/base_install_and_test.sh main
```

Install geoips_tutorial package
-------------------------
```bash

    source $GEOIPS_CONFIG_FILE
    pip install -e $GEOIPS_BASEDIR/geoips_packages/geoips_tutorial
```
