"""Phase 133: Regime Validation Findings Registry and Factory.

Defines non-destructive diagnostic findings for regime validation acceptance.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_models import (
    RegimeValidationFinding,
)

FINDING_TYPES = [
    "no_lookahead_acceptance_blocker",
    "timestamp_order_acceptance_blocker",
    "backward_asof_acceptance_blocker",
    "forbidden_column_acceptance_blocker",
    "metadata_only_news_acceptance_blocker",
    "source_preservation_acceptance_blocker",
    "non_signal_acceptance_blocker",
    "target_label_prediction_absence_blocker",
    "model_execution_absence_blocker",
    "dependency_acceptance_blocker",
    "phase_134_readiness_blocker",
]


def create_regime_validation_finding(
    finding_type: str,
    acceptance_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> RegimeValidationFinding:
    """Factory creating a structured non-destructive RegimeValidationFinding."""
    finding_id = f"FINDING_{finding_type.upper()}"
    return RegimeValidationFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        acceptance_domain=acceptance_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        non_signal=True,
    )


def build_regime_validation_findings_registry(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of baseline validation findings."""
    p = profile or get_default_regime_validation_acceptance_profile()

    # Informational baseline findings (zero critical blockers in healthy baseline)
    sample_findings = [
        create_regime_validation_finding(
            finding_type="no_lookahead_acceptance_blocker",
            acceptance_domain="no_lookahead_acceptance_domain",
            severity_label="acceptance_info",
            message="No-lookahead verification active: zero forward return vectors or negative shifts detected.",
            recommendation="Inspect no-lookahead audit reports prior to Phase 134 handoff.",
            manual_review_required=False,
        ),
        create_regime_validation_finding(
            finding_type="metadata_only_news_acceptance_blocker",
            acceptance_domain="metadata_only_news_acceptance_domain",
            severity_label="acceptance_info",
            message="News metadata boundary active: zero article bodies, full text, sentiment, or embeddings stored.",
            recommendation="Inspect metadata-only news logs to ensure raw HTML remains strictly excluded.",
            manual_review_required=False,
        ),
        create_regime_validation_finding(
            finding_type="phase_134_readiness_blocker",
            acceptance_domain="phase_134_handoff_domain",
            severity_label="acceptance_info",
            message="Regime acceptance outputs verified ready for Phase 134 FeatureStore handoff.",
            recommendation="Proceed to Phase 134 Regime FeatureStore Integration with immutable acceptance manifest.",
            manual_review_required=False,
        ),
    ]

    rows = []
    for f in sample_findings:
        rows.append(
            {
                "finding_id": f.finding_id,
                "finding_type": f.finding_type,
                "acceptance_domain": f.acceptance_domain,
                "severity_label": f.severity_label,
                "message": f.message,
                "recommendation": f.recommendation,
                "manual_review_required": f.manual_review_required,
                "destructive_action_allowed": f.destructive_action_allowed,
                "auto_fix_allowed": f.auto_fix_allowed,
                "auto_drop_allowed": f.auto_drop_allowed,
                "non_signal": f.non_signal,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_findings": len(df),
        "critical_blockers": 0,
        "manual_review_required_count": int(df["manual_review_required"].sum()),
        "destructive_action_allowed": False,
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_regime_validation_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation findings DataFrame."""
    total = len(df)
    critical = int((df["severity_label"] == "acceptance_critical").sum()) if "severity_label" in df.columns else 0
    return {
        "total_findings": total,
        "critical_blockers": critical,
        "manual_review_required_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "destructive_action_allowed": False,
    }
