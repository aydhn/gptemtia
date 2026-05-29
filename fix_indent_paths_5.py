import re

with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    # Just aggressively strip and pad anything in ensure_project_directories that looks like it's supposed to be in the list
    if "LAKE_SCENARIO_REGRESSION_" in line or "REPORTS_SCENARIO_REGRESSION_" in line or "DOCS_SCENARIO_REGRESSION_" in line:
        if line.strip().endswith(",") and not line.strip().startswith("def") and not line.strip().startswith("import"):
             lines[i] = "        " + line.strip()

with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
    f.write('\n'.join(lines))
