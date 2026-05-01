import re

file_path = "commodity_fx_signal_bot/data/storage/data_lake.py"
with open(file_path, "r") as f:
    content = f.read()

# Add the new directories to DataLake.__init__ if not exists
if "LAKE_FEATURES_MTF_DIR" not in content:
    content = content.replace(
        "from config.paths import (",
        "from config.paths import (\n    LAKE_FEATURES_MTF_DIR,\n    LAKE_FEATURES_MTF_EVENTS_DIR,"
    )

    # Update _get_feature_dir function
    new_get_feature_dir = """
    def _get_feature_dir(self, feature_set_name: str) -> Path:
        \"\"\"Get the appropriate directory for a feature set.\"\"\"
        mapping = {
            "technical": LAKE_FEATURES_TECHNICAL_DIR,
            "momentum": LAKE_FEATURES_MOMENTUM_DIR,
            "momentum_events": LAKE_FEATURES_MOMENTUM_EVENTS_DIR,
            "trend": LAKE_FEATURES_TREND_DIR,
            "trend_events": LAKE_FEATURES_TREND_EVENTS_DIR,
            "volatility": LAKE_FEATURES_VOLATILITY_DIR,
            "volatility_events": LAKE_FEATURES_VOLATILITY_EVENTS_DIR,
            "price_action": LAKE_FEATURES_PRICE_ACTION_DIR,
            "price_action_events": LAKE_FEATURES_PRICE_ACTION_EVENTS_DIR,
            "divergence": LAKE_FEATURES_DIVERGENCE_DIR,
            "divergence_events": LAKE_FEATURES_DIVERGENCE_EVENTS_DIR,
            "mtf": LAKE_FEATURES_MTF_DIR,
            "mtf_events": LAKE_FEATURES_MTF_EVENTS_DIR,
        }

        if feature_set_name in mapping:
            return mapping[feature_set_name]

        # Fallback to technical if unknown (though we should probably raise an error)
        return LAKE_FEATURES_TECHNICAL_DIR
"""

    # We'll replace the existing _get_feature_dir method
    # It might be tricky with regex, so we'll just do a simpler string replacement

    # Find _get_feature_dir implementation
    start_idx = content.find("def _get_feature_dir")
    if start_idx != -1:
        # Find the next def
        end_idx = content.find("def ", start_idx + 4)
        if end_idx == -1:
            end_idx = len(content)

        old_method = content[start_idx:end_idx]
        content = content.replace(old_method, new_get_feature_dir + "\n    ")

with open(file_path, "w") as f:
    f.write(content)
