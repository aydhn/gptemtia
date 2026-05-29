with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if line.strip() == "def load_scenario_registry(self) -> pd.DataFrame:":
        lines[i] = "    def load_scenario_registry(self) -> pd.DataFrame:"

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
    f.write('\n'.join(lines))
