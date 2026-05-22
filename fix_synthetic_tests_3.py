import glob

# The attributes of SymbolSpec are:
# symbol, name, asset_class, sub_class, currency, data_source

# Fix test_benchmark_definitions.py
with open("commodity_fx_signal_bot/tests/test_benchmark_definitions.py", "r") as f:
    content = f.read()

content = content.replace('SymbolSpec("XAUUSD", "COMMODITY", "PRECIOUS_METAL", "Gold", True)', 'SymbolSpec(symbol="XAUUSD", name="Gold", asset_class="COMMODITY", sub_class="PRECIOUS_METAL", currency="USD", data_source="yahoo")')
content = content.replace('SymbolSpec("XAGUSD", "COMMODITY", "PRECIOUS_METAL", "Silver", True)', 'SymbolSpec(symbol="XAGUSD", name="Silver", asset_class="COMMODITY", sub_class="PRECIOUS_METAL", currency="USD", data_source="yahoo")')
content = content.replace('SymbolSpec("CL=F", "COMMODITY", "ENERGY", "Oil", True)', 'SymbolSpec(symbol="CL=F", name="Oil", asset_class="COMMODITY", sub_class="ENERGY", currency="USD", data_source="yahoo")')
content = content.replace('SymbolSpec("USDTRY=X", "FX", "EMERGING", "USD TRY", True)', 'SymbolSpec(symbol="USDTRY=X", name="USD TRY", asset_class="FX", sub_class="EMERGING", currency="TRY", data_source="yahoo")')
content = content.replace('SymbolSpec("EURUSD=X", "FX", "MAJOR", "EUR USD", True)', 'SymbolSpec(symbol="EURUSD=X", name="EUR USD", asset_class="FX", sub_class="MAJOR", currency="USD", data_source="yahoo")')

with open("commodity_fx_signal_bot/tests/test_benchmark_definitions.py", "w") as f:
    f.write(content)

# Fix test_index_universe.py
with open("commodity_fx_signal_bot/tests/test_index_universe.py", "r") as f:
    content = f.read()

content = content.replace('SymbolSpec("XAUUSD", "COMMODITY", "PRECIOUS_METAL", "Gold", True)', 'SymbolSpec(symbol="XAUUSD", name="Gold", asset_class="COMMODITY", sub_class="PRECIOUS_METAL", currency="USD", data_source="yahoo")')
content = content.replace('SymbolSpec("CL=F", "COMMODITY", "ENERGY", "Oil", True)', 'SymbolSpec(symbol="CL=F", name="Oil", asset_class="COMMODITY", sub_class="ENERGY", currency="USD", data_source="yahoo")')
content = content.replace('SymbolSpec("USDTRY=X", "FX", "EMERGING", "USD TRY", True)', 'SymbolSpec(symbol="USDTRY=X", name="USD TRY", asset_class="FX", sub_class="EMERGING", currency="TRY", data_source="yahoo")')
content = content.replace('SymbolSpec("EURUSD=X", "FX", "MAJOR", "EUR USD", True)', 'SymbolSpec(symbol="EURUSD=X", name="EUR USD", asset_class="FX", sub_class="MAJOR", currency="USD", data_source="yahoo")')

with open("commodity_fx_signal_bot/tests/test_index_universe.py", "w") as f:
    f.write(content)

# Also fix the use of "group" since it is actually "sub_class" in SymbolSpec
with open("commodity_fx_signal_bot/synthetic_indices/index_universe.py", "r") as f:
    content = f.read()

content = content.replace('s.group in', 's.sub_class in')

with open("commodity_fx_signal_bot/synthetic_indices/index_universe.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/tests/test_index_pipeline.py", "r") as f:
    content = f.read()

content = content.replace('self.group = group', 'self.sub_class = group')

with open("commodity_fx_signal_bot/tests/test_index_pipeline.py", "w") as f:
    f.write(content)
