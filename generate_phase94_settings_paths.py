import os
import re

def patch_settings():
    settings_path = "config/settings.py"
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "local_review_governance_enabled" not in content:
        insert_code = """
    # Local Review Governance (Phase 94)
    local_review_governance_enabled: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_ENABLED")
    default_local_review_governance_profile: str = Field(default="balanced_local_review_governance", env="DEFAULT_LOCAL_REVIEW_GOVERNANCE_PROFILE")
    local_review_governance_default_language: str = Field(default="tr", env="LOCAL_REVIEW_GOVERNANCE_DEFAULT_LANGUAGE")
    local_review_governance_dry_run_default: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_DRY_RUN_DEFAULT")
    local_review_governance_allow_real_approval_workflow: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_REAL_APPROVAL_WORKFLOW")
    local_review_governance_allow_e_signature: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_E_SIGNATURE")
    local_review_governance_allow_official_expert_signoff: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_OFFICIAL_EXPERT_SIGNOFF")
    local_review_governance_allow_legal_signoff: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_LEGAL_SIGNOFF")
    local_review_governance_allow_compliance_approval: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_COMPLIANCE_APPROVAL")
    local_review_governance_allow_production_approval_claim: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_PRODUCTION_APPROVAL_CLAIM")
    local_review_governance_allow_official_acceptance_claim: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_OFFICIAL_ACCEPTANCE_CLAIM")
    local_review_governance_allow_broker_readiness_claim: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_BROKER_READINESS_CLAIM")
    local_review_governance_allow_live_trading_claim: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_LIVE_TRADING_CLAIM")
    local_review_governance_allow_investment_advice: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_INVESTMENT_ADVICE")
    local_review_governance_allow_package_publish: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_PACKAGE_PUBLISH")
    local_review_governance_allow_docker_build_push: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_DOCKER_BUILD_PUSH")
    local_review_governance_allow_git_tag: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_GIT_TAG")
    local_review_governance_allow_cloud_upload: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_CLOUD_UPLOAD")
    local_review_governance_allow_deployment: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_DEPLOYMENT")
    local_review_governance_allow_model_deployment_claim: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_MODEL_DEPLOYMENT_CLAIM")
    local_review_governance_allow_telemetry: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_TELEMETRY")
    local_review_governance_allow_dashboard_creation: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_DASHBOARD_CREATION")
    local_review_governance_allow_gui_creation: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_GUI_CREATION")
    local_review_governance_allow_tui_creation: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_TUI_CREATION")
    local_review_governance_allow_cloud_review_service: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_CLOUD_REVIEW_SERVICE")
    local_review_governance_allow_external_service: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_EXTERNAL_SERVICE")
    local_review_governance_allow_external_llm: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_EXTERNAL_LLM")
    local_review_governance_allow_vector_db: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_VECTOR_DB")
    local_review_governance_allow_embedding_api: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_EMBEDDING_API")
    local_review_governance_allow_file_modification: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_FILE_MODIFICATION")
    local_review_governance_allow_file_deletion: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_FILE_DELETION")
    local_review_governance_allow_file_move: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_FILE_MOVE")
    local_review_governance_allow_overwrite: bool = Field(default=False, env="LOCAL_REVIEW_GOVERNANCE_ALLOW_OVERWRITE")
    local_review_governance_scan_docs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_DOCS")
    local_review_governance_scan_reports: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_REPORTS")
    local_review_governance_scan_data_lake: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_DATA_LAKE")
    local_review_governance_scan_scripts: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_SCRIPTS")
    local_review_governance_scan_tests: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_TESTS")
    local_review_governance_scan_generated_docs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_GENERATED_DOCS")
    local_review_governance_scan_atlas_outputs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_ATLAS_OUTPUTS")
    local_review_governance_scan_continuity_outputs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_CONTINUITY_OUTPUTS")
    local_review_governance_scan_preservation_outputs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_PRESERVATION_OUTPUTS")
    local_review_governance_scan_completion_outputs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_COMPLETION_OUTPUTS")
    local_review_governance_scan_safety_outputs: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SCAN_SAFETY_OUTPUTS")
    local_review_governance_max_items: int = Field(default=750000, env="LOCAL_REVIEW_GOVERNANCE_MAX_ITEMS")
    local_review_governance_max_rows: int = Field(default=300000, env="LOCAL_REVIEW_GOVERNANCE_MAX_ROWS")
    local_review_governance_min_readiness_score: float = Field(default=0.40, env="LOCAL_REVIEW_GOVERNANCE_MIN_READINESS_SCORE")
    local_review_governance_min_quality_score: float = Field(default=0.40, env="LOCAL_REVIEW_GOVERNANCE_MIN_QUALITY_SCORE")
    local_review_governance_save_reports: bool = Field(default=True, env="LOCAL_REVIEW_GOVERNANCE_SAVE_REPORTS")
"""
        # Find class Settings
        class_idx = content.find("class Settings")
        if class_idx != -1:
            # Find the next class or end of class Settings
            # We'll just append it before the Config class if it exists
            config_idx = content.find("class Config:", class_idx)
            if config_idx != -1:
                content = content[:config_idx] + insert_code + "\n    " + content[config_idx:]
            else:
                # append to the end of the file
                content += insert_code
            
            with open(settings_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Patched settings.py")
        else:
            print("Could not find class Settings in settings.py")

def patch_env():
    env_path = ".env.example"
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "LOCAL_REVIEW_GOVERNANCE_ENABLED" not in content:
            insert_code = """
# Local Review Governance (Phase 94)
LOCAL_REVIEW_GOVERNANCE_ENABLED=true
DEFAULT_LOCAL_REVIEW_GOVERNANCE_PROFILE=balanced_local_review_governance
LOCAL_REVIEW_GOVERNANCE_DEFAULT_LANGUAGE=tr
LOCAL_REVIEW_GOVERNANCE_DRY_RUN_DEFAULT=true
LOCAL_REVIEW_GOVERNANCE_ALLOW_REAL_APPROVAL_WORKFLOW=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_E_SIGNATURE=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_OFFICIAL_EXPERT_SIGNOFF=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_LEGAL_SIGNOFF=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_COMPLIANCE_APPROVAL=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_PRODUCTION_APPROVAL_CLAIM=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_OFFICIAL_ACCEPTANCE_CLAIM=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_DOCKER_BUILD_PUSH=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_GIT_TAG=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_CLOUD_UPLOAD=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_DEPLOYMENT=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_TELEMETRY=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_DASHBOARD_CREATION=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_GUI_CREATION=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_TUI_CREATION=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_CLOUD_REVIEW_SERVICE=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_EXTERNAL_LLM=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_VECTOR_DB=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_EMBEDDING_API=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_FILE_MODIFICATION=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_FILE_DELETION=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_FILE_MOVE=false
LOCAL_REVIEW_GOVERNANCE_ALLOW_OVERWRITE=false
LOCAL_REVIEW_GOVERNANCE_SCAN_DOCS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_REPORTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_DATA_LAKE=true
LOCAL_REVIEW_GOVERNANCE_SCAN_SCRIPTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_TESTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_GENERATED_DOCS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_ATLAS_OUTPUTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_CONTINUITY_OUTPUTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_PRESERVATION_OUTPUTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_COMPLETION_OUTPUTS=true
LOCAL_REVIEW_GOVERNANCE_SCAN_SAFETY_OUTPUTS=true
LOCAL_REVIEW_GOVERNANCE_MAX_ITEMS=750000
LOCAL_REVIEW_GOVERNANCE_MAX_ROWS=300000
LOCAL_REVIEW_GOVERNANCE_MIN_READINESS_SCORE=0.40
LOCAL_REVIEW_GOVERNANCE_MIN_QUALITY_SCORE=0.40
LOCAL_REVIEW_GOVERNANCE_SAVE_REPORTS=true
"""
            with open(env_path, "a", encoding="utf-8") as f:
                f.write(insert_code)
            print("Patched .env.example")

def patch_paths():
    paths_file = "config/paths.py"
    with open(paths_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "local_review_governance" not in content:
        insert_code = """
    # Local Review Governance (Phase 94)
    "data/lake/local_review_governance",
    "data/lake/local_review_governance/profiles",
    "data/lake/local_review_governance/domains",
    "data/lake/local_review_governance/cockpit",
    "data/lake/local_review_governance/approval_ledger",
    "data/lake/local_review_governance/boundaries",
    "data/lake/local_review_governance/expert_review",
    "data/lake/local_review_governance/reviewer_console",
    "data/lake/local_review_governance/governance_binder",
    "data/lake/local_review_governance/criteria",
    "data/lake/local_review_governance/evidence",
    "data/lake/local_review_governance/issues",
    "data/lake/local_review_governance/escalation",
    "data/lake/local_review_governance/non_goals",
    "data/lake/local_review_governance/no_go_safe_go",
    "data/lake/local_review_governance/exceptions",
    "data/lake/local_review_governance/gaps",
    "data/lake/local_review_governance/risks",
    "data/lake/local_review_governance/scoring",
    "data/lake/local_review_governance/validation",
    "data/lake/local_review_governance/quality",
    "reports/output/local_review_governance",
    "reports/output/local_review_governance/csv",
    "reports/output/local_review_governance/markdown",
    "reports/output/local_review_governance/txt",
    "reports/output/local_review_governance/json",
    "docs/generated/local_review_governance",
"""
        # Find where the PROJECT_DIRECTORIES list is
        match = re.search(r"PROJECT_DIRECTORIES\s*=\s*\[", content)
        if match:
            idx = match.end()
            content = content[:idx] + insert_code + content[idx:]
            with open(paths_file, "w", encoding="utf-8") as f:
                f.write(content)
            print("Patched paths.py")

def patch_readme():
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "Local Human-Review Cockpit and Review Governance" not in content:
            insert_code = """
## Local Human-Review Cockpit and Review Governance

Bu proje, Phase 94 kapsamında **Local Human-Review Cockpit and Review Governance** katmanını içerir.
ÖNEMLİ UYARI:
- Final local human-review cockpit web dashboard/GUI/TUI değildir.
- Manual approval ledger gerçek approval workflow değildir.
- Expert review workbook official expert sign-off değildir.
- Offline reviewer console yalnızca offline rapor paketidir.
- Terminal review governance binder legal/compliance approval değildir.
- Review readiness score production approval değildir.
- E-signature, package publish, Docker push, Git tag, cloud upload, deployment, live trading, broker execution ve yatırım tavsiyesi yoktur.
- Tüm çıktılar local ve offline olarak `data/lake/local_review_governance` ve `reports/output/local_review_governance` altında oluşturulur.

Komutlar:
```bash
python -m scripts.run_review_domain_registry
python -m scripts.run_human_review_cockpit
python -m scripts.run_manual_approval_ledger
python -m scripts.run_expert_review_workbook
python -m scripts.run_offline_reviewer_console
python -m scripts.run_terminal_review_governance
python -m scripts.run_review_quality_report
python -m scripts.run_review_status
```
"""
            content += insert_code
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Patched README.md")

if __name__ == "__main__":
    patch_settings()
    patch_env()
    patch_paths()
    patch_readme()
