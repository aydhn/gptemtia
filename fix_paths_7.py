with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    lines = f.readlines()

lines = lines[:1011]

with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
    f.writelines(lines)
