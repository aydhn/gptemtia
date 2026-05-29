with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    lines = f.readlines()

for i in range(250, 450):
    if lines[i].startswith("def save_scenario_registry"):
        lines[i] = "    " + lines[i]
    if lines[i].startswith("    def load_scenario_regression_registry("):
        pass # ok
    if lines[i].startswith("    def save_scenario_regression_registry("):
        pass # ok

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
    f.writelines(lines)
