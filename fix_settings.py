import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    lines = f.readlines()

new_lines = []
in_settings = False
has_maintenance = False
for line in lines:
    if "class Settings:" in line:
        in_settings = True
    if "maintenance_enabled" in line:
        has_maintenance = True

    if in_settings and line.strip() == "def get_settings():" and not has_maintenance:
         pass # needs more complex patching

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

# Add settings loading from env
env_loading = """
        settings.maintenance_enabled = str(os.getenv("MAINTENANCE_ENABLED", "true")).lower() == "true"
        settings.default_maintenance_profile = os.getenv("DEFAULT_MAINTENANCE_PROFILE", "balanced_local_maintenance")
        settings.maintenance_default_timeframe = os.getenv("MAINTENANCE_DEFAULT_TIMEFRAME", "1d")
        settings.maintenance_dry_run_default = str(os.getenv("MAINTENANCE_DRY_RUN_DEFAULT", "true")).lower() == "true"
        settings.maintenance_allow_delete = str(os.getenv("MAINTENANCE_ALLOW_DELETE", "false")).lower() == "true"
        settings.maintenance_allow_archive_move = str(os.getenv("MAINTENANCE_ALLOW_ARCHIVE_MOVE", "false")).lower() == "true"
        settings.maintenance_scan_data_lake = str(os.getenv("MAINTENANCE_SCAN_DATA_LAKE", "true")).lower() == "true"
        settings.maintenance_scan_reports_output = str(os.getenv("MAINTENANCE_SCAN_REPORTS_OUTPUT", "true")).lower() == "true"
        settings.maintenance_scan_logs = str(os.getenv("MAINTENANCE_SCAN_LOGS", "true")).lower() == "true"
        settings.maintenance_scan_cache = str(os.getenv("MAINTENANCE_SCAN_CACHE", "true")).lower() == "true"
        settings.maintenance_scan_checkpoints = str(os.getenv("MAINTENANCE_SCAN_CHECKPOINTS", "true")).lower() == "true"
        settings.maintenance_max_inventory_files = int(os.getenv("MAINTENANCE_MAX_INVENTORY_FILES", "50000"))
        settings.maintenance_large_file_threshold_mb = int(os.getenv("MAINTENANCE_LARGE_FILE_THRESHOLD_MB", "100"))
        settings.maintenance_stale_days_default = int(os.getenv("MAINTENANCE_STALE_DAYS_DEFAULT", "30"))
        settings.maintenance_keep_latest_n_reports = int(os.getenv("MAINTENANCE_KEEP_LATEST_N_REPORTS", "10"))
        settings.maintenance_keep_latest_n_runs = int(os.getenv("MAINTENANCE_KEEP_LATEST_N_RUNS", "20"))
        settings.maintenance_keep_quality_reports_days = int(os.getenv("MAINTENANCE_KEEP_QUALITY_REPORTS_DAYS", "90"))
        settings.maintenance_keep_governance_reports_days = int(os.getenv("MAINTENANCE_KEEP_GOVERNANCE_REPORTS_DAYS", "180"))
        settings.maintenance_keep_experiment_manifests_days = int(os.getenv("MAINTENANCE_KEEP_EXPERIMENT_MANIFESTS_DAYS", "365"))
        settings.maintenance_keep_knowledge_index_days = int(os.getenv("MAINTENANCE_KEEP_KNOWLEDGE_INDEX_DAYS", "30"))
        settings.maintenance_keep_cache_days = int(os.getenv("MAINTENANCE_KEEP_CACHE_DAYS", "14"))
        settings.maintenance_keep_checkpoints_days = int(os.getenv("MAINTENANCE_KEEP_CHECKPOINTS_DAYS", "30"))
        settings.maintenance_archive_format = os.getenv("MAINTENANCE_ARCHIVE_FORMAT", "zip_manifest_only")
        settings.maintenance_archive_max_bundle_mb = int(os.getenv("MAINTENANCE_ARCHIVE_MAX_BUNDLE_MB", "1024"))
        settings.maintenance_save_reports = str(os.getenv("MAINTENANCE_SAVE_REPORTS", "true")).lower() == "true"
        settings.maintenance_min_quality_score = float(os.getenv("MAINTENANCE_MIN_QUALITY_SCORE", "0.40"))
"""
if "settings.maintenance_enabled" not in content:
    content = content.replace("        return settings", env_loading + "\n        return settings")
    with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
        f.write(content)
    print("settings.py get_settings patched")
else:
    print("settings.py get_settings already patched")
