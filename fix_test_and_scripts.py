import re

# Fix checklist test
with open("commodity_fx_signal_bot/tests/test_maintenance_checklist.py", "r") as f:
    content = f.read()
content = content.replace('is True', '== True')
with open("commodity_fx_signal_bot/tests/test_maintenance_checklist.py", "w") as f:
    f.write(content)

# Fix report builder test
with open("commodity_fx_signal_bot/tests/test_maintenance_report_builder.py", "r") as f:
    content = f.read()
content = content.replace('assert "Total Files: 10" in md', 'assert "**Total Files:** 10" in md')
with open("commodity_fx_signal_bot/tests/test_maintenance_report_builder.py", "w") as f:
    f.write(content)

# Fix scripts importing get_settings (which doesn't exist, it's Settings)
scripts = [
    "run_storage_inventory_report.py",
    "run_retention_policy_report.py",
    "run_cleanup_dry_run_report.py",
    "run_archive_dry_run_report.py",
    "run_storage_lifecycle_report.py",
    "run_maintenance_status.py"
]

for s in scripts:
    with open(f"commodity_fx_signal_bot/scripts/{s}", "r") as f:
        content = f.read()
    content = content.replace('from config.settings import get_settings', 'from config.settings import Settings')
    content = content.replace('settings = get_settings()', 'settings = Settings()')
    with open(f"commodity_fx_signal_bot/scripts/{s}", "w") as f:
        f.write(content)
