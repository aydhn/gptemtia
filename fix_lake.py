import re

files_to_fix = [
    'commodity_fx_signal_bot/scripts/run_momentum_batch_build.py',
    'commodity_fx_signal_bot/scripts/run_momentum_event_preview.py',
    'commodity_fx_signal_bot/scripts/run_momentum_feature_preview.py',
    'commodity_fx_signal_bot/scripts/run_momentum_status.py',
]

for file_path in files_to_fix:
    with open(file_path, 'r') as f:
        content = f.read()

    # ensure config.paths import
    if "from config.paths import LAKE_DIR" not in content:
        content = "from config.paths import LAKE_DIR\n" + content

    content = content.replace("lake = DataLake()", "lake = DataLake(LAKE_DIR)")

    with open(file_path, 'w') as f:
        f.write(content)
