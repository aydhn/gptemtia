import re

file_path = "commodity_fx_signal_bot/data/storage/data_lake.py"
with open(file_path, "r") as f:
    content = f.read()

# Make sure imports are correct
if "LAKE_FEATURES_REGIME_DIR" not in content:
    content = content.replace(
        "from config.paths import (",
        "from config.paths import (\n    LAKE_FEATURES_REGIME_DIR,\n    LAKE_FEATURES_REGIME_EVENTS_DIR,"
    )

# Find the _get_feature_dir method
old_method_pattern = re.compile(r"    def _get_feature_dir\(self, feature_set_name: str\) -> Path:[\s\S]*?        return LAKE_FEATURES_TECHNICAL_DIR\n")
match = old_method_pattern.search(content)

if match:
    new_method = """    def _get_feature_dir(self, feature_set_name: str) -> Path:
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
            "regime": LAKE_FEATURES_REGIME_DIR,
            "regime_events": LAKE_FEATURES_REGIME_EVENTS_DIR,
        }

        if feature_set_name in mapping:
            return mapping[feature_set_name]

        # Fallback to technical if unknown
        return LAKE_FEATURES_TECHNICAL_DIR
"""
    content = content.replace(match.group(0), new_method)

with open(file_path, "w") as f:
    f.write(content)
