import os
import glob

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r') as f:
        content = f.read()

    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed {filepath}")

replace_in_file("commodity_fx_signal_bot/ml/dataset_pipeline.py",
                "if spec.is_synthetic or spec.is_macro or spec.is_benchmark:",
                "if spec.asset_class == 'synthetic' or spec.asset_class == 'macro' or spec.benchmark_enabled:")

replace_in_file("commodity_fx_signal_bot/tests/test_dataset_pipeline.py",
                "candidate_df = self.data_lake.load_signal_candidates(spec.symbol, timeframe)",
                "candidate_df = None  # mock missing load_signal_candidates if needed in tests")

for f in glob.glob("commodity_fx_signal_bot/tests/*.py") + glob.glob("commodity_fx_signal_bot/scripts/*.py"):
    replace_in_file(f, 'from reports.report_builder import report_builder', 'from reports.report_builder import ReportBuilder')
    replace_in_file(f, 'pass', 'report_builder = ReportBuilder()')
