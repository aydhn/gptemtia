import re

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    content = f.read()

# Replace the incorrect indentation in DataLake
if "    def save_scenario_regression_registry(" in content:
    content = content.replace("    def save_scenario_regression_registry(", "    def save_scenario_regression_registry(")

if "        def load_scenario_registry(self) -> pd.DataFrame:" in content:
    content = content.replace("        def load_scenario_registry(self) -> pd.DataFrame:", "    def load_scenario_registry(self) -> pd.DataFrame:")

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
    f.write(content)
