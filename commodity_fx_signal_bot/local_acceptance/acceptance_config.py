from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalAcceptanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_official_signoff: bool = False
    allow_compliance_claim: bool = False
    allow_production_release_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_package_publish: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_safety_outputs: bool = True
    scan_hardening_outputs: bool = True
    scan_synthesis_outputs: bool = True
    max_evidence_items: int = 500000
    max_questions: int = 5000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_acceptance": LocalAcceptanceProfile(
        name="balanced_local_acceptance",
        description="Genel amaçlı local/offline final acceptance simulation ve verification rehearsal profili.",
        notes="Genel amaçlı local/offline final acceptance simulation ve verification rehearsal profili."
    ),
    "independent_reviewer_focus": LocalAcceptanceProfile(
        name="independent_reviewer_focus",
        description="Independent reviewer pack, question bank ve evidence request matrix odaklı profil.",
        max_questions=3000,
        notes="Independent reviewer pack, question bank ve evidence request matrix odaklı profil."
    ),
    "evidence_trail_focus": LocalAcceptanceProfile(
        name="evidence_trail_focus",
        description="Audit-style local evidence trail ve trace matrix odaklı profil.",
        max_evidence_items=500000,
        notes="Audit-style local evidence trail ve trace matrix odaklı profil."
    ),
    "strict_acceptance_safety": LocalAcceptanceProfile(
        name="strict_acceptance_safety",
        description="Official sign-off, compliance, production release, canlı trading, broker readiness ve yatırım tavsiyesi overclaim denetimini sıkılaştıran profil.",
        max_evidence_items=300000,
        max_questions=3000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Official sign-off, compliance, production release, canlı trading, broker readiness ve yatırım tavsiyesi overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_acceptance_profile(name: str) -> LocalAcceptanceProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return _PROFILES[name]

def list_local_acceptance_profiles(enabled_only: bool = True) -> list[LocalAcceptanceProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_acceptance_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} language boş olamaz.")
        if p.max_evidence_items <= 0:
            raise ConfigError(f"Profile {name} max_evidence_items pozitif olmalı.")
        if p.max_questions <= 0:
            raise ConfigError(f"Profile {name} max_questions pozitif olmalı.")
        if not (0 <= p.min_readiness_score <= 1):
            raise ConfigError(f"Profile {name} min_readiness_score 0-1 aralığında olmalı.")
        if not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_quality_score 0-1 aralığında olmalı.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default True olmalı.")
        
        allow_flags = [p.allow_official_signoff, p.allow_compliance_claim, p.allow_production_release_claim,
                       p.allow_live_trading_claim, p.allow_broker_readiness_claim, p.allow_investment_advice,
                       p.allow_model_deployment_claim, p.allow_package_publish, p.allow_cloud_upload,
                       p.allow_external_service, p.allow_external_llm, p.allow_file_modification,
                       p.allow_file_deletion, p.allow_file_move, p.allow_overwrite]
        if any(allow_flags):
            raise ConfigError(f"Profile {name} allow flagleri False olmalı.")

def get_default_local_acceptance_profile() -> LocalAcceptanceProfile:
    return _PROFILES["balanced_local_acceptance"]
