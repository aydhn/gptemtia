from pathlib import Path

def fix():
    # Remove old __init__.py if it exists
    p = Path("commodity_fx_signal_bot/knowledge_base/__init__.py")
    if p.exists():
        p.unlink()

fix()
