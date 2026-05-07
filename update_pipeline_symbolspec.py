import re

with open("commodity_fx_signal_bot/sizing/sizing_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("from config.symbol_config import SymbolSpec", "from config.symbols import SymbolSpec")

with open("commodity_fx_signal_bot/sizing/sizing_pipeline.py", "w") as f:
    f.write(content)
