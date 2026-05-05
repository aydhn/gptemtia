import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

insert_str1 = """
LAKE_FEATURES_DECISION_CANDIDATES_DIR = LAKE_FEATURES_DIR / "decision_candidates"
LAKE_FEATURES_DECISION_POOL_DIR = LAKE_FEATURES_DIR / "decision_pool"
DECISION_REPORTS_DIR = REPORTS_DIR / "decision_reports"
"""

content = content.replace('SIGNAL_REPORTS_DIR = REPORTS_DIR / "signal_reports"', 'SIGNAL_REPORTS_DIR = REPORTS_DIR / "signal_reports"' + insert_str1)

insert_str2 = """        LAKE_FEATURES_DECISION_CANDIDATES_DIR,
        LAKE_FEATURES_DECISION_POOL_DIR,
        DECISION_REPORTS_DIR,
"""

content = content.replace('        SIGNAL_REPORTS_DIR,\n    ]', '        SIGNAL_REPORTS_DIR,\n' + insert_str2 + '    ]')

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
