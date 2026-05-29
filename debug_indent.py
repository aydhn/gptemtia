with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    lines = f.readlines()
for i in range(280, 290):
    print(f"{i+1}: {repr(lines[i])}")
