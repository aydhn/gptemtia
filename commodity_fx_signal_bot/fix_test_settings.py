with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()
if "backup_recovery_enabled" not in content:
    print("missing")
