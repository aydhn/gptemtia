import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

content = content.replace('LAKE_MACRO_PROCESSED_DIR if processed', 'from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR\n        LAKE_MACRO_PROCESSED_DIR if processed', 1)
content = content.replace('target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR', 'from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR\n        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR')

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/indicators/feature_builder.py", "r") as f:
    content = f.read()
content = content.replace('builder = PriceActionFeatureSetBuilder()', 'from indicators.price_action_feature_set import PriceActionFeatureSetBuilder\n        builder = PriceActionFeatureSetBuilder()')
with open("commodity_fx_signal_bot/indicators/feature_builder.py", "w") as f:
    f.write(content)
