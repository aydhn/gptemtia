import ast

with open('commodity_fx_signal_bot/ml/feature_store.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip() == "def load_scenario_sample_data_manifest(self) -> pd.DataFrame:":
        lines[i] = "    def load_scenario_sample_data_manifest(self) -> pd.DataFrame:\n"
    if line.strip() == "def load_scenario_fixtures(self) -> pd.DataFrame:":
        lines[i] = "    def load_scenario_fixtures(self) -> pd.DataFrame:\n"
    if line.strip() == "def load_scenario_registry(self) -> pd.DataFrame:":
        lines[i] = "    def load_scenario_registry(self) -> pd.DataFrame:\n"

while True:
    try:
        ast.parse("".join(lines))
        break
    except IndentationError as e:
        print(f"fixing error at {e.lineno}")
        line = lines[e.lineno - 1]
        lines[e.lineno - 1] = "    " + line.lstrip()

with open('commodity_fx_signal_bot/ml/feature_store.py', 'w') as f:
    f.writelines(lines)
