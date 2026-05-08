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

for f in glob.glob("commodity_fx_signal_bot/ml/*.py") + glob.glob("commodity_fx_signal_bot/tests/*.py") + glob.glob("commodity_fx_signal_bot/scripts/*.py"):
    replace_in_file(f, "from core.symbol_spec import SymbolSpec", "from config.symbols import SymbolSpec")
