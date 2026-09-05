from dataclasses import dataclass, asdict

@dataclass
class AdvancedRoadmapItem:
    roadmap_id: str
    phase_start: int
    phase_end: int
    track_label: str
    title: str
    description: str
    expected_outputs: list[str]
    safety_notes: list[str]

@dataclass
class PhasePlanItem:
    phase: int
    title: str
    objective: str
    track_label: str
    depends_on: list[int]
    expected_outputs: list[str]
    forbidden_outputs: list[str]
    manual_review_required: bool

@dataclass
class PhaseOutputAuditItem:
    audit_id: str
    phase_range: str
    output_area: str
    expected_presence: str
    current_status: str
    gap_note: str
    manual_review_required: bool

@dataclass
class MvpAdvancedGapItem:
    gap_id: str
    gap_area: str
    current_state: str
    target_state: str
    target_phase_range: str
    priority: str
    risk_label: str
    recommendation: str

@dataclass
class FunctionalContinuationItem:
    continuation_id: str
    module_area: str
    current_module_ref: str
    advanced_target_ref: str
    continuation_status: str
    notes: str

@dataclass
class ContinuationFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_roadmap_id(phase_start: int, phase_end: int, track_label: str) -> str:
    return f"ROADMAP-{phase_start}-{phase_end}-{track_label}"

def build_phase_plan_id(phase: int) -> str:
    return f"PHASE-{phase}"

def build_phase_output_audit_id(phase_range: str, output_area: str) -> str:
    return f"AUDIT-{phase_range}-{output_area}".replace(" ", "_").upper()

def build_mvp_gap_id(gap_area: str, target_phase_range: str) -> str:
    return f"GAP-{gap_area}-{target_phase_range}".replace(" ", "_").upper()

def build_functional_continuation_id(module_area: str, advanced_target_ref: str) -> str:
    return f"CONT-{module_area}-{advanced_target_ref}".replace(" ", "_").upper()

def build_continuation_finding_id(title: str) -> str:
    return f"FINDING-{title}".replace(" ", "_").upper()
