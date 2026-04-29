import re

files_to_fix = [
    'commodity_fx_signal_bot/tests/test_momentum_events.py',
    'commodity_fx_signal_bot/tests/test_momentum_advanced.py',
    'commodity_fx_signal_bot/tests/test_momentum_feature_set.py',
]

for file_path in files_to_fix:
    with open(file_path, 'r') as f:
        content = f.read()

    # ensure pytest exists
    if "import pytest" not in content:
        content = "import pytest\n" + content

    with open(file_path, 'w') as f:
        f.write(content)
