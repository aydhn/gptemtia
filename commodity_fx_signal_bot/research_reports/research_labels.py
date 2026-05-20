# Type Labels
RESEARCH_REPORT_TYPES = [
    "symbol_research",
    "universe_research",
    "daily_digest",
    "ranking_report",
    "technical_report",
    "backtest_report",
    "performance_report",
    "validation_report",
    "ml_report",
    "paper_report",
    "quality_report",
    "unknown_research_report"
]

# Tone Labels
RESEARCH_TONE_LABELS = [
    "neutral_research",
    "constructive_research",
    "cautionary_research",
    "insufficient_data_research",
    "unknown_research_tone"
]

# Finding Labels
RESEARCH_FINDING_LABELS = [
    "supportive_context",
    "conflicting_context",
    "neutral_context",
    "uncertain_context",
    "insufficient_data",
    "quality_warning",
    "critical_quality_warning",
    "unknown_finding"
]

# Status Labels
RESEARCH_STATUS_LABELS = [
    "research_report_ready",
    "research_report_warning",
    "research_report_rejected",
    "research_report_insufficient_data",
    "research_report_unknown"
]

def list_research_report_type_labels() -> list[str]:
    return RESEARCH_REPORT_TYPES.copy()

def list_research_tone_labels() -> list[str]:
    return RESEARCH_TONE_LABELS.copy()

def list_research_finding_labels() -> list[str]:
    return RESEARCH_FINDING_LABELS.copy()

def list_research_status_labels() -> list[str]:
    return RESEARCH_STATUS_LABELS.copy()

def validate_research_report_type(label: str) -> None:
    if label not in RESEARCH_REPORT_TYPES:
        raise ValueError(f"Invalid research report type label: {label}")

def validate_research_tone(label: str) -> None:
    if label not in RESEARCH_TONE_LABELS:
        raise ValueError(f"Invalid research tone label: {label}")

def validate_research_finding(label: str) -> None:
    if label not in RESEARCH_FINDING_LABELS:
        raise ValueError(f"Invalid research finding label: {label}")

def validate_research_status(label: str) -> None:
    if label not in RESEARCH_STATUS_LABELS:
        raise ValueError(f"Invalid research status label: {label}")
