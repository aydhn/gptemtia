from dataclasses import dataclass

@dataclass(frozen=True)
class LocalReuseProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_v1_1_implementation: bool = False
    allow_implementation_approval: bool = False
    allow_production_release_claim: bool = False
    allow_official_standard_claim: bool = False
    allow_compliance_claim: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_closure_outputs: bool = True
    scan_archival_outputs: bool = True
    scan_delivery_outputs: bool = True
    scan_acceptance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_templates: int = 10000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def get_default_local_reuse_profile() -> LocalReuseProfile:
    return LocalReuseProfile(name="balanced_local_reuse", description="Genel amaçlı")

def validate_local_reuse_profiles() -> None:
    pass
