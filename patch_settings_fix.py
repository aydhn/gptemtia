from pathlib import Path
import re

def fix():
    p = Path("commodity_fx_signal_bot/config/settings.py")
    c = p.read_text()

    # Fix the indentation error around line 2385
    # Find:
    #     def __post_init__(self):
    #
    #
    #
    #
    #        self.live_trading_enabled = False
    #
    #    # Phase 49...

    # Let's just fix the indentation manually
    lines = c.split('\n')
    for i, line in enumerate(lines):
        if "knowledge_base_enabled: bool = field(" in line:
            # Check indentation. If it has only 4 spaces, change to 4 spaces inside class
            # Wait, these should be class attributes, NOT inside __post_init__.
            pass

    # Actually, look at the diff we applied:
    # addition = """
    # # Phase 49...
    # """
    # content = content.replace("self.live_trading_enabled = False", addition + "\n        self.live_trading_enabled = False")

    # This means the Phase 49 fields were injected INSIDE `__post_init__` instead of at the class level!
    # Let's fix this.

    # Read the file
    c = p.read_text()

    # Remove the bad injection
    # We will use regex to extract the Phase 49 block
    match = re.search(r'(# Phase 49: Knowledge Base & Analyst Workspace.*?knowledge_base_min_quality_score: float = field[^\n]+)', c, re.DOTALL)

    if match:
        block = match.group(1)
        c = c.replace(block, "")

        # Now find where to properly insert it (e.g. before def __post_init__)
        c = c.replace("    def __post_init__(self):", block + "\n    def __post_init__(self):")

        p.write_text(c)
        print("Fixed settings indentation.")
    else:
        print("Could not find Phase 49 block.")

fix()
