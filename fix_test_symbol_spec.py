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

for f in glob.glob("commodity_fx_signal_bot/tests/*.py") + glob.glob("commodity_fx_signal_bot/scripts/*.py"):
    replace_in_file(f, 'SymbolSpec(symbol="TEST", asset_class="unknown")', 'SymbolSpec(symbol="TEST", name="Test", asset_class="test", sub_class="test", currency="USD")')
    replace_in_file(f, 'SymbolSpec(symbol="TEST1", asset_class="unknown")', 'SymbolSpec(symbol="TEST1", name="Test 1", asset_class="test", sub_class="test", currency="USD")')
    replace_in_file(f, 'from reports.report_builder import ReportBuilder', 'from reports.report_builder import report_builder')
    replace_in_file(f, 'report_builder = ReportBuilder()', 'pass')
