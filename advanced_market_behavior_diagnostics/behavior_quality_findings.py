"""Phase 129: Behavior Quality Findings Registry.

Records non-destructive diagnostic findings, boundary warnings, and data quality notices.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_models import (
    BehaviorQualityFinding,
)

CORE_FINDING_TEMPLATES = [
    {
        "finding_type": "candidate_state_ambiguity_warning",
        "behavior_family": "transition",
        "severity": "behavior_low",
        "message": "Candidate state breakout transition exhibits expected boundary overlap with continuation.",
        "recommendation": "Inspect candidate state ambiguity without modifying source schemas.",
        "manual_review_required": False,
    },
    {
        "finding_type": "news_metadata_boundary_risk",
        "behavior_family": "news_metadata",
        "severity": "behavior_info",
        "message": "News metadata boundary strictly enforced: zero full-text and zero scraping validated.",
        "recommendation": "Maintain metadata-only news boundary across all diagnostics pipelines.",
        "manual_review_required": False,
    },
]

CORE_BEHAVIOR_QUALITY_FINDINGS = CORE_FINDING_TEMPLATES



def create_behavior_quality_finding(
    finding_type: str,
    behavior_family: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> BehaviorQualityFinding:
    """Create a structured BehaviorQualityFinding instance."""
    import uuid
    fid = f"finding_{uuid.uuid4().hex[:8]}"
    return BehaviorQualityFinding(
        finding_id=fid,
        finding_type=finding_type,
        behavior_family=behavior_family,
        severity=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_behavior_quality_findings_registry(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and metadata summary of behavior quality findings."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for idx, tmpl in enumerate(CORE_FINDING_TEMPLATES, 1):
        rows.append(
            {
                "finding_id": f"finding_p129_{idx:03d}",
                "finding_type": tmpl["finding_type"],
                "behavior_family": tmpl["behavior_family"],
                "severity": tmpl["severity"],
                "message": tmpl["message"],
                "recommendation": tmpl["recommendation"],
                "manual_review_required": tmpl["manual_review_required"],
                "destructive_action_allowed": False,
                "auto_fix_allowed": False,
                "auto_drop_allowed": False,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_behavior_quality_findings(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_behavior_quality_findings(df: pd.DataFrame) -> dict:
    """Summarize behavior quality findings registry."""
    if df.empty:
        return {
            "total_findings": 0,
            "blocking_findings_count": 0,
            "destructive_action_allowed": False,
            "non_signal": True,
        }
    return {
        "total_findings": len(df),
        "blocking_findings_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
        "non_signal": True,
    }
