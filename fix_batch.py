with open("commodity_fx_signal_bot/scripts/run_level_batch_build.py", "r") as f:
    content = f.read()

content = content.replace("from config.symbols import ALL_SYMBOLS\n        specs = [s for s in ALL_SYMBOLS.values()]", "from config.symbols import get_symbol_map\n        specs = list(get_symbol_map().values())")

with open("commodity_fx_signal_bot/scripts/run_level_batch_build.py", "w") as f:
    f.write(content)
