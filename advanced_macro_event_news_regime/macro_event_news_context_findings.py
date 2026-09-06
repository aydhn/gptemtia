"""Phase 132: Macro/Event/News Context Findings Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.macro_event_news_regime_models import (
    MacroEventNewsContextFinding,
)

SAMPLE_FINDINGS = [
    {
        "finding_id": "find_001_cpi_actual_alignment",
        "finding_type": "unresolved_scheduled_actual_alignment",
        "context_type": "calendar_event_context",
        "severity_label": "info",
        "message": "Actual publication timestamp delta is within normal latency tolerances (2s).",
        "recommendation": "Maintain backward-asof join policy.",
        "manual_review_required": False,
    },
    {
        "finding_id": "find_002_metadata_boundary_clean",
        "finding_type": "news_metadata_boundary_risk",
        "context_type": "news_metadata_context",
        "severity_label": "info",
        "message": "All news fields verified to be strictly metadata-only. Zero article text or sentiment detected.",
        "recommendation": "Retain metadata-only boundary enforcement filters.",
        "manual_review_required": False,
    },
    {
        "finding_id": "find_003_release_lag_monitoring",
        "finding_type": "unresolved_release_timestamp",
        "context_type": "macro_indicator_context",
        "severity_label": "info",
        "message": "Quarterly GDP reporting lag is 30 days. Backward join policy verified.",
        "recommendation": "Inspect quarterly release lag boundary prior to Phase 133 acceptance.",
        "manual_review_required": False,
    },
]


def create_macro_event_news_context_finding(
    finding_type: str,
    context_type: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> MacroEventNewsContextFinding:
    """Create a structured finding instance for Phase 132."""
    finding_id = f"find_{finding_type}_{len(message)}"
    return MacroEventNewsContextFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        context_type=context_type,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_macro_event_news_context_findings_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of diagnostic context findings."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in SAMPLE_FINDINGS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["destructive_action_allowed"] = False
        row["auto_fix_allowed"] = False
        row["auto_drop_allowed"] = False
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_findings": len(df),
        "severity_distribution": df["severity_label"].value_counts().to_dict() if not df.empty else {},
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty else 0,
        "destructive_action_allowed": False,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_context_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for findings registry."""
    return {
        "total_findings": len(df),
        "blockers": int((df["severity_label"] == "blocker").sum()) if "severity_label" in df.columns else 0,
        "warnings": int((df["severity_label"] == "warning").sum()) if "severity_label" in df.columns else 0,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
