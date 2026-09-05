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