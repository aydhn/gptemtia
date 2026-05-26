import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

maintenance_paths = """
    # Maintenance Paths
    MAINTENANCE_DIR = DATA_LAKE_DIR / "maintenance"
    MAINTENANCE_INVENTORY_DIR = MAINTENANCE_DIR / "inventory"
    MAINTENANCE_POLICIES_DIR = MAINTENANCE_DIR / "policies"
    MAINTENANCE_CLEANUP_DIR = MAINTENANCE_DIR / "cleanup"
    MAINTENANCE_ARCHIVE_DIR = MAINTENANCE_DIR / "archive"
    MAINTENANCE_ROTATION_DIR = MAINTENANCE_DIR / "rotation"
    MAINTENANCE_DUPLICATES_DIR = MAINTENANCE_DIR / "duplicates"
    MAINTENANCE_STALE_DIR = MAINTENANCE_DIR / "stale"
    MAINTENANCE_LARGE_ARTIFACTS_DIR = MAINTENANCE_DIR / "large_artifacts"
    MAINTENANCE_GROWTH_DIR = MAINTENANCE_DIR / "growth"
    MAINTENANCE_CHECKLISTS_DIR = MAINTENANCE_DIR / "checklists"
    MAINTENANCE_LIFECYCLE_DIR = MAINTENANCE_DIR / "lifecycle"
    MAINTENANCE_QUALITY_DIR = MAINTENANCE_DIR / "quality"

    REPORTS_MAINTENANCE_DIR = REPORTS_OUTPUT_DIR / "maintenance"
    REPORTS_MAINTENANCE_CSV_DIR = REPORTS_MAINTENANCE_DIR / "csv"
    REPORTS_MAINTENANCE_MARKDOWN_DIR = REPORTS_MAINTENANCE_DIR / "markdown"
    REPORTS_MAINTENANCE_TXT_DIR = REPORTS_MAINTENANCE_DIR / "txt"
    REPORTS_MAINTENANCE_JSON_DIR = REPORTS_MAINTENANCE_DIR / "json"

    ARCHIVES_DIR = PROJECT_ROOT / "archives"
    ARCHIVES_MANIFESTS_DIR = ARCHIVES_DIR / "manifests"
    ARCHIVES_BUNDLES_DIR = ARCHIVES_DIR / "bundles"
"""

if "MAINTENANCE_DIR" not in content:
    # Insert after FEATURE_STORE_DIR or similar
    content = re.sub(r'(class ProjectPaths:\n(.*\n)*?)(?=\n    @classmethod)', r'\1' + maintenance_paths, content)

dirs_to_add = """
            cls.MAINTENANCE_DIR,
            cls.MAINTENANCE_INVENTORY_DIR,
            cls.MAINTENANCE_POLICIES_DIR,
            cls.MAINTENANCE_CLEANUP_DIR,
            cls.MAINTENANCE_ARCHIVE_DIR,
            cls.MAINTENANCE_ROTATION_DIR,
            cls.MAINTENANCE_DUPLICATES_DIR,
            cls.MAINTENANCE_STALE_DIR,
            cls.MAINTENANCE_LARGE_ARTIFACTS_DIR,
            cls.MAINTENANCE_GROWTH_DIR,
            cls.MAINTENANCE_CHECKLISTS_DIR,
            cls.MAINTENANCE_LIFECYCLE_DIR,
            cls.MAINTENANCE_QUALITY_DIR,
            cls.REPORTS_MAINTENANCE_DIR,
            cls.REPORTS_MAINTENANCE_CSV_DIR,
            cls.REPORTS_MAINTENANCE_MARKDOWN_DIR,
            cls.REPORTS_MAINTENANCE_TXT_DIR,
            cls.REPORTS_MAINTENANCE_JSON_DIR,
            cls.ARCHIVES_DIR,
            cls.ARCHIVES_MANIFESTS_DIR,
            cls.ARCHIVES_BUNDLES_DIR,
"""

if "cls.MAINTENANCE_DIR" not in content:
    content = content.replace("        dirs = [", "        dirs = [" + dirs_to_add)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
print("paths.py patched")
