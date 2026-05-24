path = "commodity_fx_signal_bot/config/paths.py"
with open(path, "r") as f:
    content = f.read()

# Let's see what's on line 409
lines = content.split('\n')
for i, line in enumerate(lines):
    if "," in line and "REPORTS_GOVERNANCE_JSON_DIR" in line:
        pass
    if "DATA_LAKE_GOVERNANCE_DIR" in line and "directories = [" in lines[i-1]:
        print(f"Around line {i}: {lines[i-2:i+2]}")
