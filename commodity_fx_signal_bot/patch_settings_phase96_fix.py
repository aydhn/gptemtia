import os
from pathlib import Path

def patch_settings():
    settings_path = Path("config/settings.py")
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()

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
    # Find `class Settings:` and inject right after it, or append to end of file if it has no class block
    class_idx = content.find("class Settings:")
    if class_idx != -1:
        # insert right after
        inject_idx = content.find("\\n", class_idx)
        if inject_idx != -1:
            content = content[:inject_idx] + "\\n" + settings_injection + content[inject_idx:]
    else:
        # just append
        content += "\\n" + settings_injection
        
    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    patch_settings()
