import re
import os

with open("config/settings.py", "r", encoding="utf-8") as f:
    content = f.read()

fields = '''
    # Local Training Settings
    local_training_enabled: bool = True
    default_local_training_profile: str = "balanced_local_training"
    local_training_default_language: str = "tr"
    local_training_dry_run_default: bool = True
    local_training_allow_cloud_upload: bool = False
    local_training_allow_external_training_service: bool = False
    local_training_allow_external_llm: bool = False
    local_training_allow_file_modification: bool = False
    local_training_allow_file_deletion: bool = False
    local_training_allow_file_move: bool = False
    local_training_allow_overwrite: bool = False
    local_training_allow_live_commands: bool = False
    local_training_allow_broker_commands: bool = False
    local_training_allow_deploy_commands: bool = False
    local_training_allow_background_daemons: bool = False
    local_training_allow_real_market_download: bool = False
    local_training_allow_certification_claim: bool = False
    local_training_allow_investment_advice_training: bool = False
    local_training_scan_docs: bool = True
    local_training_scan_reports: bool = True
    local_training_scan_scripts: bool = True
    local_training_scan_tests: bool = True
    local_training_scan_data_lake: bool = True
    local_training_scan_cross_layer_outputs: bool = True
    local_training_scan_safety_docs: bool = True
    local_training_max_lessons: int = 10000
    local_training_max_walkthrough_steps: int = 5000
    local_training_min_training_quality_score: float = 0.40
    local_training_save_reports: bool = True
'''

init_code = '''
        self.local_training_enabled = str(os.getenv("LOCAL_TRAINING_ENABLED", str(self.local_training_enabled))).lower() == "true"
        self.default_local_training_profile = str(os.getenv("DEFAULT_LOCAL_TRAINING_PROFILE", self.default_local_training_profile))
        self.local_training_default_language = str(os.getenv("LOCAL_TRAINING_DEFAULT_LANGUAGE", self.local_training_default_language))
        self.local_training_dry_run_default = str(os.getenv("LOCAL_TRAINING_DRY_RUN_DEFAULT", str(self.local_training_dry_run_default))).lower() == "true"
        self.local_training_allow_cloud_upload = str(os.getenv("LOCAL_TRAINING_ALLOW_CLOUD_UPLOAD", str(self.local_training_allow_cloud_upload))).lower() == "true"
        self.local_training_allow_external_training_service = str(os.getenv("LOCAL_TRAINING_ALLOW_EXTERNAL_TRAINING_SERVICE", str(self.local_training_allow_external_training_service))).lower() == "true"
        self.local_training_allow_external_llm = str(os.getenv("LOCAL_TRAINING_ALLOW_EXTERNAL_LLM", str(self.local_training_allow_external_llm))).lower() == "true"
        self.local_training_allow_file_modification = str(os.getenv("LOCAL_TRAINING_ALLOW_FILE_MODIFICATION", str(self.local_training_allow_file_modification))).lower() == "true"
        self.local_training_allow_file_deletion = str(os.getenv("LOCAL_TRAINING_ALLOW_FILE_DELETION", str(self.local_training_allow_file_deletion))).lower() == "true"
        self.local_training_allow_file_move = str(os.getenv("LOCAL_TRAINING_ALLOW_FILE_MOVE", str(self.local_training_allow_file_move))).lower() == "true"
        self.local_training_allow_overwrite = str(os.getenv("LOCAL_TRAINING_ALLOW_OVERWRITE", str(self.local_training_allow_overwrite))).lower() == "true"
        self.local_training_allow_live_commands = str(os.getenv("LOCAL_TRAINING_ALLOW_LIVE_COMMANDS", str(self.local_training_allow_live_commands))).lower() == "true"
        self.local_training_allow_broker_commands = str(os.getenv("LOCAL_TRAINING_ALLOW_BROKER_COMMANDS", str(self.local_training_allow_broker_commands))).lower() == "true"
        self.local_training_allow_deploy_commands = str(os.getenv("LOCAL_TRAINING_ALLOW_DEPLOY_COMMANDS", str(self.local_training_allow_deploy_commands))).lower() == "true"
        self.local_training_allow_background_daemons = str(os.getenv("LOCAL_TRAINING_ALLOW_BACKGROUND_DAEMONS", str(self.local_training_allow_background_daemons))).lower() == "true"
        self.local_training_allow_real_market_download = str(os.getenv("LOCAL_TRAINING_ALLOW_REAL_MARKET_DOWNLOAD", str(self.local_training_allow_real_market_download))).lower() == "true"
        self.local_training_allow_certification_claim = str(os.getenv("LOCAL_TRAINING_ALLOW_CERTIFICATION_CLAIM", str(self.local_training_allow_certification_claim))).lower() == "true"
        self.local_training_allow_investment_advice_training = str(os.getenv("LOCAL_TRAINING_ALLOW_INVESTMENT_ADVICE_TRAINING", str(self.local_training_allow_investment_advice_training))).lower() == "true"
        self.local_training_scan_docs = str(os.getenv("LOCAL_TRAINING_SCAN_DOCS", str(self.local_training_scan_docs))).lower() == "true"
        self.local_training_scan_reports = str(os.getenv("LOCAL_TRAINING_SCAN_REPORTS", str(self.local_training_scan_reports))).lower() == "true"
        self.local_training_scan_scripts = str(os.getenv("LOCAL_TRAINING_SCAN_SCRIPTS", str(self.local_training_scan_scripts))).lower() == "true"
        self.local_training_scan_tests = str(os.getenv("LOCAL_TRAINING_SCAN_TESTS", str(self.local_training_scan_tests))).lower() == "true"
        self.local_training_scan_data_lake = str(os.getenv("LOCAL_TRAINING_SCAN_DATA_LAKE", str(self.local_training_scan_data_lake))).lower() == "true"
        self.local_training_scan_cross_layer_outputs = str(os.getenv("LOCAL_TRAINING_SCAN_CROSS_LAYER_OUTPUTS", str(self.local_training_scan_cross_layer_outputs))).lower() == "true"
        self.local_training_scan_safety_docs = str(os.getenv("LOCAL_TRAINING_SCAN_SAFETY_DOCS", str(self.local_training_scan_safety_docs))).lower() == "true"

        try:
            self.local_training_max_lessons = int(os.getenv("LOCAL_TRAINING_MAX_LESSONS", str(self.local_training_max_lessons)))
        except ValueError:
            pass

        try:
            self.local_training_max_walkthrough_steps = int(os.getenv("LOCAL_TRAINING_MAX_WALKTHROUGH_STEPS", str(self.local_training_max_walkthrough_steps)))
        except ValueError:
            pass

        try:
            self.local_training_min_training_quality_score = float(os.getenv("LOCAL_TRAINING_MIN_TRAINING_QUALITY_SCORE", str(self.local_training_min_training_quality_score)))
        except ValueError:
            pass

        self.local_training_save_reports = str(os.getenv("LOCAL_TRAINING_SAVE_REPORTS", str(self.local_training_save_reports))).lower() == "true"
'''

content = content.replace("class Settings:\n", "class Settings:\n" + fields + "\n")
content = content.replace("        self.live_trading_enabled = False", init_code + "\n        self.live_trading_enabled = False")

with open("config/settings.py", "w", encoding="utf-8") as f:
    f.write(content)
