import re

with open("commodity_fx_signal_bot/scripts/run_sizing_candidate_preview.py", "r") as f:
    content = f.read()

content = content.replace("from utils.logging_utils import setup_logging", "from utils.logger import setup_logging")
content = content.replace("from utils.symbol_manager import SymbolManager", "from config.symbols import get_symbol_spec\nfrom config.symbols import list_symbols")
content = content.replace("symbol_manager = SymbolManager()\n    spec = symbol_manager.get_spec(args.symbol)", "spec = get_symbol_spec(args.symbol)")

with open("commodity_fx_signal_bot/scripts/run_sizing_candidate_preview.py", "w") as f:
    f.write(content)
