with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if line == '    def load_scenario_registry(self) -> pd.DataFrame:\n':
        if "return file_path\n" in lines[i-2] or "return file_path\n" in lines[i-1]:
            # Indent issue is probably because the previous method is indented to 4 spaces, but maybe there's a mix
            pass
    if line.strip() == "def load_scenario_registry(self) -> pd.DataFrame:":
        new_lines.append("    def load_scenario_registry(self) -> pd.DataFrame:\n")
    else:
        new_lines.append(line)

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
    f.writelines(new_lines)
