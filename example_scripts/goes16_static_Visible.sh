run_procflow $GEOIPS/tests/data/goes16_20200918_1950/* \
    --procflow single_source \
    --reader_name abi_netcdf \
    --product_name Visible \
    --output_format imagery_annotated \
    --filename_format geoips_fname \
    --resampled_read \
    --sector_list goes16 \
    --sectorfiles $GEOIPS/tests/sectors/static/goes16.yaml
