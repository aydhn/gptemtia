"""Phase 131: Cross-Asset Regime Context Findings Registry.

Defines non-destructive diagnostic findings discovered during cross-asset context verification.
Strictly non-signal, zero destructive actions allowed.
"""

from typing import Any, Dict, List, Optional, Tuple
import uuid
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)
from advanced_cross_asset_regime_context.cross_asset_regime_models import (
    CrossAssetContextFinding,
)

SAMPLE_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "find_lead_lag_placeholder",
        "finding_type": "lead_lag_placeholder_only",
        "relationship_type": "relationship_lead_lag_placeholder",
        "severity_label": "info",
        "message": "Lead-lag records are configured as descriptive structural placeholders without predictive VAR or Granger fitting.",
        "recommendation": "Preserve structural catalog without executing predictive modeling or trade forecasting.",
        "manual_review_required": True,
    },
    {
        "finding_id": "find_news_metadata_boundary",
        "finding_type": "news_metadata_boundary_risk",
        "relationship_type": "relationship_news_metadata_context",
        "severity_label": "info",
        "message": "Verified all news metadata links operate strictly on tags and freshness without raw article content or NLP models.",
        "recommendation": "Enforce strict metadata-only policy across all multi-asset joins.",
        "manual_review_required": True,
    },
]


def create_cross_asset_context_finding(
    finding_type: str,
    relationship_type: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> CrossAssetContextFinding:
    """Factory creating a single CrossAssetContextFinding instance."""
    return CrossAssetContextFinding(
        finding_id=f"find_{uuid.uuid4().hex[:8]}",
        finding_type=finding_type,
        relationship_type=relationship_type,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
    )


def build_cross_asset_regime_context_findings_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build findings registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in SAMPLE_FINDINGS:
        row = dict(item)
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
    summary = summarize_cross_asset_context_findings(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_context_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize context findings."""
    types = df["finding_type"].value_counts().to_dict() if not df.empty else {}
    severities = df["severity_label"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_findings": len(df),
        "finding_types": types,
        "severities": severities,
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty else 0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    }
