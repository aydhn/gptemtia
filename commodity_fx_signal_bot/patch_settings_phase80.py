import os

closure_settings = """
    # Phase 80: Local Closure Settings
    local_closure_enabled: bool = True
    default_local_closure_profile: str = "balanced_local_closure"
    local_closure_default_language: str = "tr"
    local_closure_dry_run_default: bool = True
    local_closure_allow_real_v1_release: bool = False
    local_closure_allow_production_release_claim: bool = False
    local_closure_allow_official_project_closure_claim: bool = False
    local_closure_allow_legal_signoff_claim: bool = False
    local_closure_allow_compliance_claim: bool = False
    local_closure_allow_cloud_upload: bool = False
    local_closure_allow_package_publish: bool = False
    local_closure_allow_external_service: bool = False
    local_closure_allow_external_llm: bool = False
    local_closure_allow_file_modification: bool = False
    local_closure_allow_file_deletion: bool = False
    local_closure_allow_file_move: bool = False
    local_closure_allow_overwrite: bool = False
    local_closure_allow_live_trading_claim: bool = False
    local_closure_allow_broker_readiness_claim: bool = False
    local_closure_allow_investment_advice: bool = False
    local_closure_allow_model_deployment_claim: bool = False
    local_closure_scan_docs: bool = True
    local_closure_scan_reports: bool = True
    local_closure_scan_data_lake: bool = True
    local_closure_scan_scripts: bool = True
    local_closure_scan_tests: bool = True
    local_closure_scan_generated_docs: bool = True
    local_closure_scan_archival_outputs: bool = True
    local_closure_scan_delivery_outputs: bool = True
    local_closure_scan_acceptance_outputs: bool = True
    local_closure_scan_safety_outputs: bool = True
    local_closure_max_items: int = 500000
    local_closure_min_readiness_score: float = 0.40
    local_closure_min_quality_score: float = 0.40
    local_closure_save_reports: bool = True
"""

with open('config/settings.py', 'a', encoding='utf-8') as f:
    f.write(closure_settings)
