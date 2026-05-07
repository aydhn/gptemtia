import re

# Fix sizing_pipeline symbol spec properties (use data_source and asset_class instead)
with open("commodity_fx_signal_bot/sizing/sizing_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("spec.is_synthetic or spec.is_macro or spec.is_benchmark", "spec.data_source == 'synthetic' or spec.asset_class in ['macro', 'benchmark']")

with open("commodity_fx_signal_bot/sizing/sizing_pipeline.py", "w") as f:
    f.write(content)

# Fix test_sizing_quality np.False_ issue by checking not res["passed"] or res["passed"] == False
with open("commodity_fx_signal_bot/tests/test_sizing_quality.py", "r") as f:
    content = f.read()

content = content.replace('assert res["passed"] is False', 'assert not res["passed"]')

with open("commodity_fx_signal_bot/tests/test_sizing_quality.py", "w") as f:
    f.write(content)
