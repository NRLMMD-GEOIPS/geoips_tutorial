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
