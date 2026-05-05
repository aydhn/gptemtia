import re
with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

insert_str1 = """
LAKE_FEATURES_STRATEGY_CANDIDATES_DIR = LAKE_FEATURES_DIR / "strategy_candidates"
LAKE_FEATURES_STRATEGY_POOL_DIR = LAKE_FEATURES_DIR / "strategy_pool"
STRATEGY_REPORTS_DIR = REPORTS_DIR / "strategy_reports"
"""

insert_str2 = """        LAKE_FEATURES_STRATEGY_CANDIDATES_DIR,
        LAKE_FEATURES_STRATEGY_POOL_DIR,
        STRATEGY_REPORTS_DIR,
"""

if "LAKE_FEATURES_STRATEGY_CANDIDATES_DIR" not in content:
    content = content.replace("def ensure_project_directories", insert_str1 + "\ndef ensure_project_directories")
    content = content.replace("        DECISION_REPORTS_DIR,", "        DECISION_REPORTS_DIR,\n" + insert_str2)
    with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
        f.write(content)
