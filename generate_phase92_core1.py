import os
from pathlib import Path

def write_file(path_str, content):
    path = Path(path_str)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")
    print(f"Created {path_str}")

def generate_core1():
    write_file("commodity_fx_signal_bot/local_continuity_intelligence/__init__.py", "")
    
    write_file("commodity_fx_signal_bot/local_continuity_intelligence/continuity_config.py", '''
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalContinuityIntelligenceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_memory_system: bool = False
    allow_cloud_memory_sync: bool = False
    allow_official_lessons_report: bool = False
    allow_official_decision_record: bool = False
    allow_legal_evidence_claim: bool = False
    allow_compliance_evidence_claim: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
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
    scan_preservation_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_longterm_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_rows: int = 250000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_continuity": LocalContinuityIntelligenceProfile(
        name="balanced_local_continuity",
        description="Genel amacli profil",
        notes="Genel amaçlı local/offline operator memory book, lessons-learned codex ve future-reader continuity profili."
    ),
    "operator_memory_focus": LocalContinuityIntelligenceProfile(
        name="operator_memory_focus",
        description="Operator memory book",
        scan_data_lake=False,
        max_rows=150000,
        notes="Operator memory book, topic map, reading route ve quick-reference cards odaklı profil."
    ),
    "lessons_decision_focus": LocalContinuityIntelligenceProfile(
        name="lessons_decision_focus",
        description="Lessons-learned codex",
        max_rows=200000,
        notes="Lessons-learned codex, decision rationale capsule ve tradeoff matrix odaklı profil."
    ),
    "strict_continuity_safety": LocalContinuityIntelligenceProfile(
        name="strict_continuity_safety",
        description="Strict safety",
        max_items=300000,
        max_rows=100000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Memory/cloud/decision/legal/compliance/release/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    ),
}

def get_local_continuity_intelligence_profile(name: str) -> LocalContinuityIntelligenceProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_continuity_intelligence_profiles(enabled_only: bool = True) -> list[LocalContinuityIntelligenceProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_continuity_intelligence_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("Language bos olamaz")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items ve max_rows pozitif olmali")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("Score 0-1 araliginda olmali")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali")
        if p.allow_real_memory_system or p.allow_cloud_memory_sync or p.allow_live_trading_claim or p.allow_investment_advice:
            raise ConfigError("Forbidden claims found in profile")

def get_default_local_continuity_intelligence_profile() -> LocalContinuityIntelligenceProfile:
    return PROFILES["balanced_local_continuity"]
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/continuity_labels.py", '''
def list_continuity_domain_labels() -> list[str]:
    return [
        "operator_memory_domain",
        "lessons_learned_domain",
        "decision_rationale_domain",
        "future_reader_domain",
        "continuity_binder_domain",
        "continuity_knowledge_graph_domain",
        "continuity_concept_domain",
        "continuity_glossary_domain",
        "continuity_interpretation_domain",
        "continuity_reminder_domain",
        "quality_validation_domain",
        "unknown_continuity_domain"
    ]

def list_continuity_status_labels() -> list[str]:
    return [
        "continuity_rehearsal_ready",
        "continuity_rehearsal_ready_with_warnings",
        "continuity_rehearsal_missing",
        "continuity_rehearsal_blocked_by_safety",
        "continuity_rehearsal_needs_manual_review",
        "continuity_rehearsal_unknown"
    ]

def list_lesson_category_labels() -> list[str]:
    return [
        "lesson_architecture",
        "lesson_data_lake",
        "lesson_reporting",
        "lesson_quality",
        "lesson_safety",
        "lesson_governance",
        "lesson_testing",
        "lesson_handoff",
        "lesson_preservation",
        "lesson_unknown"
    ]

def list_decision_area_labels() -> list[str]:
    return [
        "decision_architecture",
        "decision_governance",
        "decision_safety_boundary",
        "decision_datalake_reporting",
        "decision_testing_quality",
        "decision_documentation",
        "decision_operations",
        "decision_unknown"
    ]

def list_continuity_risk_labels() -> list[str]:
    return [
        "continuity_critical_risk",
        "continuity_high_risk",
        "continuity_medium_risk",
        "continuity_low_risk",
        "continuity_info",
        "continuity_unknown_risk"
    ]

def validate_continuity_domain_label(label: str) -> None:
    pass

def validate_continuity_status(label: str) -> None:
    pass

def validate_lesson_category(label: str) -> None:
    pass

def validate_decision_area(label: str) -> None:
    pass

def validate_continuity_risk(label: str) -> None:
    pass
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/continuity_models.py", '''
from dataclasses import dataclass
from typing import List

@dataclass
class ContinuityDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str]

@dataclass
class OperatorMemoryItem:
    memory_id: str
    topic: str
    memory_area: str
    summary: str
    source_refs: List[str]
    boundary_note: str
    warnings: List[str]

@dataclass
class LessonLearnedItem:
    lesson_id: str
    lesson_category: str
    phase_ref: str
    lesson_title: str
    lesson_summary: str
    future_use: str
    warnings: List[str]

@dataclass
class DecisionRationaleItem:
    decision_id: str
    decision_area: str
    decision_title: str
    rationale_summary: str
    tradeoffs: List[str]
    boundary_note: str
    warnings: List[str]

@dataclass
class FutureReaderItem:
    reader_id: str
    reader_role: str
    guide_area: str
    instruction_summary: str
    manual_review_required: bool
    warnings: List[str]

@dataclass
class ContinuityFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

def build_continuity_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"
def build_operator_memory_item_id(topic: str, memory_area: str) -> str:
    return f"mem_{topic}_{memory_area}".replace(" ", "_")
def build_lesson_learned_item_id(phase_ref: str, lesson_title: str) -> str:
    return f"les_{phase_ref}".replace(" ", "_")
def build_decision_rationale_item_id(decision_area: str, decision_title: str) -> str:
    return f"dec_{decision_area}".replace(" ", "_")
def build_future_reader_item_id(reader_role: str, guide_area: str) -> str:
    return f"read_{reader_role}".replace(" ", "_")
def build_continuity_finding_id(title: str) -> str:
    return f"find_{title}".replace(" ", "_")

def continuity_domain_to_dict(item: ContinuityDomain) -> dict:
    return item.__dict__
def operator_memory_item_to_dict(item: OperatorMemoryItem) -> dict:
    return item.__dict__
def lesson_learned_item_to_dict(item: LessonLearnedItem) -> dict:
    return item.__dict__
def decision_rationale_item_to_dict(item: DecisionRationaleItem) -> dict:
    return item.__dict__
def future_reader_item_to_dict(item: FutureReaderItem) -> dict:
    return item.__dict__
def continuity_finding_to_dict(item: ContinuityFinding) -> dict:
    return item.__dict__
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/continuity_domain_registry.py", '''
import pandas as pd
from .continuity_models import ContinuityDomain, build_continuity_domain_id
from .continuity_labels import list_continuity_domain_labels

def build_continuity_domain_registry(profile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_continuity_domains(profile)
    df = pd.DataFrame([d.__dict__ for d in domains])
    summary = summarize_continuity_domains(df)
    return df, summary

def build_default_continuity_domains(profile) -> list[ContinuityDomain]:
    labels = list_continuity_domain_labels()
    return [ContinuityDomain(
        domain_id=build_continuity_domain_id(l),
        domain_label=l,
        domain_name=f"Domain {l}",
        description="Local offline domain",
        required_outputs=["none"],
        warnings=["Not official scope"]
    ) for l in labels]

def summarize_continuity_domains(domain_df: pd.DataFrame) -> dict:
    return {"total": len(domain_df)}
''')

if __name__ == "__main__":
    generate_core1()
    print("Core 1 generated")
