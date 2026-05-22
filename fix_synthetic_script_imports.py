import glob

# Replace "get_all_symbol_specs" with "get_enabled_symbols" in scripts
files = glob.glob("commodity_fx_signal_bot/scripts/run_*_report.py")

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    content = content.replace('get_all_symbol_specs', 'get_enabled_symbols')

    with open(file, 'w') as f:
        f.write(content)
