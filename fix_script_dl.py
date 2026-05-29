import glob

for filepath in glob.glob("commodity_fx_signal_bot/scripts/run_*_report.py") + glob.glob("commodity_fx_signal_bot/scripts/run_scenario_regression_*.py"):
    with open(filepath, 'r') as f:
        content = f.read()
    if "dl = DataLake()" in content:
        content = content.replace("dl = DataLake()", "from config.paths import LAKE_DIR\n    dl = DataLake(LAKE_DIR)")
        with open(filepath, 'w') as f:
            f.write(content)
