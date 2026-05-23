class LabelError(Exception):
    pass

EVIDENCE_SOURCE_LABELS = [
    "technical_evidence",
    "strategy_evidence",
    "risk_level_evidence",
    "backtest_evidence",
    "performance_evidence",
    "validation_evidence",
    "ml_evidence",
    "paper_evidence",
    "research_report_evidence",
    "synthetic_index_evidence",
    "portfolio_evidence",
    "regime_evidence",
    "factor_evidence",
    "quality_evidence",
    "unknown_evidence"
]

EVIDENCE_DIRECTION_LABELS = [
    "supportive_evidence",
    "conflicting_evidence",
    "neutral_evidence",
    "uncertain_evidence",
    "missing_evidence",
    "unknown_evidence_direction"
]

CONSENSUS_LABELS = [
    "strong_positive_consensus",
    "moderate_positive_consensus",
    "neutral_consensus",
    "mixed_consensus",
    "moderate_negative_consensus",
    "strong_negative_consensus",
    "insufficient_consensus_data",
    "unknown_consensus"
]

CONFIDENCE_LABELS = [
    "high_confidence_research",
    "medium_confidence_research",
    "low_confidence_research",
    "unreliable_research",
    "unknown_confidence"
]

def list_evidence_source_labels() -> list[str]:
    return EVIDENCE_SOURCE_LABELS

def list_evidence_direction_labels() -> list[str]:
    return EVIDENCE_DIRECTION_LABELS

def list_consensus_labels() -> list[str]:
    return CONSENSUS_LABELS

def list_confidence_labels() -> list[str]:
    return CONFIDENCE_LABELS

def validate_evidence_source(label: str) -> None:
    if label not in EVIDENCE_SOURCE_LABELS:
        raise LabelError(f"Invalid evidence source label: {label}")

def validate_evidence_direction(label: str) -> None:
    if label not in EVIDENCE_DIRECTION_LABELS:
        raise LabelError(f"Invalid evidence direction label: {label}")

def validate_consensus_label(label: str) -> None:
    if label not in CONSENSUS_LABELS:
        raise LabelError(f"Invalid consensus label: {label}")

def validate_confidence_label(label: str) -> None:
    if label not in CONFIDENCE_LABELS:
        raise LabelError(f"Invalid confidence label: {label}")
