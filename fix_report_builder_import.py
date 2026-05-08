import glob

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r') as f:
        content = f.read()

    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w') as f:
            f.write(content)

for f in glob.glob("commodity_fx_signal_bot/scripts/run_ml_*.py") + glob.glob("commodity_fx_signal_bot/tests/test_ml_dataset_scripts_contract.py"):
    replace_in_file(f, 'from reports.report_builder import report_builder', 'from reports.report_builder import ReportBuilder')
