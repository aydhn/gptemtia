with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if line.strip() == "def load_scenario_registry(self) -> pd.DataFrame:" and not line.startswith("    def"):
        new_lines.append("    def load_scenario_registry(self) -> pd.DataFrame:\n")
    else:
        new_lines.append(line)

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
    f.writelines(new_lines)
