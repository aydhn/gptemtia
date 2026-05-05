import re
with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

import_paths = """            LAKE_FEATURES_MTF_DIR,
            LAKE_FEATURES_MTF_EVENTS_DIR,
            LAKE_FEATURES_STRATEGY_CANDIDATES_DIR,
            LAKE_FEATURES_STRATEGY_POOL_DIR,
"""

if "LAKE_FEATURES_STRATEGY_CANDIDATES_DIR" not in content:
    content = content.replace("            LAKE_FEATURES_MTF_DIR,\n            LAKE_FEATURES_MTF_EVENTS_DIR,", import_paths)

mapping_code = """
        if feature_set_name == "strategy_candidates":
            base_dir = LAKE_FEATURES_STRATEGY_CANDIDATES_DIR
        elif feature_set_name == "strategy_pool":
            base_dir = LAKE_FEATURES_STRATEGY_POOL_DIR
        elif feature_set_name == "decision_candidates":
"""

if "feature_set_name == \"strategy_candidates\"" not in content:
    content = content.replace("elif feature_set_name == \"decision_candidates\":", mapping_code.strip())
    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
        f.write(content)
