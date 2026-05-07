import re

with open("commodity_fx_signal_bot/tests/test_sizing_quality.py", "r") as f:
    content = f.read()

content = content.replace('def test_check_sizing_candidate_duplicates():\n    df = pd.DataFrame({"sizing_id": ["a", "b", "a"]})', 'def test_check_sizing_candidate_duplicates():\n    df = pd.DataFrame({"sizing_id": ["a", "b", "a"], "timestamp": ["1", "2", "3"]})')

with open("commodity_fx_signal_bot/tests/test_sizing_quality.py", "w") as f:
    f.write(content)


with open("commodity_fx_signal_bot/tests/test_sizing_pipeline.py", "r") as f:
    content = f.read()

content = content.replace('from config.symbols import SymbolSpec', 'from config.symbols import SymbolSpec')

with open("commodity_fx_signal_bot/tests/test_sizing_pipeline.py", "w") as f:
    f.write(content)


with open("commodity_fx_signal_bot/tests/test_sizing_scripts_contract.py", "r") as f:
    content = f.read()

content = content.replace('cwd="commodity_fx_signal_bot"', 'cwd="."')

with open("commodity_fx_signal_bot/tests/test_sizing_scripts_contract.py", "w") as f:
    f.write(content)
