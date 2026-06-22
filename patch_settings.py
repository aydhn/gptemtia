import os
import re

def update_settings():
    file_path = "config/settings.py"
    with open(file_path, "r") as f:
        content = f.read()

    # Find where to add settings variables
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
    init_insertion = """
        # Local Maintenance
        self.local_maintenance_enabled = str(os.getenv("LOCAL_MAINTENANCE_ENABLED", str(self.local_maintenance_enabled))).lower() == "true"
        self.default_local_maintenance_profile = str(os.getenv("DEFAULT_LOCAL_MAINTENANCE_PROFILE", self.default_local_maintenance_profile))
        self.local_maintenance_default_language = str(os.getenv("LOCAL_MAINTENANCE_DEFAULT_LANGUAGE", self.local_maintenance_default_language))
        self.local_maintenance_dry_run_default = str(os.getenv("LOCAL_MAINTENANCE_DRY_RUN_DEFAULT", str(self.local_maintenance_dry_run_default))).lower() == "true"
        self.local_maintenance_allow_production_scheduler = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_PRODUCTION_SCHEDULER", str(self.local_maintenance_allow_production_scheduler))).lower() == "true"
        self.local_maintenance_allow_background_daemon = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_BACKGROUND_DAEMON", str(self.local_maintenance_allow_background_daemon))).lower() == "true"
        self.local_maintenance_allow_auto_upgrade = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_AUTO_UPGRADE", str(self.local_maintenance_allow_auto_upgrade))).lower() == "true"
        self.local_maintenance_allow_auto_fix = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_AUTO_FIX", str(self.local_maintenance_allow_auto_fix))).lower() == "true"
        self.local_maintenance_allow_file_modification = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_FILE_MODIFICATION", str(self.local_maintenance_allow_file_modification))).lower() == "true"
        self.local_maintenance_allow_file_deletion = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_FILE_DELETION", str(self.local_maintenance_allow_file_deletion))).lower() == "true"
        self.local_maintenance_allow_overwrite = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_OVERWRITE", str(self.local_maintenance_allow_overwrite))).lower() == "true"
        self.local_maintenance_allow_cloud_upload = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_CLOUD_UPLOAD", str(self.local_maintenance_allow_cloud_upload))).lower() == "true"
        self.local_maintenance_allow_external_service = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_EXTERNAL_SERVICE", str(self.local_maintenance_allow_external_service))).lower() == "true"
        self.local_maintenance_allow_external_llm = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_EXTERNAL_LLM", str(self.local_maintenance_allow_external_llm))).lower() == "true"
        self.local_maintenance_allow_live_commands = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_LIVE_COMMANDS", str(self.local_maintenance_allow_live_commands))).lower() == "true"
        self.local_maintenance_allow_broker_commands = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_BROKER_COMMANDS", str(self.local_maintenance_allow_broker_commands))).lower() == "true"
        self.local_maintenance_allow_deploy_commands = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_DEPLOY_COMMANDS", str(self.local_maintenance_allow_deploy_commands))).lower() == "true"
        self.local_maintenance_allow_real_market_download = str(os.getenv("LOCAL_MAINTENANCE_ALLOW_REAL_MARKET_DOWNLOAD", str(self.local_maintenance_allow_real_market_download))).lower() == "true"
        self.local_maintenance_scan_docs = str(os.getenv("LOCAL_MAINTENANCE_SCAN_DOCS", str(self.local_maintenance_scan_docs))).lower() == "true"
        self.local_maintenance_scan_tests = str(os.getenv("LOCAL_MAINTENANCE_SCAN_TESTS", str(self.local_maintenance_scan_tests))).lower() == "true"
        self.local_maintenance_scan_scripts = str(os.getenv("LOCAL_MAINTENANCE_SCAN_SCRIPTS", str(self.local_maintenance_scan_scripts))).lower() == "true"
        self.local_maintenance_scan_reports = str(os.getenv("LOCAL_MAINTENANCE_SCAN_REPORTS", str(self.local_maintenance_scan_reports))).lower() == "true"
        self.local_maintenance_scan_data_lake = str(os.getenv("LOCAL_MAINTENANCE_SCAN_DATA_LAKE", str(self.local_maintenance_scan_data_lake))).lower() == "true"
        self.local_maintenance_scan_configs = str(os.getenv("LOCAL_MAINTENANCE_SCAN_CONFIGS", str(self.local_maintenance_scan_configs))).lower() == "true"
        self.local_maintenance_scan_requirements = str(os.getenv("LOCAL_MAINTENANCE_SCAN_REQUIREMENTS", str(self.local_maintenance_scan_requirements))).lower() == "true"
        self.local_maintenance_scan_cross_layer_outputs = str(os.getenv("LOCAL_MAINTENANCE_SCAN_CROSS_LAYER_OUTPUTS", str(self.local_maintenance_scan_cross_layer_outputs))).lower() == "true"

        try:
            self.local_maintenance_default_monthly_review_day = int(os.getenv("LOCAL_MAINTENANCE_DEFAULT_MONTHLY_REVIEW_DAY", str(self.local_maintenance_default_monthly_review_day)))
        except ValueError:
            pass

        try:
            self.local_maintenance_default_quarterly_review_month_interval = int(os.getenv("LOCAL_MAINTENANCE_DEFAULT_QUARTERLY_REVIEW_MONTH_INTERVAL", str(self.local_maintenance_default_quarterly_review_month_interval)))
        except ValueError:
            pass

        try:
            self.local_maintenance_stale_report_days_warning = int(os.getenv("LOCAL_MAINTENANCE_STALE_REPORT_DAYS_WARNING", str(self.local_maintenance_stale_report_days_warning)))
        except ValueError:
            pass

        try:
            self.local_maintenance_stale_doc_days_warning = int(os.getenv("LOCAL_MAINTENANCE_STALE_DOC_DAYS_WARNING", str(self.local_maintenance_stale_doc_days_warning)))
        except ValueError:
            pass

        try:
            self.local_maintenance_stale_test_days_warning = int(os.getenv("LOCAL_MAINTENANCE_STALE_TEST_DAYS_WARNING", str(self.local_maintenance_stale_test_days_warning)))
        except ValueError:
            pass

        try:
            self.local_maintenance_dependency_age_days_warning = int(os.getenv("LOCAL_MAINTENANCE_DEPENDENCY_AGE_DAYS_WARNING", str(self.local_maintenance_dependency_age_days_warning)))
        except ValueError:
            pass

        try:
            self.local_maintenance_max_checks = int(os.getenv("LOCAL_MAINTENANCE_MAX_CHECKS", str(self.local_maintenance_max_checks)))
        except ValueError:
            pass

        try:
            self.local_maintenance_min_sustainability_score = float(os.getenv("LOCAL_MAINTENANCE_MIN_SUSTAINABILITY_SCORE", str(self.local_maintenance_min_sustainability_score)))
        except ValueError:
            pass

        try:
            self.local_maintenance_min_quality_score = float(os.getenv("LOCAL_MAINTENANCE_MIN_QUALITY_SCORE", str(self.local_maintenance_min_quality_score)))
        except ValueError:
            pass

        self.local_maintenance_save_reports = str(os.getenv("LOCAL_MAINTENANCE_SAVE_REPORTS", str(self.local_maintenance_save_reports))).lower() == "true"
"""

    if "local_maintenance_enabled" not in content:
        # Add variables to class
        idx1 = content.find("class Settings")
        if idx1 != -1:
            # find next def __init__
            idx2 = content.find("def __init__(", idx1)
            if idx2 != -1:
                content = content[:idx2] + vars_insertion + "\n    " + content[idx2:]

        # Add logic to __init__
        idx3 = content.find("self.live_trading_enabled = False")
        if idx3 != -1:
            content = content[:idx3] + init_insertion + "\n        " + content[idx3:]

        with open(file_path, "w") as f:
            f.write(content)

update_settings()
