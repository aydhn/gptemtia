
from dataclasses import dataclass
class ConfigError(Exception): pass

@dataclass(frozen=True)
class LocalClosureProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_v1_release: bool = False
    allow_production_release_claim: bool = False
    allow_official_project_closure_claim: bool = False
    allow_legal_signoff_claim: bool = False
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
    scan_archival_outputs: bool = True
    scan_delivery_outputs: bool = True
    scan_acceptance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_closure": LocalClosureProfile(
        name="balanced_local_closure",
        description="Balanced closure profile",
        language="tr",
        dry_run_default=True,
        notes="Genel amaçlı local/offline v1.0 closure rehearsal, meta-review ve lessons-learned profili."
    ),
    "meta_review_focus": LocalClosureProfile(
        name="meta_review_focus",
        description="Meta review focus",
        language="tr",
        dry_run_default=True,
        notes="Final meta-review, recap ve closure dossier odaklı profil."
    ),
    "roadmap_focus": LocalClosureProfile(
        name="roadmap_focus",
        description="Roadmap focus",
        language="tr",
        dry_run_default=True,
        notes="Future roadmap backlog, future phase candidates ve improvement backlog odaklı profil."
    ),
    "strict_closure_safety": LocalClosureProfile(
        name="strict_closure_safety",
        description="Strict closure safety",
        language="tr",
        dry_run_default=True,
        max_items=300000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Real v1 release, production release, official closure, compliance, package publish, live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_closure_profile(name: str) -> LocalClosureProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown local closure profile: {name}")
    return _PROFILES[name]

def list_local_closure_profiles(enabled_only: bool = True) -> list[LocalClosureProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_closure_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} missing language")
        if p.max_items <= 0:
            raise ConfigError(f"Profile {name} max_items must be positive")
        if not (0 <= p.min_readiness_score <= 1):
            raise ConfigError(f"Profile {name} min_readiness_score must be between 0 and 1")
        if not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_quality_score must be between 0 and 1")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True")
        
        forbidden_flags = [
            p.allow_real_v1_release,
            p.allow_production_release_claim,
            p.allow_official_project_closure_claim,
            p.allow_legal_signoff_claim,
            p.allow_compliance_claim,
            p.allow_cloud_upload,
            p.allow_package_publish,
            p.allow_external_service,
            p.allow_external_llm,
            p.allow_file_modification,
            p.allow_file_deletion,
            p.allow_file_move,
            p.allow_overwrite,
            p.allow_live_trading_claim,
            p.allow_broker_readiness_claim,
            p.allow_investment_advice,
            p.allow_model_deployment_claim
        ]
        if any(forbidden_flags):
            raise ConfigError(f"Profile {name} has forbidden allow flags set to True")

def get_default_local_closure_profile() -> LocalClosureProfile:
    return _PROFILES["balanced_local_closure"]
