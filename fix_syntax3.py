path = "commodity_fx_signal_bot/config/paths.py"
with open(path, "r") as f:
    content = f.read()

# Fix the NameError by bringing the definitions BEFORE ensure_project_directories
if "DATA_LAKE_GOVERNANCE_DIR = DATA_LAKE_DIR" in content:
    print("Found definition")
else:
    print("Definition missing!")

# Let's check where it is
lines = content.split('\n')
for i, line in enumerate(lines):
    if "DATA_LAKE_GOVERNANCE_DIR = " in line:
        print(f"Line {i}: {line}")
    if "def ensure_project_directories" in line:
        print(f"Line {i}: {line}")
