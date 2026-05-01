import re

file_path = "commodity_fx_signal_bot/config/paths.py"
with open(file_path, "r") as f:
    content = f.read()

paths_to_add = """
LAKE_FEATURES_REGIME_DIR = LAKE_FEATURES_DIR / "regime"
LAKE_FEATURES_REGIME_EVENTS_DIR = LAKE_FEATURES_DIR / "regime_events"
REGIME_REPORTS_DIR = REPORTS_DIR / "regime_reports"
"""

if "LAKE_FEATURES_REGIME_DIR" not in content:
    content = content.replace("LAKE_TMP_DIR = LAKE_DIR / \"tmp\"", paths_to_add + "\nLAKE_TMP_DIR = LAKE_DIR / \"tmp\"")

dirs_to_add = """        LAKE_FEATURES_REGIME_DIR,
        LAKE_FEATURES_REGIME_EVENTS_DIR,
        REGIME_REPORTS_DIR,
"""

if "LAKE_FEATURES_REGIME_DIR," not in content:
    content = content.replace("        LAKE_TMP_DIR,", dirs_to_add + "        LAKE_TMP_DIR,")

with open(file_path, "w") as f:
    f.write(content)
