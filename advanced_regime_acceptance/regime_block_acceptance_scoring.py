"""Phase 135: Regime Block Acceptance Scoring.

Computes normalized acceptance scores across all evaluated gates.
Explicitly guarantees that the score is a governance metric, not a signal or approval.
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
    REGIME_BLOCK_ACCEPTANCE_SCORE_DOMAIN,
)
from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
)


def classify_regime_block_acceptance_score(score: float) -> str:
    """Classify an acceptance score into standard status label."""
    if score >= 0.90:
        return ACCEPTANCE_PASS
    elif score >= 0.60:
        return ACCEPTANCE_PASS_WITH_WARNINGS
    return ACCEPTANCE_FAIL


def calculate_regime_block_acceptance_score(
    gates_df: pd.DataFrame,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> float:
    """Calculate composite acceptance score between 0.0 and 1.0."""
    if gates_df.empty:
        return 0.0
    passed = int(gates_df["passed"].sum())
    total = len(gates_df)
    return float(round(passed / total, 4)) if total > 0 else 0.0


def build_regime_block_acceptance_score_report(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for acceptance score."""
    active = profile or get_regime_acceptance_profile()
    gates_df, _ = build_regime_block_acceptance_gate_registry(active)
    score = calculate_regime_block_acceptance_score(gates_df, active)
    classification = classify_regime_block_acceptance_score(score)

    row = {
        "score_id": "regime_block_acceptance_score",
        "total_gates": len(gates_df),
        "passed_gates": int(gates_df["passed"].sum()),
        "acceptance_score": score,
        "classification": classification,
        "min_required_score": active.min_score,
        "is_acceptable": bool(score >= active.min_score),
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "model_training_ready": False,
    }
    df = pd.DataFrame([row])
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_ACCEPTANCE_SCORE_DOMAIN,
        "active_profile": active.profile_name,
        "acceptance_score": score,
        "classification": classification,
        "is_acceptable": bool(score >= active.min_score),
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "model_training_ready": False,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_acceptance_score(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize acceptance score DataFrame."""
    if df.empty:
        return {"acceptance_score": 0.0, "classification": ACCEPTANCE_FAIL, "non_signal": True}
    row = df.iloc[0]
    return {
        "acceptance_score": float(row.get("acceptance_score", 0.0)),
        "classification": str(row.get("classification", ACCEPTANCE_FAIL)),
        "is_acceptable": bool(row.get("is_acceptable", False)),
        "non_signal": True,
    }
