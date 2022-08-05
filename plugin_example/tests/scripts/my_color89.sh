#!/bin/bash

run_procflow $GEOIPS_BASEDIR/test_data/test_data_amsr2/data/20200518.062048.gcom-w1.amsr2.amsr2_nesdismanatigcom.x.x.mbt.x.e202005180759470_c202005180937100.nc \
          --procflow single_source \
          --reader_name my_amsr2_reader \
          --product_name my_color89 \
          --filename_format my_fname_format \
          --output_format imagery_annotated \
          --trackfile_parser bdeck_parser \
          --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bio012020.dat
ss_retval=$?

exit $((ss_retval))

