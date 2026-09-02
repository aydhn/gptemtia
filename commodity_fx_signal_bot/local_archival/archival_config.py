"""
Local Archival Config.
"""
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalArchivalProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    hash_algorithm: str = "sha256"
    allow_real_immutable_lock: bool = False
    allow_chmod_lock: bool = False
    allow_file_permission_change: bool = False
    allow_legal_hold_claim: bool = False
    allow_compliance_claim: bool = False
    allow_blockchain_notarization: bool = False
    allow_timestamp_authority: bool = False
    allow_cloud_archive: bool = False
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
    scan_delivery_outputs: bool = True
    scan_acceptance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_hash_items: int = 500000
    max_file_size_mb_for_hash: int = 250
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_archival": LocalArchivalProfile(
        name="balanced_local_archival",
        description="Genel amaçlı local/offline archival seal rehearsal, provenance lockfile ve custody rehearsal profili.",
        notes="Genel amaçlı local/offline archival seal rehearsal, provenance lockfile ve custody rehearsal profili."
    ),
    "provenance_lockfile_focus": LocalArchivalProfile(
        name="provenance_lockfile_focus",
        description="Local provenance lockfile, hash-of-hashes ve provenance trace matrix odaklı profil.",
        notes="Local provenance lockfile, hash-of-hashes ve provenance trace matrix odaklı profil."
    ),
    "custody_rehearsal_focus": LocalArchivalProfile(
        name="custody_rehearsal_focus",
        description="Custody chain simulation, long-term custody rehearsal guide ve retention note registry odaklı profil.",
        notes="Custody chain simulation, long-term custody rehearsal guide ve retention note registry odaklı profil."
    ),
    "strict_archival_safety": LocalArchivalProfile(
        name="strict_archival_safety",
        description="Immutable/legal/compliance/cloud/package/live/broker/advice overclaim ve sensitive-file exclusion denetimini sıkılaştıran profil.",
        max_hash_items=300000,
        max_file_size_mb_for_hash=100,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Immutable/legal/compliance/cloud/package/live/broker/advice overclaim ve sensitive-file exclusion denetimini sıkılaştıran profil."
    )
}

def get_local_archival_profile(name: str) -> LocalArchivalProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_local_archival_profiles(enabled_only: bool = True) -> list[LocalArchivalProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_archival_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name}: language is empty")
        if p.hash_algorithm not in ["sha256", "sha384", "sha512"]:
            raise ConfigError(f"Profile {name}: invalid hash algorithm {p.hash_algorithm}")
        if p.max_hash_items <= 0 or p.max_file_size_mb_for_hash <= 0:
            raise ConfigError(f"Profile {name}: max hash items/size must be positive")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name}: scores must be between 0 and 1")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name}: dry_run_default must be True in base profiles")
        if any([p.allow_real_immutable_lock, p.allow_chmod_lock, p.allow_file_permission_change,
                p.allow_legal_hold_claim, p.allow_compliance_claim, p.allow_blockchain_notarization,
                p.allow_timestamp_authority, p.allow_cloud_archive, p.allow_cloud_upload,
                p.allow_package_publish, p.allow_external_service, p.allow_external_llm,
                p.allow_file_modification, p.allow_file_deletion, p.allow_file_move,
                p.allow_overwrite, p.allow_live_trading_claim, p.allow_broker_readiness_claim,
                p.allow_investment_advice, p.allow_model_deployment_claim]):
            raise ConfigError(f"Profile {name}: active actions/claims are forbidden")

def get_default_local_archival_profile() -> LocalArchivalProfile:
    return _PROFILES["balanced_local_archival"]
