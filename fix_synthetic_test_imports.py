import os

with open("commodity_fx_signal_bot/tests/test_composite_index_builder.py", "r") as f:
    content = f.read()
content = content.replace("from core.symbol_registry import SymbolSpec", "from config.symbols import SymbolSpec")
with open("commodity_fx_signal_bot/tests/test_composite_index_builder.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/tests/test_index_pipeline.py", "r") as f:
    content = f.read()
content = content.replace("from core.symbol_registry import SymbolSpec", "from config.symbols import SymbolSpec")
with open("commodity_fx_signal_bot/tests/test_index_pipeline.py", "w") as f:
    f.write(content)
