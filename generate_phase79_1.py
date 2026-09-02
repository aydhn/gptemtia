import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\commodity_fx_signal_bot")

write_file(base_dir / "local_archival" / "__init__.py", "")

write_file(base_dir / "local_archival" / "archival_config.py", '''"""
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
''')

write_file(base_dir / "local_archival" / "archival_labels.py", '''"""
Archival Labels.
"""

_ARCHIVAL_DOMAIN_LABELS = [
    "seal_rehearsal_domain",
    "immutable_manifest_domain",
    "provenance_lockfile_domain",
    "hash_catalog_domain",
    "hash_policy_domain",
    "exclusion_policy_domain",
    "custody_rehearsal_domain",
    "retention_domain",
    "tamper_evidence_domain",
    "reproducibility_domain",
    "provenance_trace_domain",
    "quality_validation_domain",
    "unknown_archival_domain"
]

_ARCHIVAL_ITEM_LABELS = [
    "archival_doc_item",
    "archival_report_item",
    "archival_datalake_item",
    "archival_script_item",
    "archival_test_item",
    "archival_generated_doc_item",
    "archival_safety_item",
    "archival_delivery_item",
    "archival_acceptance_item",
    "archival_excluded_sensitive_item",
    "archival_unknown_item"
]

_HASH_STATUS_LABELS = [
    "hash_rehearsal_ready",
    "hash_rehearsal_skipped_sensitive",
    "hash_rehearsal_skipped_large_file",
    "hash_rehearsal_missing",
    "hash_rehearsal_error",
    "hash_rehearsal_unknown"
]

_CUSTODY_STATUS_LABELS = [
    "custody_rehearsal_ready",
    "custody_rehearsal_ready_with_warnings",
    "custody_rehearsal_missing",
    "custody_rehearsal_blocked_by_safety",
    "custody_rehearsal_needs_manual_review",
    "custody_rehearsal_unknown"
]

_ARCHIVAL_RISK_LABELS = [
    "archival_critical_risk",
    "archival_high_risk",
    "archival_medium_risk",
    "archival_low_risk",
    "archival_info",
    "archival_unknown_risk"
]

def list_archival_domain_labels() -> list[str]: return _ARCHIVAL_DOMAIN_LABELS.copy()
def list_archival_item_labels() -> list[str]: return _ARCHIVAL_ITEM_LABELS.copy()
def list_hash_status_labels() -> list[str]: return _HASH_STATUS_LABELS.copy()
def list_custody_status_labels() -> list[str]: return _CUSTODY_STATUS_LABELS.copy()
def list_archival_risk_labels() -> list[str]: return _ARCHIVAL_RISK_LABELS.copy()

def validate_archival_domain_label(label: str) -> None:
    if label not in _ARCHIVAL_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_archival_item_label(label: str) -> None:
    if label not in _ARCHIVAL_ITEM_LABELS:
        raise ValueError(f"Invalid item label: {label}")

def validate_hash_status(label: str) -> None:
    if label not in _HASH_STATUS_LABELS:
        raise ValueError(f"Invalid hash status: {label}")

def validate_custody_status(label: str) -> None:
    if label not in _CUSTODY_STATUS_LABELS:
        raise ValueError(f"Invalid custody status: {label}")

def validate_archival_risk(label: str) -> None:
    if label not in _ARCHIVAL_RISK_LABELS:
        raise ValueError(f"Invalid risk label: {label}")
''')

write_file(base_dir / "local_archival" / "archival_models.py", '''"""
Archival Models.
"""
import hashlib
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class ArchivalDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_artifacts: list[str]
    warnings: list[str]

@dataclass
class ArchivalItem:
    item_id: str
    item_label: str
    relative_path: str
    source_layer: str
    hash_algorithm: Optional[str]
    hash_value: Optional[str]
    hash_status: str
    size_bytes: Optional[int]
    modified_at_utc: Optional[str]
    warnings: list[str]

@dataclass
class ProvenanceLockEntry:
    entry_id: str
    relative_path: str
    source_layer: str
    provenance_note: str
    hash_ref: Optional[str]
    exclusion_reason: Optional[str]
    warnings: list[str]

@dataclass
class CustodyRehearsalItem:
    custody_id: str
    custody_step: str
    custody_status: str
    responsible_role_hint: str
    evidence_refs: list[str]
    warnings: list[str]

@dataclass
class ArchivalFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_archival_domain_id(domain_label: str) -> str:
    return hashlib.sha256(f"domain:{domain_label}".encode('utf-8')).hexdigest()[:16]

def build_archival_item_id(relative_path: str, item_label: str) -> str:
    return hashlib.sha256(f"item:{relative_path}:{item_label}".encode('utf-8')).hexdigest()[:16]

def build_provenance_lock_entry_id(relative_path: str) -> str:
    return hashlib.sha256(f"lock:{relative_path}".encode('utf-8')).hexdigest()[:16]

def build_custody_rehearsal_item_id(custody_step: str) -> str:
    return hashlib.sha256(f"custody:{custody_step}".encode('utf-8')).hexdigest()[:16]

def build_archival_finding_id(title: str) -> str:
    return hashlib.sha256(f"finding:{title}".encode('utf-8')).hexdigest()[:16]

def archival_domain_to_dict(item: ArchivalDomain) -> dict: return asdict(item)
def archival_item_to_dict(item: ArchivalItem) -> dict: return asdict(item)
def provenance_lock_entry_to_dict(item: ProvenanceLockEntry) -> dict: return asdict(item)
def custody_rehearsal_item_to_dict(item: CustodyRehearsalItem) -> dict: return asdict(item)
def archival_finding_to_dict(item: ArchivalFinding) -> dict: return asdict(item)
''')

write_file(base_dir / "local_archival" / "archival_domain_registry.py", '''"""
Archival Domain Registry.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archival_models import ArchivalDomain, build_archival_domain_id, archival_domain_to_dict

def build_default_archival_domains(profile: LocalArchivalProfile) -> list[ArchivalDomain]:
    return [
        ArchivalDomain(
            domain_id=build_archival_domain_id("seal_rehearsal_domain"),
            domain_label="seal_rehearsal_domain",
            domain_name="Seal Rehearsal Domain",
            description="Local/offline archival seal rehearsal context.",
            required_artifacts=["final_archival_seal_rehearsal_manifest"],
            warnings=["Not an official archival scope."]
        ),
        ArchivalDomain(
            domain_id=build_archival_domain_id("provenance_lockfile_domain"),
            domain_label="provenance_lockfile_domain",
            domain_name="Provenance Lockfile Domain",
            description="Local provenance lockfile domain.",
            required_artifacts=["local_provenance_lockfile"],
            warnings=["Not a legal lockfile."]
        )
    ]

def build_archival_domain_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_archival_domains(profile)
    df = pd.DataFrame([archival_domain_to_dict(d) for d in domains])
    summary = summarize_archival_domains(df)
    return df, summary

def summarize_archival_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df) if domain_df is not None else 0,
        "note": "This is a local/offline dry-run registry."
    }
''')

print("generate_phase79_1.py created.")
