import re

with open("commodity_fx_signal_bot/scripts/run_sizing_candidate_preview.py", "r") as f:
    content = f.read()

content = content.replace("from utils.logger import setup_logging\n", "")
content = content.replace("setup_logging()\n    ", "logging.basicConfig(level=logging.INFO)\n    ")

with open("commodity_fx_signal_bot/scripts/run_sizing_candidate_preview.py", "w") as f:
    f.write(content)
