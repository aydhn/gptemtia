import re

with open("commodity_fx_signal_bot/scripts/run_sizing_candidate_preview.py", "r") as f:
    content = f.read()

content = content.replace("from config.symbols import list_symbols\n", "")

with open("commodity_fx_signal_bot/scripts/run_sizing_candidate_preview.py", "w") as f:
    f.write(content)
