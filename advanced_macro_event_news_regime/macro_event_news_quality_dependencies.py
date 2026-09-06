"""Phase 132: Macro/Event/News Quality Dependencies Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_QUALITY_DEPENDENCIES = [
    {
        "dependency_id": "qual_dep_phase_123_quality",
        "source_phase": "Phase 123",
        "description": "Feature Quality, Drift & Stationarity Diagnostics dependency.",
        "status": "active",
        "min_score": 0.45,
    },
    {
        "dependency_id": "qual_dep_phase_124_store",
        "source_phase": "Phase 124",
        "description": "Advanced FeatureStore Integration catalog quality dependency.",
        "status": "active",
        "min_score": 0.45,
    },
    {
        "dependency_id": "qual_dep_phase_129_behavior",
        "source_phase": "Phase 129",
        "description": "Market behavior regime diagnostics quality dependency.",
        "status": "active",
        "min_score": 0.45,
    },
    {
        "dependency_id": "qual_dep_phase_130_stability",
        "source_phase": "Phase 130",
        "description": "Regime transition stability score quality dependency.",
        "status": "active",
        "min_score": 0.45,
    },
    {
        "dependency_id": "qual_dep_phase_131_cross_asset",
        "source_phase": "Phase 131",
        "description": "Cross-asset regime context score dependency.",
        "status": "active",
        "min_score": 0.45,
    },
    {
        "dependency_id": "qual_dep_macro_timestamp_quality",
        "source_phase": "Phase 132",
        "description": "Macro release timestamp quality and non-null rate.",
        "status": "active",
        "min_score": 0.50,
    },
    {
        "dependency_id": "qual_dep_calendar_completeness",
        "source_phase": "Phase 132",
        "description": "Economic calendar event importance and timing completeness.",
        "status": "active",
        "min_score": 0.50,
    },
    {
        "dependency_id": "qual_dep_news_meta_coverage",
        "source_phase": "Phase 132",
        "description": "News metadata tagging completeness and provenance verification.",
        "status": "active",
        "min_score": 0.50,
    },
    {
        "dependency_id": "qual_dep_manual_review_blockers",
        "source_phase": "Phase 132",
        "description": "Resolution of all blocking manual review items prior to Phase 133.",
        "status": "active",
        "min_score": 0.50,
    },
]


def build_macro_event_news_quality_dependency_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of quality dependencies."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_QUALITY_DEPENDENCIES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_quality_dependencies": len(df),
        "source_phases": df["source_phase"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_quality_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for quality dependencies."""
    return {
        "total_dependencies": len(df),
        "min_required_score": float(df["min_score"].min()) if "min_score" in df.columns else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
