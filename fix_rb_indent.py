import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    lines = f.readlines()

# The class indentation in report_builder is 4 spaces, so the methods should be 4 spaces.
new_lines = []
for line in lines:
    if line.startswith("    # --- MAINTENANCE REPORTING ---"):
        new_lines.append(line)
        continue
    new_lines.append(line)

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.writelines(new_lines)
