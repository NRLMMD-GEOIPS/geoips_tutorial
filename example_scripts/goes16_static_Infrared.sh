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

run_procflow $GEOIPS/tests/data/goes16_20200918_1950/* \
    --procflow single_source \
    --reader_name abi_netcdf \
    --product_name Infrared \
    --output_format imagery_annotated \
    --filename_format geoips_fname \
    --resampled_read \
    --sector_list goes16 \
    --sectorfiles $GEOIPS/tests/sectors/static/goes16.yaml
