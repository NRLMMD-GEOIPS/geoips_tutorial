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

NRLMMD-GEOIPS/geoips#25 - remove Visible from tests

### Improvements
* Use Infrared-Gray for AMSR2 overlay vs Visible
* Use Infrared for goes-16 static product


# NRLMMD-GEOIPS/geoips_tutorial#5-clean-up-and-apply-bug-fixes-for-jupyter-notebooks

### Bug Fixes
* **notebooks/interfaces.ipynb**
    * Fixed bugs under get_filenamer_type and procflow example codeblocks
### Improvements
* **notebooks**
    * Remove deprecated interface functions
    * Updated formatting in markdown blocks
    * Update examples under interfaces notebook to center around ABI Infrared-Gray product
* **notebook_funcs**
    * Add by_type kwarg to print_signatures() that prints the function signature for each unique module type when true
* **setup_tutorial_plugin**
    * Removed reliance on rsync, which may not be available across all systems
    * Removed reliance on geoips_template_plugin, and manually sets up interface module directories
    * Add partially populated tutorial_setup.py, which gets copied to the tutorial_plugin directory
### Major new functionality
* **launch.json template**
    *Added a launch.json file intended to be copied over to a .vscode directory. It contains an AMSR 2 test case

# NRLMMD-GEOIPS/geoips_tutorial#6

### Improvements
* **example_scripts** Added examples for Command Line Processing tutorial
    * GOES-16 Static Visible annotated imagery example
    * AMSR2 windspeed single source clean imagery example
    * AMSR2 windspeed config-based clean imagery example
    * AMSR2 overlays config-based imagery example

# 1-tutorial-notebook-bug-fixes-and-readme-updates

### Bug Fixes
* **notebooks/utils/set\_env.ipy**
    * Force os.system to open a bash subshell, otherwise might open sh subshell
    * Check if GEOIPS_PACKAGES_DIR is set rather than GEOIPS_OUTDIRS, since GEOIPS_OUTDIRS is set manually
    * Use abspath of GEOIPS_OUTDIRS
### Documentation Updates
* **README.md**
    * GEOIPS_CONFIG_FILE now points to geoips/setup/config_geoips
    * Replace instructions to checkout branch dev with main

NRLMMD-GEOIPS/geoips_tutorial#3 add git lfs install to README.md

### Installation and Test
* **README.md**
    * Add "git lfs install" to README to ensure Git Large File Storage is enabled to prevent corrupt clones
        on git lfs tracked data files.


# v1.5.1: 2022-07-13, canned interface modules, tutorial plugin script

### Major New Functionality
* **Canned interface modules**
    * Add interface modules that are ready to add to geoips
* **Create tutorial plugin**
    * Copy over select files from geoips\_template\_plugin to new directory for tutorial
* **setup scripts**
    * Add setup.py that holds python dependencies for running Jupyter notebooks
* **notebooks**
    * Add notebook that steps through module interfaces
    * Add notebook that steps through single_source procflow

### Documentation Updates
* **README.md**
    * Add README documenting install process for geoips\_tutorial plugin
* Update \*.md Distro statement headers to use 4 spaces prefix rather than ### (formatting improvement)
