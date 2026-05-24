import sys

paths_path = "commodity_fx_signal_bot/config/paths.py"
with open(paths_path, 'r') as f:
    content = f.read()

ensure_start = content.find("def ensure_project_directories() -> None:")
if ensure_start != -1:
    dirs_start = content.find("directories = [", ensure_start)
    dirs_end = content.find("]", dirs_start)

    new_dirs = """,
        DATA_LAKE_GOVERNANCE_DIR,
        DATA_LAKE_GOVERNANCE_INVENTORY_DIR,
        DATA_LAKE_GOVERNANCE_FINGERPRINTS_DIR,
        DATA_LAKE_GOVERNANCE_PROVENANCE_DIR,
        DATA_LAKE_GOVERNANCE_LINEAGE_DIR,
        DATA_LAKE_GOVERNANCE_DEPENDENCIES_DIR,
        DATA_LAKE_GOVERNANCE_AUDIT_DIR,
        DATA_LAKE_GOVERNANCE_SOURCE_ATTRIBUTION_DIR,
        DATA_LAKE_GOVERNANCE_CHECKLISTS_DIR,
        DATA_LAKE_GOVERNANCE_QUALITY_DIR,
        REPORTS_GOVERNANCE_DIR,
        REPORTS_GOVERNANCE_CSV_DIR,
        REPORTS_GOVERNANCE_MARKDOWN_DIR,
        REPORTS_GOVERNANCE_TXT_DIR,
        REPORTS_GOVERNANCE_JSON_DIR"""

    content = content[:dirs_end] + new_dirs + content[dirs_end:]

    with open(paths_path, 'w') as f:
        f.write(content)
    print("Fixed paths.py")
else:
    print("Not found")
