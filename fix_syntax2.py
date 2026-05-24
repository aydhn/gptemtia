path = "commodity_fx_signal_bot/config/paths.py"
with open(path, "r") as f:
    content = f.read()

content = content.replace("REPORTS_SECURITY_REPORTS_DIR,\n    ,\n        DATA_LAKE_GOVERNANCE_DIR,", "REPORTS_SECURITY_REPORTS_DIR,\n        DATA_LAKE_GOVERNANCE_DIR,")

with open(path, "w") as f:
    f.write(content)
print("Fixed syntax")
