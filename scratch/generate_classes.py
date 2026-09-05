import os
from pathlib import Path

ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/advanced_gap_closure")

def w(name, content):
    with open(ROOT_DIR / name, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# __init__.py
w("__init__.py", "")

# gap_closure_config.py
w("gap_closure_config.py", """
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class FunctionalGapClosureProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 105
    target_final_phase: int = 160
    next_phase: int = 106
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    enable_phase_106_handoff: bool = True
    enable_provider_requirements: bool = True
    enable_no_scraping_boundary: bool = True
    enable_readiness_reconciliation: bool = True
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_functional_gap_closure": FunctionalGapClosureProfile(
        name="balanced_functional_gap_closure",
        description="Phase 105 functional gap closure ve Phase 106 data foundation handoff için dengeli profil.",
        notes="Phase 105 functional gap closure ve Phase 106 data foundation handoff için dengeli profil."
    ),
    "strict_gap_closure_safety": FunctionalGapClosureProfile(
        name="strict_gap_closure_safety",
        description="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen gap closure profili.",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen gap closure profili."
    ),
    "phase_106_handoff_focus": FunctionalGapClosureProfile(
        name="phase_106_handoff_focus",
        description="Phase 106 Multi-Provider Data Abstraction handoff gereksinimlerine odaklı profil.",
        notes="Phase 106 Multi-Provider Data Abstraction handoff gereksinimlerine odaklı profil."
    )
}

def get_functional_gap_closure_profile(name: str) -> FunctionalGapClosureProfile:
    if name not in PROFILES:
        raise ConfigError(f"Profile {name} not found")
    return PROFILES[name]

def list_functional_gap_closure_profiles(enabled_only: bool = True) -> list[FunctionalGapClosureProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_functional_gap_closure_profiles() -> None:
    for p in PROFILES.values():
        assert p.current_phase == 105
        assert p.target_final_phase == 160
        assert p.next_phase == 106
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert not p.allow_live_trading
        assert not p.allow_broker_integration
        assert not p.allow_real_order
        assert not p.allow_investment_advice
        assert not p.allow_model_deployment
        assert not p.allow_production_deployment
        assert not p.allow_web_server
        assert not p.allow_dashboard
        assert not p.allow_gui_tui
        assert not p.allow_external_llm
        assert not p.allow_vector_db
        assert not p.allow_embedding_api
        assert not p.allow_web_scraping
        assert not p.allow_cloud_publish
        assert not p.allow_docker_push
        assert not p.allow_git_tag
        assert not p.allow_archive_creation
        assert not p.allow_file_deletion
        assert not p.allow_file_move
        assert not p.allow_overwrite
        assert 0.0 <= p.min_readiness_score <= 1.0
        assert 0.0 <= p.min_quality_score <= 1.0

def get_default_functional_gap_closure_profile() -> FunctionalGapClosureProfile:
    return PROFILES["balanced_functional_gap_closure"]
""")

w("gap_closure_labels.py", """
DOMAIN_LABELS = [
    "gap_closure_profile_domain", "readiness_reconciliation_domain", "mvp_to_v2_closure_domain",
    "foundation_audit_domain", "dependency_closure_domain", "missing_functionality_domain",
    "implementation_backlog_domain", "phase_106_handoff_domain", "data_provider_requirement_domain",
    "no_scraping_boundary_domain", "provider_interface_readiness_domain", "data_quality_readiness_domain",
    "contract_handoff_domain", "functional_safety_domain", "functional_quality_domain", "unknown_gap_closure_domain"
]

STATUS_LABELS = [
    "gap_closed", "gap_partially_closed", "gap_open", "gap_blocked_by_safety",
    "gap_deferred_to_future_phase", "gap_needs_manual_review", "gap_unknown"
]

PRIORITY_LABELS = [
    "priority_critical", "priority_high", "priority_medium", "priority_low", "priority_info"
]

READINESS_LABELS = [
    "data_foundation_ready", "data_foundation_ready_with_warnings", "data_foundation_missing",
    "data_foundation_blocked_by_no_scraping_boundary", "data_foundation_needs_manual_review", "data_foundation_unknown"
]

RISK_LABELS = [
    "functional_gap_critical_risk", "functional_gap_high_risk", "functional_gap_medium_risk",
    "functional_gap_low_risk", "functional_gap_info", "functional_gap_unknown_risk"
]

def list_gap_closure_domain_labels(): return DOMAIN_LABELS
def list_gap_status_labels(): return STATUS_LABELS
def list_implementation_priority_labels(): return PRIORITY_LABELS
def list_data_foundation_readiness_labels(): return READINESS_LABELS
def list_functional_gap_risk_labels(): return RISK_LABELS

def validate_gap_closure_domain_label(label: str): assert label in DOMAIN_LABELS
def validate_gap_status(label: str): assert label in STATUS_LABELS
def validate_implementation_priority(label: str): assert label in PRIORITY_LABELS
def validate_data_foundation_readiness(label: str): assert label in READINESS_LABELS
def validate_functional_gap_risk_label(label: str): assert label in RISK_LABELS
""")

w("gap_closure_models.py", """
from dataclasses import dataclass, asdict

@dataclass
class GapClosureProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    status_label: str
    warnings: list[str]

@dataclass
class ReadinessReconciliationItem:
    reconciliation_id: str
    foundation_area: str
    source_phase_range: str
    current_state: str
    target_state: str
    reconciliation_status: str
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ClosureMatrixItem:
    closure_id: str
    mvp_area: str
    advanced_target_area: str
    current_phase_support: str
    required_future_phase: str
    closure_status: str
    gap_note: str
    manual_review_required: bool

@dataclass
class MissingFunctionalityItem:
    missing_id: str
    functionality_area: str
    current_gap: str
    required_for_phase: int
    priority_label: str
    risk_label: str
    recommendation: str
    manual_review_required: bool

@dataclass
class DataFoundationRequirement:
    requirement_id: str
    requirement_area: str
    required_for_phase: int
    provider_relevance: str
    no_scraping_constraint: str
    expected_contract: str
    readiness_label: str
    warnings: list[str]

@dataclass
class ContractHandoffItem:
    handoff_id: str
    source_layer: str
    target_layer: str
    contract_area: str
    handoff_summary: str
    handoff_status: str
    manual_review_required: bool

@dataclass
class FunctionalGapFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_gap_closure_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_readiness_reconciliation_id(foundation_area: str, source_phase_range: str) -> str: return f"recon_{foundation_area}_{source_phase_range}"
def build_closure_matrix_id(mvp_area: str, advanced_target_area: str) -> str: return f"closure_{mvp_area}_{advanced_target_area}"
def build_missing_functionality_id(functionality_area: str, required_for_phase: int) -> str: return f"miss_{functionality_area}_{required_for_phase}"
def build_data_foundation_requirement_id(requirement_area: str, required_for_phase: int) -> str: return f"req_{requirement_area}_{required_for_phase}"
def build_contract_handoff_id(source_layer: str, target_layer: str, contract_area: str) -> str: return f"handoff_{source_layer}_{target_layer}_{contract_area}"
def build_functional_gap_finding_id(title: str) -> str: return f"finding_{title.replace(' ', '_').lower()}"

def to_dict(obj):
    return asdict(obj)
""")

print("Generated models and config")
