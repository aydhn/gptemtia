import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

write_file('local_briefing/__init__.py', '''
"""Local Briefing and Stakeholder Communication Module."""
''')

write_file('local_briefing/briefing_config.py', '''
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalBriefingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_investment_advice: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_production_release_claim: bool = False
    allow_model_deployment_claim: bool = False
    allow_official_board_decision_claim: bool = False
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
    scan_cross_layer_outputs: bool = True
    scan_training_outputs: bool = True
    max_sections: int = 5000
    max_slide_items: int = 200
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_briefing": LocalBriefingProfile(
        name="balanced_local_briefing",
        description="Genel amacli local/offline stakeholder communication ve executive briefing profili.",
        notes="Genel amacli local/offline stakeholder communication ve executive briefing profili."
    ),
    "executive_summary_focus": LocalBriefingProfile(
        name="executive_summary_focus",
        description="Executive summary odakli profil.",
        max_sections=2500,
        max_slide_items=120,
        notes="Executive summary, one-pager ve decision-context binder odakli profil."
    ),
    "nontechnical_deck_focus": LocalBriefingProfile(
        name="nontechnical_deck_focus",
        description="Nontechnical deck odakli profil.",
        max_slide_items=80,
        notes="Teknik olmayan paydaslar icin briefing deck source ve anlati sadelestirme odakli profil."
    ),
    "strict_communication_safety": LocalBriefingProfile(
        name="strict_communication_safety",
        description="Strict safety profil.",
        max_sections=3000,
        max_slide_items=100,
        min_quality_score=0.60,
        notes="Yatirim tavsiyesi, canli trading, broker readiness, production release ve official decision iddialarini siki denetleyen profil."
    )
}

def get_local_briefing_profile(name: str) -> LocalBriefingProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_briefing_profiles(enabled_only: bool = True) -> list[LocalBriefingProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_briefing_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olmamali.")
        if p.max_sections <= 0:
            raise ConfigError("max_sections pozitif olmali.")
        if p.max_slide_items <= 0:
            raise ConfigError("max_slide_items pozitif olmali.")
        if not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if any([
            p.allow_investment_advice, p.allow_live_trading_claim,
            p.allow_broker_readiness_claim, p.allow_production_release_claim,
            p.allow_model_deployment_claim, p.allow_official_board_decision_claim,
            p.allow_cloud_upload, p.allow_external_service, p.allow_external_llm,
            p.allow_file_modification, p.allow_file_deletion, p.allow_file_move,
            p.allow_overwrite
        ]):
            raise ConfigError("advice/live/broker/production/deployment/official/cloud/external/file action flagleri False olmali.")

def get_default_local_briefing_profile() -> LocalBriefingProfile:
    return PROFILES["balanced_local_briefing"]
''')

write_file('local_briefing/briefing_labels.py', '''
class LabelError(Exception):
    pass

AUDIENCE_LABELS = [
    "executive_audience", "business_stakeholder_audience", "analyst_audience",
    "operator_audience", "developer_audience", "compliance_reviewer_audience",
    "nontechnical_audience", "unknown_audience"
]

SECTION_LABELS = [
    "project_overview_section", "capability_section", "architecture_section",
    "milestone_section", "boundary_section", "risk_limitation_section",
    "decision_context_section", "operating_model_section", "next_steps_section",
    "faq_section", "unknown_section"
]

STATUS_LABELS = [
    "communication_ready", "communication_ready_with_warnings", "communication_missing",
    "communication_blocked_by_safety", "communication_needs_manual_review", "communication_unknown"
]

DECISION_LABELS = [
    "decision_context_informational", "decision_context_manual_review",
    "decision_context_no_go_related", "decision_context_safe_next_step", "decision_context_unknown"
]

RISK_LABELS = [
    "communication_critical_risk", "communication_high_risk", "communication_medium_risk",
    "communication_low_risk", "communication_info", "communication_unknown_risk"
]

def list_audience_labels() -> list[str]: return AUDIENCE_LABELS
def list_briefing_section_labels() -> list[str]: return SECTION_LABELS
def list_communication_status_labels() -> list[str]: return STATUS_LABELS
def list_decision_context_labels() -> list[str]: return DECISION_LABELS
def list_communication_risk_labels() -> list[str]: return RISK_LABELS

def validate_audience_label(label: str) -> None:
    if label not in AUDIENCE_LABELS:
        raise LabelError(f"Invalid audience label: {label}")
def validate_briefing_section_label(label: str) -> None:
    if label not in SECTION_LABELS:
        raise LabelError(f"Invalid section label: {label}")
def validate_communication_status(label: str) -> None:
    if label not in STATUS_LABELS:
        raise LabelError(f"Invalid status label: {label}")
def validate_decision_context_label(label: str) -> None:
    if label not in DECISION_LABELS:
        raise LabelError(f"Invalid decision label: {label}")
def validate_communication_risk(label: str) -> None:
    if label not in RISK_LABELS:
        raise LabelError(f"Invalid risk label: {label}")
''')

write_file('local_briefing/briefing_models.py', '''
import hashlib
from dataclasses import dataclass, asdict

@dataclass
class StakeholderAudience:
    audience_id: str
    audience_label: str
    audience_name: str
    information_needs: list[str]
    forbidden_framings: list[str]
    warnings: list[str]

@dataclass
class BriefingSection:
    section_id: str
    section_label: str
    title: str
    audience_label: str
    summary: str
    key_points: list[str]
    warnings: list[str]

@dataclass
class DeckSlideSource:
    slide_id: str
    slide_number: int
    title: str
    audience_label: str
    bullets: list[str]
    speaker_notes: str
    safety_notes: list[str]

@dataclass
class DecisionQuestion:
    question_id: str
    question: str
    context_label: str
    evidence_sources: list[str]
    safe_response: str
    warnings: list[str]

@dataclass
class CommunicationFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_audience_id(audience_label: str) -> str:
    return hashlib.md5(audience_label.encode()).hexdigest()[:8]

def build_briefing_section_id(section_label: str, title: str, audience_label: str) -> str:
    s = f"{section_label}_{title}_{audience_label}"
    return hashlib.md5(s.encode()).hexdigest()[:8]

def build_deck_slide_id(slide_number: int, title: str) -> str:
    s = f"{slide_number}_{title}"
    return hashlib.md5(s.encode()).hexdigest()[:8]

def build_decision_question_id(question: str) -> str:
    return hashlib.md5(question.encode()).hexdigest()[:8]

def build_communication_finding_id(title: str) -> str:
    return hashlib.md5(title.encode()).hexdigest()[:8]

def stakeholder_audience_to_dict(item: StakeholderAudience) -> dict: return asdict(item)
def briefing_section_to_dict(item: BriefingSection) -> dict: return asdict(item)
def deck_slide_source_to_dict(item: DeckSlideSource) -> dict: return asdict(item)
def decision_question_to_dict(item: DecisionQuestion) -> dict: return asdict(item)
def communication_finding_to_dict(item: CommunicationFinding) -> dict: return asdict(item)
''')

write_file('local_briefing/audience_registry.py', '''
import pandas as pd
from .briefing_config import LocalBriefingProfile
from .briefing_models import StakeholderAudience, build_audience_id

def build_default_audiences(profile: LocalBriefingProfile) -> list[StakeholderAudience]:
    return [
        StakeholderAudience(
            audience_id=build_audience_id("executive_audience"),
            audience_label="executive_audience",
            audience_name="Executive",
            information_needs=["amac", "kapsam", "sinirliliklar", "karar baglami", "sonraki adimlar"],
            forbidden_framings=["yatirim komitesi onayina hazir", "canli trading onayli", "garanti getiri"],
            warnings=["Bu grup investment committee anlamina gelmez."]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("business_stakeholder_audience"),
            audience_label="business_stakeholder_audience",
            audience_name="Business Stakeholder",
            information_needs=["platform ne yapar/ne yapmaz", "rapor turleri", "guvenlik sinirlari"],
            forbidden_framings=["production release onayli", "broker bagli"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("analyst_audience"),
            audience_label="analyst_audience",
            audience_name="Analyst",
            information_needs=["rapor okuma", "evidence", "metadata", "non-use policy"],
            forbidden_framings=["kesin AL/SAT sinyali", "yatirim tavsiyesi"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("operator_audience"),
            audience_label="operator_audience",
            audience_name="Operator",
            information_needs=["safe commands", "status outputs", "manual review"],
            forbidden_framings=["otomatik canli operasyon baslatilabilir"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("developer_audience"),
            audience_label="developer_audience",
            audience_name="Developer",
            information_needs=["mimari", "moduller", "test ve script contract"],
            forbidden_framings=["deployment onayi verildi"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("compliance_reviewer_audience"),
            audience_label="compliance_reviewer_audience",
            audience_name="Compliance Reviewer",
            information_needs=["non-use", "secret exclusion", "safety boundaries"],
            forbidden_framings=["resmi compliance raporudur"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("nontechnical_audience"),
            audience_label="nontechnical_audience",
            audience_name="Nontechnical",
            information_needs=["sade anlatim", "terim sozlugu", "risk/sinirlilik"],
            forbidden_framings=["kesin kazanc"],
            warnings=[]
        )
    ]

def build_stakeholder_audience_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    audiences = build_default_audiences(profile)
    df = pd.DataFrame([vars(a) for a in audiences])
    summary = summarize_audiences(df)
    return df, summary

def summarize_audiences(audience_df: pd.DataFrame) -> dict:
    if audience_df is None or audience_df.empty:
        return {"total_audiences": 0}
    return {
        "total_audiences": len(audience_df),
        "audiences": audience_df["audience_name"].tolist()
    }
''')
