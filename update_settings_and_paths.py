import os
import sys

# Update settings.py
settings_path = "commodity_fx_signal_bot/config/settings.py"
with open(settings_path, 'r') as f:
    settings_content = f.read()

new_settings = """
    # Governance Settings (Phase 47)
    governance_enabled: bool = True
    default_governance_profile: str = "balanced_research_governance"
    governance_default_timeframe: str = "1d"
    governance_scan_data_lake: bool = True
    governance_scan_reports_output: bool = True
    governance_capture_file_hashes: bool = True
    governance_capture_schema_fingerprints: bool = True
    governance_capture_row_counts: bool = True
    governance_capture_modified_times: bool = True
    governance_capture_artifact_sizes: bool = True
    governance_max_file_hash_mb: int = 50
    governance_lineage_max_depth: int = 8
    governance_require_provenance_for_research_outputs: bool = True
    governance_require_fingerprint_for_key_artifacts: bool = True
    governance_require_audit_trail: bool = True
    governance_save_inventory: bool = True
    governance_save_lineage: bool = True
    governance_save_audit_trail: bool = True
    governance_save_reports: bool = True
    governance_min_quality_score: float = 0.40
"""

if "governance_enabled: bool" not in settings_content:
    # Find a good place to insert, e.g. after experiment_tracking_enabled
    insert_point = settings_content.find("experiment_tracking_enabled: bool")
    if insert_point != -1:
        # Find the end of that line
        end_of_line = settings_content.find("\n", insert_point)
        settings_content = settings_content[:end_of_line+1] + new_settings + settings_content[end_of_line+1:]
        with open(settings_path, 'w') as f:
            f.write(settings_content)
        print("Updated settings.py")
    else:
        print("Could not find insert point in settings.py")

# Update paths.py
paths_path = "commodity_fx_signal_bot/config/paths.py"
with open(paths_path, 'r') as f:
    paths_content = f.read()

new_paths = """
# Governance Paths
DATA_LAKE_GOVERNANCE_DIR = DATA_LAKE_DIR / "governance"
DATA_LAKE_GOVERNANCE_INVENTORY_DIR = DATA_LAKE_GOVERNANCE_DIR / "inventory"
DATA_LAKE_GOVERNANCE_FINGERPRINTS_DIR = DATA_LAKE_GOVERNANCE_DIR / "fingerprints"
DATA_LAKE_GOVERNANCE_PROVENANCE_DIR = DATA_LAKE_GOVERNANCE_DIR / "provenance"
DATA_LAKE_GOVERNANCE_LINEAGE_DIR = DATA_LAKE_GOVERNANCE_DIR / "lineage"
DATA_LAKE_GOVERNANCE_DEPENDENCIES_DIR = DATA_LAKE_GOVERNANCE_DIR / "dependencies"
DATA_LAKE_GOVERNANCE_AUDIT_DIR = DATA_LAKE_GOVERNANCE_DIR / "audit"
DATA_LAKE_GOVERNANCE_SOURCE_ATTRIBUTION_DIR = DATA_LAKE_GOVERNANCE_DIR / "source_attribution"
DATA_LAKE_GOVERNANCE_CHECKLISTS_DIR = DATA_LAKE_GOVERNANCE_DIR / "checklists"
DATA_LAKE_GOVERNANCE_QUALITY_DIR = DATA_LAKE_GOVERNANCE_DIR / "quality"

REPORTS_GOVERNANCE_DIR = REPORTS_OUTPUT_DIR / "governance"
REPORTS_GOVERNANCE_CSV_DIR = REPORTS_GOVERNANCE_DIR / "csv"
REPORTS_GOVERNANCE_MARKDOWN_DIR = REPORTS_GOVERNANCE_DIR / "markdown"
REPORTS_GOVERNANCE_TXT_DIR = REPORTS_GOVERNANCE_DIR / "txt"
REPORTS_GOVERNANCE_JSON_DIR = REPORTS_GOVERNANCE_DIR / "json"
"""

if "DATA_LAKE_GOVERNANCE_DIR" not in paths_content:
    paths_content += "\n" + new_paths

    # Also update ensure_project_directories
    ensure_func_start = paths_content.find("def ensure_project_directories():")
    if ensure_func_start != -1:
        # Find the list of directories
        dirs_start = paths_content.find("directories = [", ensure_func_start)
        if dirs_start != -1:
            dirs_end = paths_content.find("]", dirs_start)
            dirs_list = paths_content[dirs_start:dirs_end]

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

            paths_content = paths_content[:dirs_end] + new_dirs + paths_content[dirs_end:]
            with open(paths_path, 'w') as f:
                f.write(paths_content)
            print("Updated paths.py")
        else:
            print("Could not find directories list in paths.py")
    else:
        print("Could not find ensure_project_directories in paths.py")

# Update .env.example
env_path = "commodity_fx_signal_bot/.env.example"
with open(env_path, 'a') as f:
    f.write("""
# Governance Settings
GOVERNANCE_ENABLED=true
DEFAULT_GOVERNANCE_PROFILE=balanced_research_governance
GOVERNANCE_DEFAULT_TIMEFRAME=1d
GOVERNANCE_SCAN_DATA_LAKE=true
GOVERNANCE_SCAN_REPORTS_OUTPUT=true
GOVERNANCE_CAPTURE_FILE_HASHES=true
GOVERNANCE_CAPTURE_SCHEMA_FINGERPRINTS=true
GOVERNANCE_CAPTURE_ROW_COUNTS=true
GOVERNANCE_CAPTURE_MODIFIED_TIMES=true
GOVERNANCE_CAPTURE_ARTIFACT_SIZES=true
GOVERNANCE_MAX_FILE_HASH_MB=50
GOVERNANCE_LINEAGE_MAX_DEPTH=8
GOVERNANCE_REQUIRE_PROVENANCE_FOR_RESEARCH_OUTPUTS=true
GOVERNANCE_REQUIRE_FINGERPRINT_FOR_KEY_ARTIFACTS=true
GOVERNANCE_REQUIRE_AUDIT_TRAIL=true
GOVERNANCE_SAVE_INVENTORY=true
GOVERNANCE_SAVE_LINEAGE=true
GOVERNANCE_SAVE_AUDIT_TRAIL=true
GOVERNANCE_SAVE_REPORTS=true
GOVERNANCE_MIN_QUALITY_SCORE=0.40
""")
print("Updated .env.example")
