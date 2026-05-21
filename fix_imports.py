import os
import glob

# Search for the wrong import get_universe_specs and replace with get_enabled_symbols
scripts = glob.glob("commodity_fx_signal_bot/scripts/run_*.py")

for script in scripts:
    with open(script, "r") as f:
        content = f.read()

    if "get_universe_specs" in content:
        content = content.replace("get_universe_specs", "get_enabled_symbols")
        with open(script, "w") as f:
            f.write(content)
