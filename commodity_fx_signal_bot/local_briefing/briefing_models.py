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
