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

GeoIPS Tutorial Repository
==========================

The GeoIPS Tutorial repository contains Jupyter notebooks with
interactive tutorials to aid in understanding the GeoIPS processing
infrastructure and workflow.

Please see the 
[GeoIPS Documentation](https://github.com/NRLMMD-GEOIPS/geoips/blob/main/README.md)
for more information on the GeoIPS base infrastructure and plugin architecture.

Package Overview
-----------------

Jupyter notebooks are contained within the 
[notebooks](https://github.com/NRLMMD-GEOIPS/geoips_tutorial/notebooks)

System Requirements
---------------------

* geoips >= 1.5.3
* Test data repos contained in $GEOIPS_TESTDATA_DIR for tests to pass.

IF REQUIRED: Install base geoips package
------------------------------------------------------------
SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS ENVIRONMENT 

If GeoIPS Base is not yet installed, follow the
[installation instructions](https://github.com/NRLMMD-GEOIPS/geoips/blob/main/docs/installation.rst)
within the geoips source repo documentation:

Install geoips_template_plugin package
----------------------------------------
```bash
    # Assuming you followed the fully supported installation,
    # using $GEOIPS_PACKAGES_DIR and $GEOIPS_CONFIG_FILE:
    source $GEOIPS_CONFIG_FILE
    git clone -b $GEOIPS_ACTIVE_BRANCH $GEOIPS_REPO_URL $GEOIPS_PACKAGES_DIR/geoips_tutorial
    pip install -e $GEOIPS_PACKAGES_DIR/geoips_tutorial
```

Test geoips_tutorial installation
-----------------------------------------
```bash
    # Assuming you followed the fully supported installation,
    # using $GEOIPS_PACKAGES_DIR and $GEOIPS_CONFIG_FILE:
    source $GEOIPS_CONFIG_FILE
    $GEOIPS_PACKAGES_DIR/geoips_tutorial/tests/test_all.sh
```
