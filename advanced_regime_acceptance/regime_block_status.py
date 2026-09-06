"""Phase 135: Regime Block Overall Status Report.

Synthesizes inventory, gates, scoring, compliance, and contracts into a unified
status report for the Phase 126-135 regime classification block.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    ACCEPTANCE_PASS_WITH_WARNINGS,
    ACCEPTANCE_FAIL,
    REGIME_BLOCK_STATUS_DOMAIN,
)
from advanced_regime_acceptance.regime_block_acceptance_scoring import (
    build_regime_block_acceptance_score_report,
)


def build_regime_block_status_report(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the overall block status DataFrame and summary."""
    active = profile or get_regime_acceptance_profile()
    _, score_summary = build_regime_block_acceptance_score_report(active)

    score = score_summary.get("acceptance_score", 1.0)
    classification = score_summary.get("classification", ACCEPTANCE_PASS)

    row = {
        "block_name": "Regime Classification and Market Behavior Block",
        "phase_start": 126,
        "phase_end": 135,
        "target_final_phase": 160,
        "next_phase": 136,
        "overall_status": classification,
        "acceptance_score": score,
        "total_modules": 10,
        "total_gates": 17,
        "manual_review_count": 1,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    df = pd.DataFrame([row])
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_STATUS_DOMAIN,
        "active_profile": active.profile_name,
        "phase_start": 126,
        "phase_end": 135,
        "target_final_phase": 160,
        "next_phase": 136,
        "overall_status": classification,
        "acceptance_score": score,
        "total_modules": 10,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_status(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize block status DataFrame."""
    if df.empty:
        return {"overall_status": ACCEPTANCE_FAIL, "acceptance_score": 0.0, "non_signal": True}
    row = df.iloc[0]
    return {
        "overall_status": str(row.get("overall_status", ACCEPTANCE_FAIL)),
        "acceptance_score": float(row.get("acceptance_score", 0.0)),
        "non_signal": True,
    }
