import glob

# Check SymbolSpec constructor
with open("commodity_fx_signal_bot/config/symbols.py", "r") as f:
    print("--- config/symbols.py ---")
    for line in f.readlines()[:30]:
        print(line.strip())
