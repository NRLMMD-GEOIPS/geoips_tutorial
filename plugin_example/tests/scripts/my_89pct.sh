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

#!/bin/bash

run_procflow $GEOIPS_BASEDIR/test_data/test_data_amsr2/data/20200518.062048.gcom-w1.amsr2.amsr2_nesdismanatigcom.x.x.mbt.x.e202005180759470_c202005180937100.nc \
          --procflow single_source \
          --reader_name my_amsr2_reader \
          --product_name my_89pct \
          --filename_format my_geotiff_fname \
          --output_format my_geotiff_output \
          --trackfile_parser bdeck_parser \
          --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bio012020.dat
ss_retval=$?

exit $((ss_retval))

