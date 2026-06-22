def fix_settings():
    file_path = "config/settings.py"
    with open(file_path, "r") as f:
        lines = f.readlines()

    out_lines = []
    in_class = False
    added = False

    vars_insertion = [
        "    # Local Maintenance Settings\n",
        "    local_maintenance_enabled: bool = True\n",
        "    default_local_maintenance_profile: str = \"balanced_local_maintenance\"\n",
        "    local_maintenance_default_language: str = \"tr\"\n",
        "    local_maintenance_dry_run_default: bool = True\n",
        "    local_maintenance_allow_production_scheduler: bool = False\n",
        "    local_maintenance_allow_background_daemon: bool = False\n",
        "    local_maintenance_allow_auto_upgrade: bool = False\n",
        "    local_maintenance_allow_auto_fix: bool = False\n",
        "    local_maintenance_allow_file_modification: bool = False\n",
        "    local_maintenance_allow_file_deletion: bool = False\n",
        "    local_maintenance_allow_overwrite: bool = False\n",
        "    local_maintenance_allow_cloud_upload: bool = False\n",
        "    local_maintenance_allow_external_service: bool = False\n",
        "    local_maintenance_allow_external_llm: bool = False\n",
        "    local_maintenance_allow_live_commands: bool = False\n",
        "    local_maintenance_allow_broker_commands: bool = False\n",
        "    local_maintenance_allow_deploy_commands: bool = False\n",
        "    local_maintenance_allow_real_market_download: bool = False\n",
        "    local_maintenance_scan_docs: bool = True\n",
        "    local_maintenance_scan_tests: bool = True\n",
        "    local_maintenance_scan_scripts: bool = True\n",
        "    local_maintenance_scan_reports: bool = True\n",
        "    local_maintenance_scan_data_lake: bool = True\n",
        "    local_maintenance_scan_configs: bool = True\n",
        "    local_maintenance_scan_requirements: bool = True\n",
        "    local_maintenance_scan_cross_layer_outputs: bool = True\n",
        "    local_maintenance_default_monthly_review_day: int = 1\n",
        "    local_maintenance_default_quarterly_review_month_interval: int = 3\n",
        "    local_maintenance_stale_report_days_warning: int = 45\n",
        "    local_maintenance_stale_doc_days_warning: int = 90\n",
        "    local_maintenance_stale_test_days_warning: int = 90\n",
        "    local_maintenance_dependency_age_days_warning: int = 180\n",
        "    local_maintenance_max_checks: int = 300000\n",
        "    local_maintenance_min_sustainability_score: float = 0.40\n",
        "    local_maintenance_min_quality_score: float = 0.40\n",
        "    local_maintenance_save_reports: bool = True\n"
    ]

    for line in lines:
        if line.startswith("class Settings"):
            in_class = True
            out_lines.append(line)
            continue

        if in_class and not added and "def __init__" in line:
            out_lines.extend(vars_insertion)
            added = True

        out_lines.append(line)

    with open(file_path, "w") as f:
        f.writelines(out_lines)

fix_settings()
