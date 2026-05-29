import re

with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    content = f.read()

lines = content.split('\n')
in_ensure = False
for i, line in enumerate(lines):
    if "def ensure_project_directories() -> None:" in line:
        in_ensure = True
    elif in_ensure and "directories = [" in line:
        in_ensure = True
    elif in_ensure and line.strip() == "]":
        in_ensure = False
    elif in_ensure and "LAKE_" in line and not line.startswith("        "):
        # Fix indentation
        lines[i] = "        " + line.strip()
    elif in_ensure and "REPORTS_" in line and not line.startswith("        "):
        lines[i] = "        " + line.strip()
    elif in_ensure and "DOCS_" in line and not line.startswith("        "):
        lines[i] = "        " + line.strip()

with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
    f.write('\n'.join(lines))
