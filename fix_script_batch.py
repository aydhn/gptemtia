import re

with open("commodity_fx_signal_bot/scripts/run_sizing_batch_build.py", "r") as f:
    content = f.read()

content = content.replace(
    "from config.symbols import get_symbol_spec, COMMODITIES, FOREX",
    "from config.symbols import get_enabled_symbols"
)
content = content.replace(
    "all_specs = COMMODITIES + FOREX",
    "all_specs = get_enabled_symbols()"
)

with open("commodity_fx_signal_bot/scripts/run_sizing_batch_build.py", "w") as f:
    f.write(content)
