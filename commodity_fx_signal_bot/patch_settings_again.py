def fix_settings():
    file_path = "config/settings.py"
    with open(file_path, "r") as f:
        content = f.read()

    # The previous patch might have missed adding the class variables
    vars_insertion = """
    # Local Maintenance Settings
    local_maintenance_enabled: bool = True
    default_local_maintenance_profile: str = "balanced_local_maintenance"
    local_maintenance_default_language: str = "tr"
    local_maintenance_dry_run_default: bool = True
    local_maintenance_allow_production_scheduler: bool = False
    local_maintenance_allow_background_daemon: bool = False
    local_maintenance_allow_auto_upgrade: bool = False
    local_maintenance_allow_auto_fix: bool = False
    local_maintenance_allow_file_modification: bool = False
    local_maintenance_allow_file_deletion: bool = False
    local_maintenance_allow_overwrite: bool = False
    local_maintenance_allow_cloud_upload: bool = False
    local_maintenance_allow_external_service: bool = False
    local_maintenance_allow_external_llm: bool = False
    local_maintenance_allow_live_commands: bool = False
    local_maintenance_allow_broker_commands: bool = False
    local_maintenance_allow_deploy_commands: bool = False
    local_maintenance_allow_real_market_download: bool = False
    local_maintenance_scan_docs: bool = True
    local_maintenance_scan_tests: bool = True
    local_maintenance_scan_scripts: bool = True
    local_maintenance_scan_reports: bool = True
    local_maintenance_scan_data_lake: bool = True
    local_maintenance_scan_configs: bool = True
    local_maintenance_scan_requirements: bool = True
    local_maintenance_scan_cross_layer_outputs: bool = True
    local_maintenance_default_monthly_review_day: int = 1
    local_maintenance_default_quarterly_review_month_interval: int = 3
    local_maintenance_stale_report_days_warning: int = 45
    local_maintenance_stale_doc_days_warning: int = 90
    local_maintenance_stale_test_days_warning: int = 90
    local_maintenance_dependency_age_days_warning: int = 180
    local_maintenance_max_checks: int = 300000
    local_maintenance_min_sustainability_score: float = 0.40
    local_maintenance_min_quality_score: float = 0.40
    local_maintenance_save_reports: bool = True
"""
    if "local_maintenance_enabled: bool" not in content:
        idx = content.find("def __init__")
        if idx != -1:
            content = content[:idx] + vars_insertion + "\n    " + content[idx:]
            with open(file_path, "w") as f:
                f.write(content)

fix_settings()
