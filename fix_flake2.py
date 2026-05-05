import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

content = content.replace('            return (\n                from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR\n        LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR\n            ) / f"{code}.parquet"', '            from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR\n            return (\n                LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR\n            ) / f"{code}.parquet"')

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
