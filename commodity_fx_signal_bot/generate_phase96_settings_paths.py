import os
from pathlib import Path
import re

def patch_settings():
    settings_path = Path("config/settings.py")
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Settings code to inject
    settings_injection = """
    # Phase 96: Local Distribution Packaging Settings
    local_distribution_packaging_enabled: bool = True
    default_local_distribution_packaging_profile: str = "balanced_local_distribution_packaging"
    local_distribution_packaging_default_language: str = "tr"
    local_distribution_packaging_dry_run_default: bool = True
    local_distribution_packaging_allow_real_archive_creation: bool = False
    local_distribution_packaging_allow_zip_creation: bool = False
    local_distribution_packaging_allow_tar_creation: bool = False
    local_distribution_packaging_allow_binary_artifact: bool = False
    local_distribution_packaging_allow_installer_creation: bool = False
    local_distribution_packaging_allow_executable_packaging: bool = False
    local_distribution_packaging_allow_package_publish: bool = False
    local_distribution_packaging_allow_docker_build_push: bool = False
    local_distribution_packaging_allow_git_tag: bool = False
    local_distribution_packaging_allow_cloud_upload: bool = False
    local_distribution_packaging_allow_deployment: bool = False
    local_distribution_packaging_allow_official_release: bool = False
    local_distribution_packaging_allow_official_handover: bool = False
    local_distribution_packaging_allow_legal_signoff: bool = False
    local_distribution_packaging_allow_compliance_approval: bool = False
    local_distribution_packaging_allow_production_approval_claim: bool = False
    local_distribution_packaging_allow_official_acceptance_claim: bool = False
    local_distribution_packaging_allow_broker_readiness_claim: bool = False
    local_distribution_packaging_allow_live_trading_claim: bool = False
    local_distribution_packaging_allow_investment_advice: bool = False
    local_distribution_packaging_allow_model_deployment_claim: bool = False
    local_distribution_packaging_allow_web_server: bool = False
    local_distribution_packaging_allow_dashboard_creation: bool = False
    local_distribution_packaging_allow_gui_creation: bool = False
    local_distribution_packaging_allow_tui_creation: bool = False
    local_distribution_packaging_allow_telemetry: bool = False
    local_distribution_packaging_allow_external_service: bool = False
    local_distribution_packaging_allow_external_llm: bool = False
    local_distribution_packaging_allow_vector_db: bool = False
    local_distribution_packaging_allow_embedding_api: bool = False
    local_distribution_packaging_allow_file_modification: bool = False
    local_distribution_packaging_allow_file_deletion: bool = False
    local_distribution_packaging_allow_file_move: bool = False
    local_distribution_packaging_allow_overwrite: bool = False
    local_distribution_packaging_scan_docs: bool = True
    local_distribution_packaging_scan_reports: bool = True
    local_distribution_packaging_scan_data_lake: bool = True
    local_distribution_packaging_scan_scripts: bool = True
    local_distribution_packaging_scan_tests: bool = True
    local_distribution_packaging_scan_generated_docs: bool = True
    local_distribution_packaging_scan_documentation_export_outputs: bool = True
    local_distribution_packaging_scan_review_outputs: bool = True
    local_distribution_packaging_scan_atlas_outputs: bool = True
    local_distribution_packaging_scan_continuity_outputs: bool = True
    local_distribution_packaging_scan_preservation_outputs: bool = True
    local_distribution_packaging_scan_completion_outputs: bool = True
    local_distribution_packaging_scan_safety_outputs: bool = True
    local_distribution_packaging_max_items: int = 750000
    local_distribution_packaging_max_rows: int = 300000
    local_distribution_packaging_min_readiness_score: float = 0.40
    local_distribution_packaging_min_quality_score: float = 0.40
    local_distribution_packaging_save_reports: bool = True
"""

    if "local_distribution_packaging_enabled: bool = True" not in content:
        # Find where to inject in Settings class
        # typically right before the end of the class, or we can just find 'class Settings' and put it at the top
        class_idx = content.find("class Settings(BaseSettings):")
        if class_idx != -1:
            end_of_class_line = content.find(":", class_idx)
            # Find the next non-empty line
            newline_idx = content.find("\\n", end_of_class_line)
            # insert after class docstring or something similar
            # easier to append before the first method (like `model_config`)
            inject_idx = content.find("model_config = SettingsConfigDict", class_idx)
            if inject_idx != -1:
                content = content[:inject_idx] + settings_injection + "\n    " + content[inject_idx:]
            else:
                print("Could not find model_config in Settings")
        
        with open(settings_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Patched config/settings.py")
    else:
        print("config/settings.py already patched")

def patch_env():
    env_path = Path(".env.example")
    with open(env_path, "r", encoding="utf-8") as f:
        content = f.read()

    env_injection = """
# Phase 96: Local Distribution Packaging Settings
LOCAL_DISTRIBUTION_PACKAGING_ENABLED=true
DEFAULT_LOCAL_DISTRIBUTION_PACKAGING_PROFILE=balanced_local_distribution_packaging
LOCAL_DISTRIBUTION_PACKAGING_DEFAULT_LANGUAGE=tr
LOCAL_DISTRIBUTION_PACKAGING_DRY_RUN_DEFAULT=true
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_REAL_ARCHIVE_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_ZIP_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_TAR_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_BINARY_ARTIFACT=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_INSTALLER_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_EXECUTABLE_PACKAGING=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_PACKAGE_PUBLISH=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_DOCKER_BUILD_PUSH=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_GIT_TAG=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_CLOUD_UPLOAD=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_DEPLOYMENT=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_OFFICIAL_RELEASE=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_OFFICIAL_HANDOVER=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_LEGAL_SIGNOFF=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_COMPLIANCE_APPROVAL=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_PRODUCTION_APPROVAL_CLAIM=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_OFFICIAL_ACCEPTANCE_CLAIM=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_INVESTMENT_ADVICE=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_WEB_SERVER=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_DASHBOARD_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_GUI_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_TUI_CREATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_TELEMETRY=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_EXTERNAL_SERVICE=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_EXTERNAL_LLM=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_VECTOR_DB=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_EMBEDDING_API=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_FILE_MODIFICATION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_FILE_DELETION=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_FILE_MOVE=false
LOCAL_DISTRIBUTION_PACKAGING_ALLOW_OVERWRITE=false
LOCAL_DISTRIBUTION_PACKAGING_SCAN_DOCS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_REPORTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_DATA_LAKE=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_SCRIPTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_TESTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_GENERATED_DOCS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_DOCUMENTATION_EXPORT_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_REVIEW_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_ATLAS_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_CONTINUITY_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_PRESERVATION_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_COMPLETION_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_SCAN_SAFETY_OUTPUTS=true
LOCAL_DISTRIBUTION_PACKAGING_MAX_ITEMS=750000
LOCAL_DISTRIBUTION_PACKAGING_MAX_ROWS=300000
LOCAL_DISTRIBUTION_PACKAGING_MIN_READINESS_SCORE=0.40
LOCAL_DISTRIBUTION_PACKAGING_MIN_QUALITY_SCORE=0.40
LOCAL_DISTRIBUTION_PACKAGING_SAVE_REPORTS=true
"""

    if "LOCAL_DISTRIBUTION_PACKAGING_ENABLED=true" not in content:
        with open(env_path, "a", encoding="utf-8") as f:
            f.write("\\n" + env_injection)
        print("Patched .env.example")
    else:
        print(".env.example already patched")

def patch_paths():
    paths_path = Path("config/paths.py")
    with open(paths_path, "r", encoding="utf-8") as f:
        content = f.read()

    paths_props = """
    # Phase 96: Local Distribution Packaging Outputs
    @property
    def local_distribution_packaging_dir(self) -> Path:
        return self.data_lake_dir / "local_distribution_packaging"

    @property
    def local_distribution_packaging_profiles_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "profiles"

    @property
    def local_distribution_packaging_domains_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "domains"

    @property
    def local_distribution_packaging_distribution_bundle_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "distribution_bundle"

    @property
    def local_distribution_packaging_portable_docs_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "portable_docs"

    @property
    def local_distribution_packaging_release_folder_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "release_folder"

    @property
    def local_distribution_packaging_zip_map_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "zip_map"

    @property
    def local_distribution_packaging_governance_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "packaging_governance"

    @property
    def local_distribution_packaging_criteria_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "criteria"

    @property
    def local_distribution_packaging_evidence_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "evidence"

    @property
    def local_distribution_packaging_issues_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "issues"

    @property
    def local_distribution_packaging_handoff_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "handoff"

    @property
    def local_distribution_packaging_source_maps_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "source_maps"

    @property
    def local_distribution_packaging_output_maps_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "output_maps"

    @property
    def local_distribution_packaging_command_maps_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "command_maps"

    @property
    def local_distribution_packaging_no_go_safe_go_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "no_go_safe_go"

    @property
    def local_distribution_packaging_exceptions_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "exceptions"

    @property
    def local_distribution_packaging_gaps_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "gaps"

    @property
    def local_distribution_packaging_risks_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "risks"

    @property
    def local_distribution_packaging_scoring_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "scoring"

    @property
    def local_distribution_packaging_validation_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "validation"

    @property
    def local_distribution_packaging_quality_dir(self) -> Path:
        return self.local_distribution_packaging_dir / "quality"

    @property
    def reports_local_distribution_packaging_dir(self) -> Path:
        return self.reports_output_dir / "local_distribution_packaging"

    @property
    def reports_local_distribution_packaging_csv_dir(self) -> Path:
        return self.reports_local_distribution_packaging_dir / "csv"

    @property
    def reports_local_distribution_packaging_markdown_dir(self) -> Path:
        return self.reports_local_distribution_packaging_dir / "markdown"

    @property
    def reports_local_distribution_packaging_txt_dir(self) -> Path:
        return self.reports_local_distribution_packaging_dir / "txt"

    @property
    def reports_local_distribution_packaging_json_dir(self) -> Path:
        return self.reports_local_distribution_packaging_dir / "json"

    @property
    def docs_generated_local_distribution_packaging_dir(self) -> Path:
        return self.docs_generated_dir / "local_distribution_packaging"

    @property
    def docs_generated_local_distribution_packaging_portable_docs_dir(self) -> Path:
        return self.docs_generated_local_distribution_packaging_dir / "portable_docs"

    @property
    def docs_generated_local_distribution_packaging_release_folder_dir(self) -> Path:
        return self.docs_generated_local_distribution_packaging_dir / "release_folder"

    @property
    def docs_generated_local_distribution_packaging_zip_map_dir(self) -> Path:
        return self.docs_generated_local_distribution_packaging_dir / "zip_map"

    @property
    def docs_generated_local_distribution_packaging_governance_dir(self) -> Path:
        return self.docs_generated_local_distribution_packaging_dir / "packaging_governance"
"""

    paths_dirs = """
        # Phase 96: Local Distribution Packaging Outputs
        self.local_distribution_packaging_dir,
        self.local_distribution_packaging_profiles_dir,
        self.local_distribution_packaging_domains_dir,
        self.local_distribution_packaging_distribution_bundle_dir,
        self.local_distribution_packaging_portable_docs_dir,
        self.local_distribution_packaging_release_folder_dir,
        self.local_distribution_packaging_zip_map_dir,
        self.local_distribution_packaging_governance_dir,
        self.local_distribution_packaging_criteria_dir,
        self.local_distribution_packaging_evidence_dir,
        self.local_distribution_packaging_issues_dir,
        self.local_distribution_packaging_handoff_dir,
        self.local_distribution_packaging_source_maps_dir,
        self.local_distribution_packaging_output_maps_dir,
        self.local_distribution_packaging_command_maps_dir,
        self.local_distribution_packaging_no_go_safe_go_dir,
        self.local_distribution_packaging_exceptions_dir,
        self.local_distribution_packaging_gaps_dir,
        self.local_distribution_packaging_risks_dir,
        self.local_distribution_packaging_scoring_dir,
        self.local_distribution_packaging_validation_dir,
        self.local_distribution_packaging_quality_dir,
        self.reports_local_distribution_packaging_dir,
        self.reports_local_distribution_packaging_csv_dir,
        self.reports_local_distribution_packaging_markdown_dir,
        self.reports_local_distribution_packaging_txt_dir,
        self.reports_local_distribution_packaging_json_dir,
        self.docs_generated_local_distribution_packaging_dir,
        self.docs_generated_local_distribution_packaging_portable_docs_dir,
        self.docs_generated_local_distribution_packaging_release_folder_dir,
        self.docs_generated_local_distribution_packaging_zip_map_dir,
        self.docs_generated_local_distribution_packaging_governance_dir,
"""

    if "def local_distribution_packaging_dir" not in content:
        # Inject properties
        inject_idx = content.find("def ensure_project_directories")
        if inject_idx != -1:
            content = content[:inject_idx] + paths_props + "\n    " + content[inject_idx:]
        
        # Inject to ensure_project_directories
        dirs_list_idx = content.find("dirs_to_create = [")
        if dirs_list_idx != -1:
            bracket_idx = content.find("]", dirs_list_idx)
            content = content[:bracket_idx] + paths_dirs + content[bracket_idx:]
        
        with open(paths_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Patched config/paths.py")
    else:
        print("config/paths.py already patched")

if __name__ == "__main__":
    patch_settings()
    patch_env()
    patch_paths()
