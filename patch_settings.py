import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

maintenance_settings = """
    # Maintenance Settings
    maintenance_enabled: bool = True
    default_maintenance_profile: str = "balanced_local_maintenance"
    maintenance_default_timeframe: str = "1d"
    maintenance_dry_run_default: bool = True
    maintenance_allow_delete: bool = False
    maintenance_allow_archive_move: bool = False
    maintenance_scan_data_lake: bool = True
    maintenance_scan_reports_output: bool = True
    maintenance_scan_logs: bool = True
    maintenance_scan_cache: bool = True
    maintenance_scan_checkpoints: bool = True
    maintenance_max_inventory_files: int = 50000
    maintenance_large_file_threshold_mb: int = 100
    maintenance_stale_days_default: int = 30
    maintenance_keep_latest_n_reports: int = 10
    maintenance_keep_latest_n_runs: int = 20
    maintenance_keep_quality_reports_days: int = 90
    maintenance_keep_governance_reports_days: int = 180
    maintenance_keep_experiment_manifests_days: int = 365
    maintenance_keep_knowledge_index_days: int = 30
    maintenance_keep_cache_days: int = 14
    maintenance_keep_checkpoints_days: int = 30
    maintenance_archive_format: str = "zip_manifest_only"
    maintenance_archive_max_bundle_mb: int = 1024
    maintenance_save_reports: bool = True
    maintenance_min_quality_score: float = 0.40
"""

if "maintenance_enabled" not in content:
    content = re.sub(r'(class Settings:\n(.*\n)*?)(?=\n    @classmethod)', r'\1' + maintenance_settings, content)
    with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
        f.write(content)
    print("settings.py patched")
else:
    print("settings.py already patched")
