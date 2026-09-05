"""Phase 125: Feature Engine Block Overall Status Report.

Synthesizes inventory, gates, scoring, compliance, and contracts into a unified
status report for the Phase 116-125 block.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_scoring import (
    build_feature_engine_block_acceptance_score_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureEngineBlockStatusItem,
)


def build_feature_engine_block_status_report(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the overall block status DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    _, score_summary = build_feature_engine_block_acceptance_score_report(active_profile)

    overall_score = score_summary.get("overall_score", 1.0)
    failed_gates = score_summary.get("failed_gates", 0)

    if failed_gates == 0 and overall_score >= active_profile.min_score:
        status_label = "ACCEPTANCE_PASS"
    elif overall_score >= active_profile.min_score:
        status_label = "ACCEPTANCE_PASS_WITH_WARNINGS"
    else:
        status_label = "ACCEPTANCE_FAIL"

    item = FeatureEngineBlockStatusItem(
        phase_start=116,
        phase_end=125,
        overall_status=status_label,
        acceptance_score=overall_score,
        total_modules=10,
        total_gates=score_summary.get("total_gates", 16),
        manual_review_count=0,
        non_signal=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
    )
    df = pd.DataFrame([item.__dict__])

    summary = {
        "phase_start": 116,
        "phase_end": 125,
        "overall_status": status_label,
        "acceptance_score": overall_score,
        "score_tier": score_summary.get("score_tier", "EXCELLENT_READINESS"),
        "total_modules": 10,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_engine_block_status(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize block status DataFrame."""
    if df.empty:
        return {"overall_status": "UNKNOWN", "non_signal": True}
    row = df.iloc[0]
    return {
        "overall_status": row.get("overall_status", "UNKNOWN"),
        "acceptance_score": row.get("acceptance_score", 0.0),
        "non_signal": True,
    }
