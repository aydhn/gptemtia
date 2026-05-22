import os
import glob

# Search all files in synthetic_indices, scripts, and tests for "core.symbol_registry" and replace with "config.symbols"
files_to_check = glob.glob("commodity_fx_signal_bot/synthetic_indices/*.py") + \
                 glob.glob("commodity_fx_signal_bot/scripts/*.py") + \
                 glob.glob("commodity_fx_signal_bot/tests/*.py")

for file in files_to_check:
    with open(file, 'r') as f:
        content = f.read()

    if "core.symbol_registry" in content:
        content = content.replace("core.symbol_registry", "config.symbols")
        with open(file, 'w') as f:
            f.write(content)
