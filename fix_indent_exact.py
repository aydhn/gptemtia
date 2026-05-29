with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    lines = f.readlines()

def print_surrounding(idx):
    for i in range(max(0, idx-5), min(len(lines), idx+5)):
        print(f"{i+1}: {repr(lines[i])}")

print("Before:")
print_surrounding(287)

# Maybe the previous method isn't indented to 4? Let's check line 265 (start of save_scenario_registry)
for i in range(250, 300):
    if "def save_scenario_registry" in lines[i]:
        print(f"save_scenario_registry is at line {i+1}: {repr(lines[i])}")
