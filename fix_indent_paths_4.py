import re

with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if "LAKE_SCENARIO_REGRESSION_DIR," in line and not line.startswith("        ") and "directories" not in line:
        lines[i] = "        " + line.strip()

with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
    f.write('\n'.join(lines))
