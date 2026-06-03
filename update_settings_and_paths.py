import os
import re

# Update settings.py
with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    settings_content = f.read()

settings_injection = """
    # Phase 61: Portable Packaging
    portable_packaging_enabled: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ENABLED", "true")).lower() == "true")
    default_portable_packaging_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_PORTABLE_PACKAGING_PROFILE", "balanced_local_packaging"))
    portable_packaging_default_language: str = field(default_factory=lambda: os.getenv("PORTABLE_PACKAGING_DEFAULT_LANGUAGE", "tr"))
    portable_packaging_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_DRY_RUN_DEFAULT", "true")).lower() == "true")
    portable_packaging_allow_archive_create: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_ARCHIVE_CREATE", "false")).lower() == "true")
    portable_packaging_allow_package_publish: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_PACKAGE_PUBLISH", "false")).lower() == "true")
    portable_packaging_allow_docker: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_DOCKER", "false")).lower() == "true")
    portable_packaging_allow_cloud_deploy: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_CLOUD_DEPLOY", "false")).lower() == "true")
    portable_packaging_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    portable_packaging_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    portable_packaging_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    portable_packaging_include_source: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_SOURCE", "true")).lower() == "true")
    portable_packaging_include_docs: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_DOCS", "true")).lower() == "true")
    portable_packaging_include_tests: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_TESTS", "true")).lower() == "true")
    portable_packaging_include_configs: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_CONFIGS", "true")).lower() == "true")
    portable_packaging_include_reports_manifest_only: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_REPORTS_MANIFEST_ONLY", "true")).lower() == "true")
    portable_packaging_include_data_manifest_only: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_DATA_MANIFEST_ONLY", "true")).lower() == "true")
    portable_packaging_max_inventory_files: int = field(default_factory=lambda: int(os.getenv("PORTABLE_PACKAGING_MAX_INVENTORY_FILES", "100000")))
    portable_packaging_max_manifest_file_mb: int = field(default_factory=lambda: int(os.getenv("PORTABLE_PACKAGING_MAX_MANIFEST_FILE_MB", "50")))
    portable_packaging_save_reports: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_SAVE_REPORTS", "true")).lower() == "true")
    portable_packaging_min_quality_score: float = field(default_factory=lambda: float(os.getenv("PORTABLE_PACKAGING_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):
"""

settings_content = re.sub(r'    def __post_init__\(self\):', settings_injection, settings_content)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(settings_content)

# Update paths.py
with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    paths_content = f.read()


paths_injection = """
        # Phase 61: Portable Packaging
        self.LAKE_PORTABLE_PACKAGING_DIR = LAKE_PORTABLE_PACKAGING_DIR
        self.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR = LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR
        self.LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR = LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR
        self.LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR = LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR
        self.LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR
        self.LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR
        self.LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR
        self.LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR
        self.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR = LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR
        self.LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR = LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR
        self.LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR = LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR
        self.LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR = LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR
        self.LAKE_PORTABLE_PACKAGING_DRIFT_DIR = LAKE_PORTABLE_PACKAGING_DRIFT_DIR
        self.LAKE_PORTABLE_PACKAGING_SAFETY_DIR = LAKE_PORTABLE_PACKAGING_SAFETY_DIR
        self.LAKE_PORTABLE_PACKAGING_QUALITY_DIR = LAKE_PORTABLE_PACKAGING_QUALITY_DIR

        self.REPORTS_PORTABLE_PACKAGING_DIR = REPORTS_PORTABLE_PACKAGING_DIR
        self.REPORTS_PORTABLE_PACKAGING_CSV_DIR = REPORTS_PORTABLE_PACKAGING_CSV_DIR
        self.REPORTS_PORTABLE_PACKAGING_MARKDOWN_DIR = REPORTS_PORTABLE_PACKAGING_MARKDOWN_DIR
        self.REPORTS_PORTABLE_PACKAGING_TXT_DIR = REPORTS_PORTABLE_PACKAGING_TXT_DIR
        self.REPORTS_PORTABLE_PACKAGING_JSON_DIR = REPORTS_PORTABLE_PACKAGING_JSON_DIR

        self.PORTABLE_BUNDLE_DIR = PORTABLE_BUNDLE_DIR
        self.PORTABLE_BUNDLE_MANIFESTS_DIR = PORTABLE_BUNDLE_MANIFESTS_DIR
        self.PORTABLE_BUNDLE_SETUP_DIR = PORTABLE_BUNDLE_SETUP_DIR
        self.PORTABLE_BUNDLE_ARCHIVE_PLANS_DIR = PORTABLE_BUNDLE_ARCHIVE_PLANS_DIR

        self.DOCS_PORTABLE_PACKAGING_DIR = DOCS_PORTABLE_PACKAGING_DIR

"""

paths_content = re.sub(r'# Phase 39: Research Reports', paths_injection + '# Phase 39: Research Reports', paths_content)

paths_constants_injection = """
# Phase 61: Portable Packaging
LAKE_PORTABLE_PACKAGING_DIR = LAKE_DIR / "portable_packaging"
LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR = LAKE_PORTABLE_PACKAGING_DIR / "environment"
LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR = LAKE_PORTABLE_PACKAGING_DIR / "dependencies"
LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR = LAKE_PORTABLE_PACKAGING_DIR / "requirements"
LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_DIR / "install_verification"
LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_DIR / "import_verification"
LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_DIR / "script_verification"
LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR = LAKE_PORTABLE_PACKAGING_DIR / "config_verification"
LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR = LAKE_PORTABLE_PACKAGING_DIR / "bundle_manifest"
LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR = LAKE_PORTABLE_PACKAGING_DIR / "archive_manifest"
LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR = LAKE_PORTABLE_PACKAGING_DIR / "source_policy"
LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR = LAKE_PORTABLE_PACKAGING_DIR / "setup_guides"
LAKE_PORTABLE_PACKAGING_DRIFT_DIR = LAKE_PORTABLE_PACKAGING_DIR / "drift"
LAKE_PORTABLE_PACKAGING_SAFETY_DIR = LAKE_PORTABLE_PACKAGING_DIR / "safety"
LAKE_PORTABLE_PACKAGING_QUALITY_DIR = LAKE_PORTABLE_PACKAGING_DIR / "quality"

REPORTS_PORTABLE_PACKAGING_DIR = REPORTS_DIR / "portable_packaging"
REPORTS_PORTABLE_PACKAGING_CSV_DIR = REPORTS_PORTABLE_PACKAGING_DIR / "csv"
REPORTS_PORTABLE_PACKAGING_MARKDOWN_DIR = REPORTS_PORTABLE_PACKAGING_DIR / "markdown"
REPORTS_PORTABLE_PACKAGING_TXT_DIR = REPORTS_PORTABLE_PACKAGING_DIR / "txt"
REPORTS_PORTABLE_PACKAGING_JSON_DIR = REPORTS_PORTABLE_PACKAGING_DIR / "json"

PORTABLE_BUNDLE_DIR = PROJECT_ROOT / "portable_bundle"
PORTABLE_BUNDLE_MANIFESTS_DIR = PORTABLE_BUNDLE_DIR / "manifests"
PORTABLE_BUNDLE_SETUP_DIR = PORTABLE_BUNDLE_DIR / "setup"
PORTABLE_BUNDLE_ARCHIVE_PLANS_DIR = PORTABLE_BUNDLE_DIR / "archive_plans"

DOCS_PORTABLE_PACKAGING_DIR = PROJECT_ROOT / "docs" / "generated" / "portable_packaging"

"""

paths_content = paths_content + paths_constants_injection

paths_create_injection = """
            self.LAKE_PORTABLE_PACKAGING_DIR,
            self.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR,
            self.LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR,
            self.LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR,
            self.LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR,
            self.LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR,
            self.LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR,
            self.LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR,
            self.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR,
            self.LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR,
            self.LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR,
            self.LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR,
            self.LAKE_PORTABLE_PACKAGING_DRIFT_DIR,
            self.LAKE_PORTABLE_PACKAGING_SAFETY_DIR,
            self.LAKE_PORTABLE_PACKAGING_QUALITY_DIR,

            self.REPORTS_PORTABLE_PACKAGING_DIR,
            self.REPORTS_PORTABLE_PACKAGING_CSV_DIR,
            self.REPORTS_PORTABLE_PACKAGING_MARKDOWN_DIR,
            self.REPORTS_PORTABLE_PACKAGING_TXT_DIR,
            self.REPORTS_PORTABLE_PACKAGING_JSON_DIR,

            self.PORTABLE_BUNDLE_DIR,
            self.PORTABLE_BUNDLE_MANIFESTS_DIR,
            self.PORTABLE_BUNDLE_SETUP_DIR,
            self.PORTABLE_BUNDLE_ARCHIVE_PLANS_DIR,

            self.DOCS_PORTABLE_PACKAGING_DIR,
"""

paths_content = re.sub(r'            self.DOCS_ANALYST_UX_DIR,', '            self.DOCS_ANALYST_UX_DIR,' + paths_create_injection, paths_content)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(paths_content)

# Update .env.example
with open("commodity_fx_signal_bot/.env.example", "a") as f:
    f.write("""
# Portable Packaging
PORTABLE_PACKAGING_ENABLED=true
DEFAULT_PORTABLE_PACKAGING_PROFILE=balanced_local_packaging
PORTABLE_PACKAGING_DEFAULT_LANGUAGE=tr
PORTABLE_PACKAGING_DRY_RUN_DEFAULT=true
PORTABLE_PACKAGING_ALLOW_ARCHIVE_CREATE=false
PORTABLE_PACKAGING_ALLOW_PACKAGE_PUBLISH=false
PORTABLE_PACKAGING_ALLOW_DOCKER=false
PORTABLE_PACKAGING_ALLOW_CLOUD_DEPLOY=false
PORTABLE_PACKAGING_ALLOW_LIVE_COMMANDS=false
PORTABLE_PACKAGING_ALLOW_BROKER_COMMANDS=false
PORTABLE_PACKAGING_ALLOW_DEPLOY_COMMANDS=false
PORTABLE_PACKAGING_ALLOW_BACKGROUND_DAEMONS=false
PORTABLE_PACKAGING_ALLOW_REAL_MARKET_DOWNLOAD=false
PORTABLE_PACKAGING_ALLOW_EXTERNAL_LLM=false
PORTABLE_PACKAGING_INCLUDE_SOURCE=true
PORTABLE_PACKAGING_INCLUDE_DOCS=true
PORTABLE_PACKAGING_INCLUDE_TESTS=true
PORTABLE_PACKAGING_INCLUDE_CONFIGS=true
PORTABLE_PACKAGING_INCLUDE_REPORTS_MANIFEST_ONLY=true
PORTABLE_PACKAGING_INCLUDE_DATA_MANIFEST_ONLY=true
PORTABLE_PACKAGING_MAX_INVENTORY_FILES=100000
PORTABLE_PACKAGING_MAX_MANIFEST_FILE_MB=50
PORTABLE_PACKAGING_SAVE_REPORTS=true
PORTABLE_PACKAGING_MIN_QUALITY_SCORE=0.40
""")

