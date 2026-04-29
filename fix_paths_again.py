import re

with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
    paths_content = f.read()

if "MOMENTUM_REPORTS_DIR =" not in paths_content:
    new_paths = """
LAKE_FEATURES_MOMENTUM_DIR = LAKE_FEATURES_DIR / "momentum"
LAKE_FEATURES_MOMENTUM_EVENTS_DIR = LAKE_FEATURES_DIR / "momentum_events"
MOMENTUM_REPORTS_DIR = REPORTS_DIR / "momentum_reports"
"""
    paths_content = paths_content.replace("INDICATOR_REPORTS_DIR = REPORTS_DIR / \"indicator_reports\"", f"INDICATOR_REPORTS_DIR = REPORTS_DIR / \"indicator_reports\"{new_paths}")

    # add to ensure_project_directories
    directories_replacement = """        LAKE_FEATURES_TECHNICAL_DIR,
        LAKE_FEATURES_MOMENTUM_DIR,
        LAKE_FEATURES_MOMENTUM_EVENTS_DIR,
        LAKE_FEATURES_MANIFESTS_DIR,
        LAKE_FEATURES_REPORTS_DIR,
        INDICATOR_REPORTS_DIR,
        MOMENTUM_REPORTS_DIR,"""
    paths_content = paths_content.replace("""        LAKE_FEATURES_TECHNICAL_DIR,
        LAKE_FEATURES_MANIFESTS_DIR,
        LAKE_FEATURES_REPORTS_DIR,
        INDICATOR_REPORTS_DIR,""", directories_replacement)

    with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
        f.write(paths_content)

print("Fixed paths.py")
