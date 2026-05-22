import glob

files = glob.glob("commodity_fx_signal_bot/tests/test_benchmark_definitions.py") + glob.glob("commodity_fx_signal_bot/tests/test_index_universe.py")

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # We need to add the missing argument for SymbolSpec. It expects 5 arguments, we gave 4.
    content = content.replace("SymbolSpec(\"XAUUSD\", \"COMMODITY\", \"PRECIOUS_METAL\", \"Gold\")", "SymbolSpec(\"XAUUSD\", \"COMMODITY\", \"PRECIOUS_METAL\", \"Gold\", True)")
    content = content.replace("SymbolSpec(\"XAGUSD\", \"COMMODITY\", \"PRECIOUS_METAL\", \"Silver\")", "SymbolSpec(\"XAGUSD\", \"COMMODITY\", \"PRECIOUS_METAL\", \"Silver\", True)")
    content = content.replace("SymbolSpec(\"CL=F\", \"COMMODITY\", \"ENERGY\", \"Oil\")", "SymbolSpec(\"CL=F\", \"COMMODITY\", \"ENERGY\", \"Oil\", True)")
    content = content.replace("SymbolSpec(\"USDTRY=X\", \"FX\", \"EMERGING\", \"USD TRY\")", "SymbolSpec(\"USDTRY=X\", \"FX\", \"EMERGING\", \"USD TRY\", True)")
    content = content.replace("SymbolSpec(\"EURUSD=X\", \"FX\", \"MAJOR\", \"EUR USD\")", "SymbolSpec(\"EURUSD=X\", \"FX\", \"MAJOR\", \"EUR USD\", True)")

    with open(file, 'w') as f:
        f.write(content)
