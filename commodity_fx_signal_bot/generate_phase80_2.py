import os

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

ensure_dir("local_closure")

write_file("local_closure/__init__.py", "")

closure_config = """
from dataclasses import dataclass
from core.exceptions import ConfigError

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
"""
write_file("local_closure/closure_config.py", closure_config)

closure_labels = """
def list_closure_domain_labels() -> list[str]:
    return [
        "meta_review_domain",
        "lessons_learned_domain",
        "roadmap_domain",
        "governance_rehearsal_domain",
        "closure_dossier_domain",
        "recap_domain",
        "unresolved_items_domain",
        "maintenance_aftercare_domain",
        "quality_validation_domain",
        "unknown_closure_domain"
    ]

def list_closure_item_labels() -> list[str]:
    return [
        "closure_doc_item",
        "closure_report_item",
        "closure_datalake_item",
        "closure_script_item",
        "closure_test_item",
        "closure_generated_doc_item",
        "closure_safety_item",
        "closure_archival_item",
        "closure_delivery_item",
        "closure_acceptance_item",
        "closure_unknown_item"
    ]

def list_closure_status_labels() -> list[str]:
    return [
        "closure_ready_for_rehearsal",
        "closure_ready_with_warnings",
        "closure_missing",
        "closure_blocked_by_safety",
        "closure_needs_manual_review",
        "closure_unknown"
    ]

def list_roadmap_status_labels() -> list[str]:
    return [
        "roadmap_candidate",
        "roadmap_deferred",
        "roadmap_needs_research",
        "roadmap_blocked_by_safety",
        "roadmap_not_applicable",
        "roadmap_unknown"
    ]

def list_closure_risk_labels() -> list[str]:
    return [
        "closure_critical_risk",
        "closure_high_risk",
        "closure_medium_risk",
        "closure_low_risk",
        "closure_info",
        "closure_unknown_risk"
    ]

def validate_closure_domain_label(label: str) -> None:
    if label not in list_closure_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_closure_item_label(label: str) -> None:
    if label not in list_closure_item_labels():
        raise ValueError(f"Invalid item label: {label}")

def validate_closure_status(label: str) -> None:
    if label not in list_closure_status_labels():
        raise ValueError(f"Invalid closure status: {label}")

def validate_roadmap_status(label: str) -> None:
    if label not in list_roadmap_status_labels():
        raise ValueError(f"Invalid roadmap status: {label}")

def validate_closure_risk(label: str) -> None:
    if label not in list_closure_risk_labels():
        raise ValueError(f"Invalid closure risk: {label}")
"""
write_file("local_closure/closure_labels.py", closure_labels)

closure_models = """
from dataclasses import dataclass
from typing import Any
import hashlib

@dataclass
class ClosureDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ClosureItem:
    item_id: str
    item_label: str
    item_name: str
    source_layer: str
    status: str
    evidence_refs: list[str]
    warnings: list[str]

@dataclass
class LessonLearnedItem:
    lesson_id: str
    lesson_title: str
    category: str
    observation: str
    implication: str
    recommendation: str
    warnings: list[str]

@dataclass
class RoadmapItem:
    roadmap_id: str
    title: str
    category: str
    status: str
    rationale: str
    prerequisites: list[str]
    safety_boundaries: list[str]
    warnings: list[str]

@dataclass
class ClosureFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_closure_domain_id(domain_label: str) -> str:
    return hashlib.sha256(domain_label.encode()).hexdigest()[:12]

def build_closure_item_id(item_name: str, item_label: str) -> str:
    return hashlib.sha256(f"{item_name}_{item_label}".encode()).hexdigest()[:12]

def build_lesson_learned_id(lesson_title: str) -> str:
    return hashlib.sha256(lesson_title.encode()).hexdigest()[:12]

def build_roadmap_item_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def build_closure_finding_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def closure_domain_to_dict(item: ClosureDomain) -> dict[str, Any]:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": ",".join(item.required_outputs),
        "warnings": ",".join(item.warnings)
    }

def closure_item_to_dict(item: ClosureItem) -> dict[str, Any]:
    return {
        "item_id": item.item_id,
        "item_label": item.item_label,
        "item_name": item.item_name,
        "source_layer": item.source_layer,
        "status": item.status,
        "evidence_refs": ",".join(item.evidence_refs),
        "warnings": ",".join(item.warnings)
    }

def lesson_learned_item_to_dict(item: LessonLearnedItem) -> dict[str, Any]:
    return {
        "lesson_id": item.lesson_id,
        "lesson_title": item.lesson_title,
        "category": item.category,
        "observation": item.observation,
        "implication": item.implication,
        "recommendation": item.recommendation,
        "warnings": ",".join(item.warnings)
    }

def roadmap_item_to_dict(item: RoadmapItem) -> dict[str, Any]:
    return {
        "roadmap_id": item.roadmap_id,
        "title": item.title,
        "category": item.category,
        "status": item.status,
        "rationale": item.rationale,
        "prerequisites": ",".join(item.prerequisites),
        "safety_boundaries": ",".join(item.safety_boundaries),
        "warnings": ",".join(item.warnings)
    }

def closure_finding_to_dict(item: ClosureFinding) -> dict[str, Any]:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": ",".join(item.warnings)
    }
"""
write_file("local_closure/closure_models.py", closure_models)

closure_domain_registry = """
import pandas as pd
from local_closure.closure_config import LocalClosureProfile
from local_closure.closure_models import ClosureDomain, build_closure_domain_id, closure_domain_to_dict

def build_default_closure_domains(profile: LocalClosureProfile) -> list[ClosureDomain]:
    domains = [
        ClosureDomain(
            domain_id=build_closure_domain_id("meta_review_domain"),
            domain_label="meta_review_domain",
            domain_name="Final Meta Review",
            description="Overall project review in local/offline context.",
            required_outputs=["final_meta_review_report"],
            warnings=["Not an official closure."]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("lessons_learned_domain"),
            domain_label="lessons_learned_domain",
            domain_name="Lessons Learned",
            description="Collected insights and observations.",
            required_outputs=["lessons_learned_compendium"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("roadmap_domain"),
            domain_label="roadmap_domain",
            domain_name="Future Roadmap",
            description="Future work items backlog.",
            required_outputs=["future_roadmap_backlog"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("governance_rehearsal_domain"),
            domain_label="governance_rehearsal_domain",
            domain_name="Governance Rehearsal",
            description="Post-project governance rehearsal.",
            required_outputs=["post_project_governance_rehearsal_guide"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("closure_dossier_domain"),
            domain_label="closure_dossier_domain",
            domain_name="Closure Dossier",
            description="Final local closure dossier.",
            required_outputs=["v1_local_closure_dossier"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("recap_domain"),
            domain_label="recap_domain",
            domain_name="Closure Recaps",
            description="Executive and technical summaries.",
            required_outputs=["closure_executive_recap", "closure_technical_recap"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("unresolved_items_domain"),
            domain_label="unresolved_items_domain",
            domain_name="Unresolved Items",
            description="Tracking items not resolved in V1.",
            required_outputs=["closure_unresolved_items_register"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("maintenance_aftercare_domain"),
            domain_label="maintenance_aftercare_domain",
            domain_name="Maintenance and Aftercare",
            description="Post-project maintenance instructions.",
            required_outputs=["closure_maintenance_calendar_rehearsal", "closure_handoff_aftercare_guide"],
            warnings=[]
        ),
        ClosureDomain(
            domain_id=build_closure_domain_id("quality_validation_domain"),
            domain_label="quality_validation_domain",
            domain_name="Quality Validation",
            description="Final validation checks.",
            required_outputs=["closure_validation_report", "closure_quality_report"],
            warnings=[]
        )
    ]
    return domains

def build_closure_domain_registry(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_closure_domains(profile)
    df = pd.DataFrame([closure_domain_to_dict(d) for d in domains])
    summary = summarize_closure_domains(df)
    return df, summary

def summarize_closure_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df.empty:
        return {"total_domains": 0, "status": "empty"}
    return {
        "total_domains": len(domain_df),
        "domains": domain_df["domain_label"].tolist(),
        "status": "generated"
    }
"""
write_file("local_closure/closure_domain_registry.py", closure_domain_registry)
