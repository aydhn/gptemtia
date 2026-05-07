import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

paths_str = """
LAKE_FEATURES_LEVEL_CANDIDATES_DIR = LAKE_FEATURES_DIR / "level_candidates"
LAKE_FEATURES_LEVEL_POOL_DIR = LAKE_FEATURES_DIR / "level_pool"

REPORTS_LEVEL_REPORTS_DIR = REPORTS_DIR / "level_reports"
"""

content = content.replace("LAKE_FEATURES_SIZING_POOL_DIR = LAKE_FEATURES_DIR / \"sizing_pool\"", "LAKE_FEATURES_SIZING_POOL_DIR = LAKE_FEATURES_DIR / \"sizing_pool\"" + paths_str)

dir_str = """    LAKE_FEATURES_LEVEL_CANDIDATES_DIR,
    LAKE_FEATURES_LEVEL_POOL_DIR,
    REPORTS_LEVEL_REPORTS_DIR,"""

content = content.replace("    LAKE_FEATURES_SIZING_POOL_DIR,", "    LAKE_FEATURES_SIZING_POOL_DIR,\n" + dir_str)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
