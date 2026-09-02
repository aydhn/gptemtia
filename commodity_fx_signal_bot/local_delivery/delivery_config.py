import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalDeliveryProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_transfer: bool = False
    allow_archive_creation: bool = False
    allow_zip_creation: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_official_handoff_claim: bool = False
    allow_production_handoff_claim: bool = False
    allow_compliance_claim: bool = False
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
    scan_safety_outputs: bool = True
    scan_acceptance_outputs: bool = True
    max_items: int = 500000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_delivery": LocalDeliveryProfile(
        name="balanced_local_delivery",
        description="Genel amacli local/offline final delivery rehearsal profili.",
        notes="Genel amaçlı local/offline final delivery rehearsal ve handoff package documentation profili."
    ),
    "handoff_index_focus": LocalDeliveryProfile(
        name="handoff_index_focus",
        description="Handoff package index odakli.",
        notes="Handoff package index, docs/reports/DataLake/scripts/tests/generated docs katalogları odaklı profil."
    ),
    "portable_reviewer_focus": LocalDeliveryProfile(
        name="portable_reviewer_focus",
        description="Portable reviewer guide odakli.",
        notes="Portable reviewer archive guide, evidence map ve reading order odaklı profil."
    ),
    "strict_delivery_safety": LocalDeliveryProfile(
        name="strict_delivery_safety",
        description="Siki safety sinirlari.",
        max_items=300000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Gerçek transfer, cloud upload, package publish, official handoff ve canlı/broker/deploy overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_delivery_profile(name: str) -> LocalDeliveryProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_local_delivery_profiles(enabled_only: bool = True) -> list[LocalDeliveryProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_local_delivery_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} has no language.")
        if p.max_items <= 0:
            raise ConfigError(f"Profile {name} has invalid max_items.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} has invalid scores.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True.")
        if any([
            p.allow_real_transfer, p.allow_archive_creation, p.allow_zip_creation, p.allow_cloud_upload,
            p.allow_package_publish, p.allow_external_service, p.allow_external_llm, p.allow_file_modification,
            p.allow_file_deletion, p.allow_file_move, p.allow_overwrite, p.allow_official_handoff_claim,
            p.allow_production_handoff_claim, p.allow_compliance_claim, p.allow_live_trading_claim,
            p.allow_broker_readiness_claim, p.allow_investment_advice, p.allow_model_deployment_claim
        ]):
            raise ConfigError(f"Profile {name} has unsafe allow flag set to True.")

def get_default_local_delivery_profile() -> LocalDeliveryProfile:
    return _PROFILES["balanced_local_delivery"]
