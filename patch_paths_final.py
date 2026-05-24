from pathlib import Path

def patch():
    p = Path("commodity_fx_signal_bot/config/paths.py")
    c = p.read_text()

    if "REPORTS_OUTPUT_DIR = REPORTS_DIR" not in c:
        # It's probably missing. Let's add it where REPORTS_DIR is defined.
        c = c.replace("REPORTS_DIR = PROJECT_ROOT / \"reports\"", "REPORTS_DIR = PROJECT_ROOT / \"reports\"\nREPORTS_OUTPUT_DIR = REPORTS_DIR / \"output\"")
        p.write_text(c)
        print("Patched REPORTS_OUTPUT_DIR")
    else:
        print("REPORTS_OUTPUT_DIR already exists.")

patch()
