import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

# Let's check if the replacement worked
print("LAKE_SYNTHETIC_INDICES_DIR" in content)
