import re
with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

insert_str = """
        if feature_set_name == "strategy_candidates":
            base_dir = LAKE_FEATURES_STRATEGY_CANDIDATES_DIR
        elif feature_set_name == "strategy_pool":
            base_dir = LAKE_FEATURES_STRATEGY_POOL_DIR
        else:
            base_dir = LAKE_FEATURES_DIR / feature_set_name

        symbol_dir = (
            base_dir / source / sub_class / safe_sym
        )
"""

if "strategy_candidates" not in content.split("def get_feature_path(")[1].split("def save_features(")[0]:
    content = content.replace("        symbol_dir = (\n            LAKE_FEATURES_DIR / feature_set_name / source / sub_class / safe_sym\n        )", insert_str)
    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
        f.write(content)
