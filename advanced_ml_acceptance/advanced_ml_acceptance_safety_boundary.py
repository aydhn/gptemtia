# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Safety Boundary Specifications."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    SAFETY_DOMAIN,
    ACCEPTANCE_READY,
)

NO_GO_CONDITIONS: List[str] = [
    "live trading",
    "broker integration",
    "real order",
    "investment advice",
    "signal generation",
    "directional certainty",
    "dataset materialization",
    "feature snapshot materialization",
    "strategy/backtest/walk-forward/benchmark/transaction-cost/slippage/optimizer execution",
    "real model training/model fit/model predict/model inference/model transform",
    "probability prediction",
    "calibration execution",
    "uncertainty estimation",
    "drift calculation",
    "explainability calculation",
    "feature attribution calculation",
    "target/label/prediction",
    "metric calculation/performance claim",
    "model artifact persistence",
    "model registry write",
    "model deployment",
    "production deployment",
    "production approval",
    "broker-ready approval",
    "live-trading approval",
    "release approval",
    "official approval",
    "real audit log",
    "full article/article body/raw content/scraped HTML usage",
    "embedding/vector generation",
    "source overwrite/destructive cleaning",
    "auto-imputation/auto-feature-drop",
    "scraping",
    "credential output",
]

SAFE_GO_CONDITIONS: List[str] = [
    "local/offline Advanced ML acceptance report generation",
    "Phase 136-144 component contract completeness checks",
    "non-production readiness score",
    "manual review queue",
    "blocker/gap/warning registry",
    "validation evidence summary",
    "safety boundary summary",
    "Phase 146 realistic backtest contract handoff",
]


def build_advanced_ml_acceptance_no_go_conditions(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> List[str]:
    """Return all strictly prohibited actions for Phase 145."""
    return list(NO_GO_CONDITIONS)


def build_advanced_ml_acceptance_safe_go_conditions(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> List[str]:
    """Return all permitted actions for Phase 145."""
    return list(SAFE_GO_CONDITIONS)


def build_advanced_ml_acceptance_safety_boundary(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for safety boundary specifications."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for cond in NO_GO_CONDITIONS:
        records.append({
            "condition": cond,
            "category": "NO_GO",
            "enforced": True,
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
        })
    for cond in SAFE_GO_CONDITIONS:
        records.append({
            "condition": cond,
            "category": "SAFE_GO",
            "enforced": True,
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": SAFETY_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_conditions": len(df),
        "no_go_count": len(NO_GO_CONDITIONS),
        "safe_go_count": len(SAFE_GO_CONDITIONS),
        "non_signal": True,
        "status": "SECURE",
    }
    return df, summary


def summarize_advanced_ml_acceptance_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    return {
        "condition_count": len(df),
        "no_go_count": int((df["category"] == "NO_GO").sum()) if not df.empty and "category" in df.columns else len(NO_GO_CONDITIONS),
        "safe_go_count": int((df["category"] == "SAFE_GO").sum()) if not df.empty and "category" in df.columns else len(SAFE_GO_CONDITIONS),
        "non_signal": True,
    }
