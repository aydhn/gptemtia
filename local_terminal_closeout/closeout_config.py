from dataclasses import dataclass
from typing import Dict, List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalTerminalCloseoutProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_project_closeout: bool = False
    allow_official_governance_seal: bool = False
    allow_official_handover_constitution: bool = False
    allow_official_acceptance: bool = False
    allow_official_release: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_real_build: bool = False
    allow_cloud_build: bool = False
    allow_ci_cd: bool = False
    allow_docker_build_push: bool = False
    allow_docker_image_creation: bool = False
    allow_build_artifact: bool = False
    allow_binary_artifact: bool = False
    allow_installer_creation: bool = False
    allow_executable_packaging: bool = False
    allow_dependency_install: bool = False
    allow_environment_provisioning: bool = False
    allow_package_publish: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_real_archive_creation: bool = False
    allow_zip_creation: bool = False
    allow_web_server: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_telemetry: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_completion_outputs: bool = True
    scan_reproducibility_outputs: bool = True
    scan_packaging_outputs: bool = True
    scan_documentation_export_outputs: bool = True
    scan_review_outputs: bool = True
    scan_atlas_outputs: bool = True
    scan_continuity_outputs: bool = True
    scan_preservation_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 750000
    max_rows: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_terminal_closeout": LocalTerminalCloseoutProfile(
        name="balanced_local_terminal_closeout",
        description="Balanced profile",
        notes="Genel amaçlı local/offline terminal master closeout, ultimate project ledger ve handover constitution profili."
    ),
    "ledger_focus": LocalTerminalCloseoutProfile(
        name="ledger_focus",
        description="Ledger focus",
        max_rows=250000,
        notes="Ultimate project ledger, phase/module/script/report/docs/DataLake/governance registry odaklı profil."
    ),
    "handover_constitution_focus": LocalTerminalCloseoutProfile(
        name="handover_constitution_focus",
        description="Handover focus",
        max_rows=200000,
        notes="Pre-final handover constitution, governance seal rehearsal ve final archive catalog odaklı profil."
    ),
    "strict_terminal_closeout_safety": LocalTerminalCloseoutProfile(
        name="strict_terminal_closeout_safety",
        description="Strict safety",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Closeout/seal/handover/acceptance/release/build/archive/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_terminal_closeout_profile(name: str) -> LocalTerminalCloseoutProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_local_terminal_closeout_profiles(enabled_only: bool = True) -> list[LocalTerminalCloseoutProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_local_terminal_closeout_profiles() -> None:
    for p in _PROFILES.values():
        if not p.language:
            raise ConfigError("Language cannot be empty")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("Max items and rows must be positive")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("Scores must be 0-1")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default must be True")

def get_default_local_terminal_closeout_profile() -> LocalTerminalCloseoutProfile:
    return _PROFILES["balanced_local_terminal_closeout"]
