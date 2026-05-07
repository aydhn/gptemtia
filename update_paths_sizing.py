import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

paths_to_add = """# Risk Data Lake directories
LAKE_FEATURES_RISK_CANDIDATES_DIR = LAKE_FEATURES_DIR / "risk_candidates"
LAKE_FEATURES_RISK_POOL_DIR = LAKE_FEATURES_DIR / "risk_pool"

# Sizing Reports
REPORTS_SIZING_REPORTS_DIR = REPORTS_DIR / "sizing_reports"

# Sizing Data Lake directories
LAKE_FEATURES_SIZING_CANDIDATES_DIR = LAKE_FEATURES_DIR / "sizing_candidates"
LAKE_FEATURES_SIZING_POOL_DIR = LAKE_FEATURES_DIR / "sizing_pool"
"""

content = re.sub(r'# Risk Data Lake directories\s*LAKE_FEATURES_RISK_CANDIDATES_DIR = LAKE_FEATURES_DIR / "risk_candidates"\s*LAKE_FEATURES_RISK_POOL_DIR = LAKE_FEATURES_DIR / "risk_pool"', paths_to_add, content)

dirs_to_add = """        REPORTS_RISK_REPORTS_DIR,
        LAKE_FEATURES_RISK_CANDIDATES_DIR,
        LAKE_FEATURES_RISK_POOL_DIR,
        STRATEGY_RULE_REPORTS_DIR,
        REPORTS_SIZING_REPORTS_DIR,
        LAKE_FEATURES_SIZING_CANDIDATES_DIR,
        LAKE_FEATURES_SIZING_POOL_DIR,
"""

content = re.sub(r'        REPORTS_RISK_REPORTS_DIR,\s*LAKE_FEATURES_RISK_CANDIDATES_DIR,\s*LAKE_FEATURES_RISK_POOL_DIR,\s*STRATEGY_RULE_REPORTS_DIR,', dirs_to_add, content)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
