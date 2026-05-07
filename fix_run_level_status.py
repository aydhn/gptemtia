with open("commodity_fx_signal_bot/scripts/run_level_status.py", "r") as f:
    content = f.read()

content = content.replace("from config.symbols import ALL_SYMBOLS", "from config.symbols import get_symbol_map")
content = content.replace("for symbol, spec in ALL_SYMBOLS.items():", "for symbol, spec in get_symbol_map().items():\n        if symbol != spec.symbol: continue # skip aliases")

with open("commodity_fx_signal_bot/scripts/run_level_status.py", "w") as f:
    f.write(content)
