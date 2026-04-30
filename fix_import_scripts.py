import os
import glob

for filename in ["commodity_fx_signal_bot/scripts/run_trend_batch_build.py", "commodity_fx_signal_bot/scripts/run_trend_status.py"]:
    with open(filename, "r") as f:
        content = f.read()

    content = content.replace("get_symbols_by_class", "get_symbols_by_asset_class")
    content = content.replace("from config.symbols import get_symbols_by_asset_class, get_symbol_spec, UNIVERSE", "from config.symbols import get_symbols_by_asset_class, get_symbol_spec, DEFAULT_SYMBOL_UNIVERSE")
    content = content.replace("from config.symbols import UNIVERSE", "from config.symbols import DEFAULT_SYMBOL_UNIVERSE")
    content = content.replace("UNIVERSE", "DEFAULT_SYMBOL_UNIVERSE")

    with open(filename, "w") as f:
        f.write(content)
