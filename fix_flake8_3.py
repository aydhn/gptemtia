import re

files_to_fix = [
    'commodity_fx_signal_bot/tests/test_momentum_scripts_contract.py',
]

for file_path in files_to_fix:
    with open(file_path, 'r') as f:
        content = f.read()

    content = content.replace("import pytest\n", "")

    with open(file_path, 'w') as f:
        f.write(content)
