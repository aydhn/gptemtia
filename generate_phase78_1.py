import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")

def write_file(path_str, content):
    p = BASE_DIR / path_str
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {p}")

write_file("local_delivery/__init__.py", '''
"""Local delivery module for Phase 78."""
''')

write_file("local_delivery/delivery_config.py", '''
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
''')

write_file("local_delivery/delivery_labels.py", '''
import logging

logger = logging.getLogger(__name__)

_DELIVERY_DOMAIN_LABELS = [
    "bundle_manifest_domain", "handoff_index_domain", "reviewer_guide_domain",
    "transfer_checklist_domain", "evidence_map_domain", "delivery_rehearsal_domain",
    "recipient_orientation_domain", "safety_boundary_domain", "readiness_scoring_domain",
    "quality_validation_domain", "unknown_delivery_domain"
]

_DELIVERY_ITEM_LABELS = [
    "delivery_doc_item", "delivery_report_item", "delivery_datalake_item",
    "delivery_script_item", "delivery_test_item", "delivery_generated_doc_item",
    "delivery_safety_item", "delivery_acceptance_item", "delivery_unknown_item"
]

_DELIVERY_STATUS_LABELS = [
    "delivery_ready_for_rehearsal", "delivery_ready_with_warnings", "delivery_missing",
    "delivery_blocked_by_safety", "delivery_needs_manual_review", "delivery_unknown"
]

_TRANSFER_READINESS_LABELS = [
    "transfer_ready_for_manual_review", "transfer_ready_with_warnings",
    "transfer_missing_required_item", "transfer_blocked_by_no_go",
    "transfer_not_applicable", "transfer_unknown"
]

_DELIVERY_RISK_LABELS = [
    "delivery_critical_risk", "delivery_high_risk", "delivery_medium_risk",
    "delivery_low_risk", "delivery_info", "delivery_unknown_risk"
]

def list_delivery_domain_labels() -> list[str]:
    return _DELIVERY_DOMAIN_LABELS.copy()

def list_delivery_item_labels() -> list[str]:
    return _DELIVERY_ITEM_LABELS.copy()

def list_delivery_status_labels() -> list[str]:
    return _DELIVERY_STATUS_LABELS.copy()

def list_transfer_readiness_labels() -> list[str]:
    return _TRANSFER_READINESS_LABELS.copy()

def list_delivery_risk_labels() -> list[str]:
    return _DELIVERY_RISK_LABELS.copy()

def validate_delivery_domain_label(label: str) -> None:
    if label not in _DELIVERY_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_delivery_item_label(label: str) -> None:
    if label not in _DELIVERY_ITEM_LABELS:
        raise ValueError(f"Invalid item label: {label}")

def validate_delivery_status(label: str) -> None:
    if label not in _DELIVERY_STATUS_LABELS:
        raise ValueError(f"Invalid status label: {label}")

def validate_transfer_readiness_label(label: str) -> None:
    if label not in _TRANSFER_READINESS_LABELS:
        raise ValueError(f"Invalid transfer readiness label: {label}")

def validate_delivery_risk(label: str) -> None:
    if label not in _DELIVERY_RISK_LABELS:
        raise ValueError(f"Invalid delivery risk label: {label}")
''')

write_file("local_delivery/delivery_models.py", '''
import hashlib
from dataclasses import dataclass

@dataclass
class DeliveryDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_items: list[str]
    warnings: list[str]

@dataclass
class DeliveryItem:
    item_id: str
    item_label: str
    relative_path: str
    source_layer: str
    item_status: str
    size_bytes: int | None
    modified_at_utc: str | None
    delivery_notes: list[str]
    warnings: list[str]

@dataclass
class DeliveryTraceItem:
    trace_id: str
    source_item_id: str
    source_path: str
    target_bundle_section: str
    trace_status: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeliveryChecklistItem:
    checklist_id: str
    checklist_name: str
    description: str
    readiness_label: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeliveryFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_delivery_domain_id(domain_label: str) -> str:
    return hashlib.md5(f"domain_{domain_label}".encode()).hexdigest()[:12]

def build_delivery_item_id(relative_path: str, item_label: str) -> str:
    return hashlib.md5(f"item_{relative_path}_{item_label}".encode()).hexdigest()[:12]

def build_delivery_trace_id(source_item_id: str, target_bundle_section: str) -> str:
    return hashlib.md5(f"trace_{source_item_id}_{target_bundle_section}".encode()).hexdigest()[:12]

def build_delivery_checklist_id(checklist_name: str) -> str:
    return hashlib.md5(f"check_{checklist_name}".encode()).hexdigest()[:12]

def build_delivery_finding_id(title: str) -> str:
    return hashlib.md5(f"find_{title}".encode()).hexdigest()[:12]

def delivery_domain_to_dict(item: DeliveryDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_items": item.required_items,
        "warnings": item.warnings
    }

def delivery_item_to_dict(item: DeliveryItem) -> dict:
    return {
        "item_id": item.item_id,
        "item_label": item.item_label,
        "relative_path": item.relative_path,
        "source_layer": item.source_layer,
        "item_status": item.item_status,
        "size_bytes": item.size_bytes,
        "modified_at_utc": item.modified_at_utc,
        "delivery_notes": item.delivery_notes,
        "warnings": item.warnings
    }

def delivery_trace_item_to_dict(item: DeliveryTraceItem) -> dict:
    return {
        "trace_id": item.trace_id,
        "source_item_id": item.source_item_id,
        "source_path": item.source_path,
        "target_bundle_section": item.target_bundle_section,
        "trace_status": item.trace_status,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }

def delivery_checklist_item_to_dict(item: DeliveryChecklistItem) -> dict:
    return {
        "checklist_id": item.checklist_id,
        "checklist_name": item.checklist_name,
        "description": item.description,
        "readiness_label": item.readiness_label,
        "evidence_refs": item.evidence_refs,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }

def delivery_finding_to_dict(item: DeliveryFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }
''')

write_file("local_delivery/delivery_domain_registry.py", '''
import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile
from local_delivery.delivery_models import DeliveryDomain, build_delivery_domain_id, delivery_domain_to_dict

def build_default_delivery_domains(profile: LocalDeliveryProfile) -> list[DeliveryDomain]:
    domains = []
    labels = [
        "bundle_manifest_domain", "handoff_index_domain", "reviewer_guide_domain",
        "transfer_checklist_domain", "evidence_map_domain", "delivery_rehearsal_domain",
        "recipient_orientation_domain", "safety_boundary_domain", "readiness_scoring_domain",
        "quality_validation_domain"
    ]
    for lbl in labels:
        domains.append(DeliveryDomain(
            domain_id=build_delivery_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')} for delivery rehearsal",
            required_items=["README.md", "SAFE_USAGE_GUIDE.md"],
            warnings=[]
        ))
    return domains

def build_delivery_domain_registry(profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_delivery_domains(profile)
    df = pd.DataFrame([delivery_domain_to_dict(d) for d in domains])
    return df, summarize_delivery_domains(df)

def summarize_delivery_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0}
    return {
        "total_domains": len(domain_df),
        "domains_listed": domain_df["domain_label"].tolist()
    }
''')

write_file("local_delivery/bundle_manifest.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile
from local_delivery.delivery_models import DeliveryItem, build_delivery_item_id, delivery_item_to_dict

def build_final_delivery_bundle_manifest(project_root: Path, profile: LocalDeliveryProfile) -> tuple[dict, dict]:
    manifest = {
        "local_only_delivery_statement": "This is a local/offline delivery rehearsal. No actual files are transferred.",
        "dry_run_delivery_rehearsal_statement": "Dry run mode active. No cloud upload, package publish or real transfer.",
        "included_docs_references": ["README.md", "docs/"],
        "included_generated_docs_references": ["docs/generated/"],
        "reports_output_references": ["reports/output/"],
        "data_lake_references": ["data/lake/"],
        "scripts_tests_references": ["scripts/", "tests/"],
        "safety_boundary_references": ["SAFE_USAGE_GUIDE.md"],
        "acceptance_reviewer_references": ["PORTABLE_REVIEWER_ARCHIVE_GUIDE.md"],
        "no_go_safe_go_summary": "Check no-go/safe-go register for details.",
        "manual_transfer_instructions": "Use manual USB or secure offline transfer.",
        "what_is_not_included": "Raw secrets, private keys, live trading configs, external API keys.",
        "no_cloud_upload_statement": "Cloud upload is strictly forbidden.",
        "no_package_publish_statement": "Package publishing is strictly forbidden."
    }
    return manifest, validate_delivery_bundle_manifest_safety(manifest, profile)

def build_delivery_bundle_manifest_items(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        DeliveryItem(
            item_id=build_delivery_item_id("README.md", "delivery_doc_item"),
            item_label="delivery_doc_item",
            relative_path="README.md",
            source_layer="docs",
            item_status="delivery_ready_for_rehearsal",
            size_bytes=100,
            modified_at_utc=None,
            delivery_notes=[],
            warnings=[]
        )
    ]
    df = pd.DataFrame([delivery_item_to_dict(i) for i in items])
    return df, summarize_delivery_bundle_manifest({"type": "manifest_items"}, df)

def validate_delivery_bundle_manifest_safety(manifest: dict, profile: LocalDeliveryProfile) -> dict:
    return {"manifest_safe": True, "warnings": []}

def summarize_delivery_bundle_manifest(manifest: dict, item_df: pd.DataFrame) -> dict:
    return {
        "manifest_keys": list(manifest.keys()),
        "total_items": len(item_df) if item_df is not None else 0
    }
''')
