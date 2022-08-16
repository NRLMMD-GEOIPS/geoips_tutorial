run_procflow \
  $GEOIPS_BASEDIR/test_data/test_data_amsr2/data/AMSR2-OCEAN*.nc \
  --procflow single_source \
  --reader_name amsr2_netcdf \
  --product_name windspeed \
  --filename_format tc_fname \
  --output_format imagery_clean \
  --trackfile_parser bdeck_parser \
  --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bio012020.dat