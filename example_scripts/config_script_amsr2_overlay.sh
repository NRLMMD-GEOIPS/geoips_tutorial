run_procflow ${GEOIPS_TESTDATA_DIR}/test_data_amsr2/data/*mbt*.nc \
  --procflow config_based \
  --output_config ${GEOIPS_PACKAGES_DIR}/geoips_tutorial/example_scripts/output_config_amsr2_overlay.yaml \
  --fuse_files ${GEOIPS_TESTDATA_DIR}/test_data_amsr2/bg_data/ahi_20200518_0740/* \
  --fuse_reader ahi_hsd \
  --fuse_product Visible \
  --fuse_resampled_read True