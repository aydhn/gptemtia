import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

insert_str = """
LAKE_FEATURES_STRATEGY_RULE_CANDIDATES_DIR = LAKE_FEATURES_DIR / "strategy_rule_candidates"
LAKE_FEATURES_ENTRY_EXIT_CANDIDATES_DIR = LAKE_FEATURES_DIR / "entry_exit_candidates"
LAKE_FEATURES_STRATEGY_RULE_POOL_DIR = LAKE_FEATURES_DIR / "strategy_rule_pool"
STRATEGY_RULE_REPORTS_DIR = REPORTS_DIR / "strategy_rule_reports"
"""

if "LAKE_FEATURES_STRATEGY_RULE_CANDIDATES_DIR" not in content:
    content = content.replace('STRATEGY_REPORTS_DIR = REPORTS_DIR / "strategy_reports"', 'STRATEGY_REPORTS_DIR = REPORTS_DIR / "strategy_reports"\n' + insert_str)

dir_insert_str = """
        LAKE_FEATURES_STRATEGY_RULE_CANDIDATES_DIR,
        LAKE_FEATURES_ENTRY_EXIT_CANDIDATES_DIR,
        LAKE_FEATURES_STRATEGY_RULE_POOL_DIR,
        STRATEGY_RULE_REPORTS_DIR,
"""

if "LAKE_FEATURES_STRATEGY_RULE_CANDIDATES_DIR," not in content:
    content = content.replace('        STRATEGY_REPORTS_DIR,\n    ]', '        STRATEGY_REPORTS_DIR,\n' + dir_insert_str + '    ]')

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
