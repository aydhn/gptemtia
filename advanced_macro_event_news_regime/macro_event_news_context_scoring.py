"""Phase 132: Macro/Event/News Context Scoring and Diagnostics Report."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.macro_event_news_context_findings import (
    build_macro_event_news_context_findings_registry,
)
from advanced_macro_event_news_regime.macro_event_news_regime_models import (
    MacroEventNewsContextScore,
)


def classify_macro_event_news_context_score(
    score: float,
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> str:
    """Classify numeric context score into descriptive diagnostic tier."""
    p = profile or get_macro_event_news_regime_profile()
    if score >= 0.85:
        return "high_context_integrity"
    elif score >= p.min_context_score:
        return "acceptable_context_integrity"
    elif score >= 0.30:
        return "marginal_context_integrity"
    else:
        return "critical_context_flaw"


def calculate_macro_event_news_context_score(
    findings_df: pd.DataFrame,
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> MacroEventNewsContextScore:
    """Compute context integrity score from findings without trading signal implication."""
    p = profile or get_macro_event_news_regime_profile()
    base_score = 1.0

    if findings_df.empty:
        return MacroEventNewsContextScore(
            context_score=base_score,
            classification=classify_macro_event_news_context_score(base_score, p),
            total_findings=0,
            blocker_count=0,
            warning_count=0,
            manual_review_count=0,
            non_signal=True,
            source_preserved=True,
            official_approval=False,
            production_ready=False,
            broker_ready=False,
        )

    blockers = int((findings_df["severity_label"] == "blocker").sum()) if "severity_label" in findings_df.columns else 0
    warnings = int((findings_df["severity_label"] == "warning").sum()) if "severity_label" in findings_df.columns else 0
    manual_reviews = int(findings_df["manual_review_required"].sum()) if "manual_review_required" in findings_df.columns else 0

    penalty = (blockers * 0.35) + (warnings * 0.10) + (manual_reviews * 0.02)
    score = max(0.0, min(1.0, round(base_score - penalty, 4)))

    return MacroEventNewsContextScore(
        context_score=score,
        classification=classify_macro_event_news_context_score(score, p),
        total_findings=len(findings_df),
        blocker_count=blockers,
        warning_count=warnings,
        manual_review_count=manual_reviews,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
    )


def build_macro_event_news_context_score_report(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build score report DataFrame and summary dictionary."""
    p = profile or get_macro_event_news_regime_profile()
    f_df, _ = build_macro_event_news_context_findings_registry(p)
    scored = calculate_macro_event_news_context_score(f_df, p)

    row = {
        "profile_name": p.profile_name,
        "context_score": scored.context_score,
        "classification": scored.classification,
        "total_findings": scored.total_findings,
        "blocker_count": scored.blocker_count,
        "warning_count": scored.warning_count,
        "manual_review_count": scored.manual_review_count,
        "min_required_score": p.min_context_score,
        "meets_threshold": scored.context_score >= p.min_context_score,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    df = pd.DataFrame([row])
    summary = {
        "context_score": scored.context_score,
        "classification": scored.classification,
        "meets_threshold": scored.context_score >= p.min_context_score,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_context_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for context score DataFrame."""
    return {
        "total_scores": len(df),
        "mean_score": float(df["context_score"].mean()) if "context_score" in df.columns else 0.0,
        "meets_threshold_all": bool(df["meets_threshold"].all()) if "meets_threshold" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
