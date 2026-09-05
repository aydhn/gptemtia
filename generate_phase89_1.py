import os
from pathlib import Path

def create_files():
    base_dir = Path("commodity_fx_signal_bot/local_longterm_operations")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    with open(base_dir / "__init__.py", "w", encoding="utf-8") as f:
        f.write('"""Local Long-Term Operations and v1.x Roadmap Governance layer."""\n')
        
    with open(base_dir / "longterm_config.py", "w", encoding="utf-8") as f:
        f.write('''"""Long-term operations configuration."""
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalLongTermOperationsProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_operations_plan: bool = False
    allow_official_lifecycle_policy: bool = False
    allow_real_deprecation: bool = False
    allow_auto_deprecation: bool = False
    allow_auto_migration: bool = False
    allow_production_roadmap_claim: bool = False
    allow_official_release_commitment: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_signoff: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_telemetry: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
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
    scan_generated_docs: bool = True
    scan_release_candidate_outputs: bool = True
    scan_incident_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_calendar_rows: int = 10000
    max_workbook_rows: int = 100000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_longterm_operations": LocalLongTermOperationsProfile(
        name="balanced_local_longterm_operations",
        description="Balanced long-term operations profile.",
        notes="Genel amaçlı local/offline long-term operations binder, lifecycle maintenance workbook ve v1.x roadmap governance profili."
    ),
    "maintenance_calendar_focus": LocalLongTermOperationsProfile(
        name="maintenance_calendar_focus",
        description="Maintenance calendar focus profile.",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_generated_docs=True,
        scan_release_candidate_outputs=True,
        scan_incident_outputs=False,
        scan_governance_outputs=False,
        scan_safety_outputs=False,
        max_calendar_rows=8000,
        notes="Yearly/quarterly/monthly/weekly review calendars ve maintenance cadence odaklı profil."
    ),
    "deprecation_roadmap_focus": LocalLongTermOperationsProfile(
        name="deprecation_roadmap_focus",
        description="Deprecation roadmap focus profile.",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=False,
        scan_tests=False,
        scan_generated_docs=False,
        scan_release_candidate_outputs=False,
        scan_incident_outputs=True,
        scan_governance_outputs=True,
        scan_safety_outputs=False,
        max_workbook_rows=80000,
        notes="Deprecation rehearsal, migration readiness ve v1.x roadmap governance odaklı profil."
    ),
    "strict_lifecycle_safety": LocalLongTermOperationsProfile(
        name="strict_lifecycle_safety",
        description="Strict lifecycle safety profile.",
        max_items=300000,
        max_calendar_rows=5000,
        max_workbook_rows=50000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Operations/lifecycle/deprecation/migration/roadmap/release/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_longterm_operations_profile(name: str) -> LocalLongTermOperationsProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_local_longterm_operations_profiles(enabled_only: bool = True) -> list[LocalLongTermOperationsProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_longterm_operations_profiles() -> None:
    for profile in _PROFILES.values():
        if not profile.language:
            raise ConfigError("Language cannot be empty.")
        if profile.max_items <= 0 or profile.max_calendar_rows <= 0 or profile.max_workbook_rows <= 0:
            raise ConfigError("Max limits must be positive.")
        if not (0.0 <= profile.min_readiness_score <= 1.0) or not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError("Scores must be between 0 and 1.")
        if not profile.dry_run_default:
            raise ConfigError("dry_run_default must be True.")
        if any([
            profile.allow_real_operations_plan, profile.allow_official_lifecycle_policy,
            profile.allow_real_deprecation, profile.allow_auto_deprecation,
            profile.allow_auto_migration, profile.allow_production_roadmap_claim,
            profile.allow_official_release_commitment, profile.allow_package_publish,
            profile.allow_docker_build_push, profile.allow_git_tag,
            profile.allow_cloud_upload, profile.allow_deployment,
            profile.allow_legal_signoff, profile.allow_compliance_signoff,
            profile.allow_live_trading_claim, profile.allow_broker_readiness_claim,
            profile.allow_investment_advice, profile.allow_model_deployment_claim,
            profile.allow_telemetry, profile.allow_dashboard_creation,
            profile.allow_gui_creation, profile.allow_tui_creation,
            profile.allow_external_service, profile.allow_external_llm,
            profile.allow_file_modification, profile.allow_file_deletion,
            profile.allow_file_move, profile.allow_overwrite
        ]):
            raise ConfigError("All dangerous allow flags must be False.")

def get_default_local_longterm_operations_profile() -> LocalLongTermOperationsProfile:
    return _PROFILES["balanced_local_longterm_operations"]
''')

    with open(base_dir / "longterm_labels.py", "w", encoding="utf-8") as f:
        f.write('''"""Long-term labels definition."""

_DOMAIN_LABELS = [
    "longterm_operations_binder_domain",
    "review_calendar_domain",
    "lifecycle_maintenance_domain",
    "maintenance_cadence_domain",
    "retention_review_domain",
    "quality_safety_review_domain",
    "incident_redteam_governance_review_domain",
    "deprecation_rehearsal_domain",
    "migration_readiness_domain",
    "roadmap_governance_domain",
    "feature_intake_domain",
    "change_control_domain",
    "quality_validation_domain",
    "unknown_longterm_domain"
]

_CALENDAR_LABELS = [
    "calendar_rehearsal_available",
    "calendar_rehearsal_partial",
    "calendar_rehearsal_missing",
    "calendar_rehearsal_manual_review",
    "calendar_rehearsal_unknown"
]

_LIFECYCLE_LABELS = [
    "lifecycle_rehearsal_ready",
    "lifecycle_rehearsal_ready_with_warnings",
    "lifecycle_rehearsal_missing",
    "lifecycle_rehearsal_blocked_by_safety",
    "lifecycle_rehearsal_needs_manual_review",
    "lifecycle_rehearsal_unknown"
]

_DEPRECATION_LABELS = [
    "deprecation_rehearsal_candidate",
    "deprecation_rehearsal_not_candidate",
    "deprecation_rehearsal_blocked",
    "deprecation_rehearsal_manual_review",
    "deprecation_rehearsal_unknown"
]

_RISK_LABELS = [
    "lifecycle_critical_risk",
    "lifecycle_high_risk",
    "lifecycle_medium_risk",
    "lifecycle_low_risk",
    "lifecycle_info",
    "lifecycle_unknown_risk"
]

def list_longterm_domain_labels() -> list[str]:
    return _DOMAIN_LABELS

def list_calendar_status_labels() -> list[str]:
    return _CALENDAR_LABELS

def list_lifecycle_status_labels() -> list[str]:
    return _LIFECYCLE_LABELS

def list_deprecation_status_labels() -> list[str]:
    return _DEPRECATION_LABELS

def list_lifecycle_risk_labels() -> list[str]:
    return _RISK_LABELS

def validate_longterm_domain_label(label: str) -> None:
    if label not in _DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_calendar_status(label: str) -> None:
    if label not in _CALENDAR_LABELS:
        raise ValueError(f"Invalid calendar status label: {label}")

def validate_lifecycle_status(label: str) -> None:
    if label not in _LIFECYCLE_LABELS:
        raise ValueError(f"Invalid lifecycle status label: {label}")

def validate_deprecation_status(label: str) -> None:
    if label not in _DEPRECATION_LABELS:
        raise ValueError(f"Invalid deprecation status label: {label}")

def validate_lifecycle_risk(label: str) -> None:
    if label not in _RISK_LABELS:
        raise ValueError(f"Invalid lifecycle risk label: {label}")
''')

    with open(base_dir / "longterm_models.py", "w", encoding="utf-8") as f:
        f.write('''"""Long-term models."""
from dataclasses import dataclass
import hashlib

@dataclass
class LongTermDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ReviewCalendarItem:
    calendar_id: str
    calendar_name: str
    cadence: str
    review_area: str
    calendar_status: str
    expected_manual_action: str
    warnings: list[str]

@dataclass
class LifecycleWorkbookItem:
    workbook_id: str
    workbook_area: str
    lifecycle_status: str
    review_question: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeprecationCandidate:
    candidate_id: str
    candidate_name: str
    candidate_area: str
    deprecation_status: str
    impact_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class RoadmapCandidate:
    roadmap_id: str
    roadmap_name: str
    roadmap_area: str
    priority_hint: str
    expected_benefit: str
    risk_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class LifecycleFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_longterm_domain_id(domain_label: str) -> str:
    return hashlib.sha256(domain_label.encode()).hexdigest()[:12]

def build_review_calendar_item_id(calendar_name: str, review_area: str) -> str:
    return hashlib.sha256(f"{calendar_name}_{review_area}".encode()).hexdigest()[:12]

def build_lifecycle_workbook_item_id(workbook_area: str, review_question: str) -> str:
    return hashlib.sha256(f"{workbook_area}_{review_question}".encode()).hexdigest()[:12]

def build_deprecation_candidate_id(candidate_name: str, candidate_area: str) -> str:
    return hashlib.sha256(f"{candidate_name}_{candidate_area}".encode()).hexdigest()[:12]

def build_roadmap_candidate_id(roadmap_name: str, roadmap_area: str) -> str:
    return hashlib.sha256(f"{roadmap_name}_{roadmap_area}".encode()).hexdigest()[:12]

def build_lifecycle_finding_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def longterm_domain_to_dict(item: LongTermDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": "|".join(item.required_outputs),
        "warnings": "|".join(item.warnings)
    }

def review_calendar_item_to_dict(item: ReviewCalendarItem) -> dict:
    return {
        "calendar_id": item.calendar_id,
        "calendar_name": item.calendar_name,
        "cadence": item.cadence,
        "review_area": item.review_area,
        "calendar_status": item.calendar_status,
        "expected_manual_action": item.expected_manual_action,
        "warnings": "|".join(item.warnings)
    }

def lifecycle_workbook_item_to_dict(item: LifecycleWorkbookItem) -> dict:
    return {
        "workbook_id": item.workbook_id,
        "workbook_area": item.workbook_area,
        "lifecycle_status": item.lifecycle_status,
        "review_question": item.review_question,
        "evidence_refs": "|".join(item.evidence_refs),
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def deprecation_candidate_to_dict(item: DeprecationCandidate) -> dict:
    return {
        "candidate_id": item.candidate_id,
        "candidate_name": item.candidate_name,
        "candidate_area": item.candidate_area,
        "deprecation_status": item.deprecation_status,
        "impact_note": item.impact_note,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def roadmap_candidate_to_dict(item: RoadmapCandidate) -> dict:
    return {
        "roadmap_id": item.roadmap_id,
        "roadmap_name": item.roadmap_name,
        "roadmap_area": item.roadmap_area,
        "priority_hint": item.priority_hint,
        "expected_benefit": item.expected_benefit,
        "risk_note": item.risk_note,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def lifecycle_finding_to_dict(item: LifecycleFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }
''')

    with open(base_dir / "longterm_domain_registry.py", "w", encoding="utf-8") as f:
        f.write('''"""Long-term domain registry."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile
from .longterm_models import LongTermDomain, build_longterm_domain_id, longterm_domain_to_dict

def build_default_longterm_domains(profile: LocalLongTermOperationsProfile) -> list[LongTermDomain]:
    labels = [
        "longterm_operations_binder_domain",
        "review_calendar_domain",
        "lifecycle_maintenance_domain",
        "maintenance_cadence_domain",
        "retention_review_domain",
        "quality_safety_review_domain",
        "incident_redteam_governance_review_domain",
        "deprecation_rehearsal_domain",
        "migration_readiness_domain",
        "roadmap_governance_domain",
        "feature_intake_domain",
        "change_control_domain",
        "quality_validation_domain"
    ]
    domains = []
    for lbl in labels:
        domains.append(LongTermDomain(
            domain_id=build_longterm_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')} rehearsal.",
            required_outputs=["rehearsal_report.md"],
            warnings=["Bu domain official operations scope değildir."]
        ))
    return domains

def build_longterm_domain_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_longterm_domains(profile)
    df = pd.DataFrame([longterm_domain_to_dict(d) for d in domains])
    summary = summarize_longterm_domains(df)
    return df, summary

def summarize_longterm_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].tolist() if not domain_df.empty else []
    }
''')

    with open(base_dir / "operations_binder.py", "w", encoding="utf-8") as f:
        f.write('''"""Operations binder."""
from pathlib import Path
from .longterm_config import LocalLongTermOperationsProfile

def build_longterm_operations_binder_sections(project_root: Path, profile: LocalLongTermOperationsProfile) -> list[dict]:
    return [
        {"title": "Amaç ve Kapsam", "content": "Offline/local long-term operations binder provası."},
        {"title": "Bu binder ne değildir?", "content": "Gerçek production operations plan değildir. Official lifecycle policy değildir. Roadmap commitment değildir. Yatırım tavsiyesi yoktur."},
        {"title": "Long-term operations overview", "content": "Sistem lokal olarak bakım altındadır."},
        {"title": "Yearly/quarterly/monthly/weekly review overview", "content": "Manuel inceleme takvimleri oluşturulmuştur."},
        {"title": "Lifecycle maintenance workbook recap", "content": "Bakım defteri hazırlandı."},
        {"title": "Retention/DataLake/generated docs review recap", "content": "Dosya saklama ve inceleme defteri."},
        {"title": "Quality/safety/incident/redteam/governance review recap", "content": "Kalite ve güvenlik değerlendirmeleri."},
        {"title": "Deprecation rehearsal recap", "content": "Offline deneme amaçlı deprecation provası."},
        {"title": "Migration readiness recap", "content": "Local migration deneme planı."},
        {"title": "v1.x roadmap governance recap", "content": "Local roadmap planlama defteri."},
        {"title": "Change-control rehearsal recap", "content": "Değişiklik kontrol provası."},
        {"title": "No-go/safe-go recap", "content": "Güvenlik sınırları."},
        {"title": "Final manual review requirements", "content": "Tüm adımlar manuel onay gerektirir."},
        {"title": "Final non-production boundary statement", "content": "Sistem kesinlikle canlı ortama çıkmaya hazır değildir."}
    ]

def build_final_local_longterm_operations_binder(project_root: Path, profile: LocalLongTermOperationsProfile) -> tuple[str, dict]:
    sections = build_longterm_operations_binder_sections(project_root, profile)
    text = "# Final Local Long-Term Operations Binder\\n\\n"
    for sec in sections:
        text += f"## {sec['title']}\\n{sec['content']}\\n\\n"
    summary = summarize_longterm_operations_binder(text)
    return text, summary

def summarize_longterm_operations_binder(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("##")
    }

def save_longterm_operations_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return output_path
''')

if __name__ == "__main__":
    create_files()
