import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

new_constants = """
LAKE_FEATURES_TREND_DIR = LAKE_FEATURES_DIR / "trend"
LAKE_FEATURES_TREND_EVENTS_DIR = LAKE_FEATURES_DIR / "trend_events"
TREND_REPORTS_DIR = REPORTS_DIR / "trend_reports"
"""

if "LAKE_FEATURES_TREND_DIR" not in content:
    content = content.replace(
        "MOMENTUM_REPORTS_DIR = REPORTS_DIR / \"momentum_reports\"",
        "MOMENTUM_REPORTS_DIR = REPORTS_DIR / \"momentum_reports\"\n" + new_constants
    )

    directories_to_add = """        LAKE_FEATURES_TREND_DIR,
        LAKE_FEATURES_TREND_EVENTS_DIR,
        TREND_REPORTS_DIR,
"""
    content = content.replace(
        "MOMENTUM_REPORTS_DIR,",
        "MOMENTUM_REPORTS_DIR,\n" + directories_to_add
    )
    with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
        f.write(content)
