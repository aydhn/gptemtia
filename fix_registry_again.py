with open("commodity_fx_signal_bot/indicators/registry.py", "r") as f:
    lines = f.readlines()

# Remove lines 96-99
with open("commodity_fx_signal_bot/indicators/registry.py", "w") as f:
    for i, line in enumerate(lines):
        if 95 <= i <= 98: # Zero-based indexing for lines 96-99
            continue
        f.write(line)
