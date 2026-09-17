# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Dependency Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

DEPENDENCIES: List[Dict[str, Any]] = [
    {"dep_id": "DEP-146", "phase_ref": "Phase 146", "source": "advanced_realistic_backtest", "requirement": "Realistic backtest and cost/slippage contracts", "satisfied": True},
    {"dep_id": "DEP-147", "phase_ref": "Phase 147", "source": "advanced_walk_forward_validation", "requirement": "Walk-forward and OOS split contracts", "satisfied": True},
    {"dep_id": "DEP-148", "phase_ref": "Phase 148", "source": "advanced_stress_testing", "requirement": "Stress testing and scenario simulation contracts", "satisfied": True},
    {"dep_id": "DEP-149", "phase_ref": "Phase 149", "source": "advanced_monte_carlo_robustness", "requirement": "Monte Carlo robustness and stability contracts", "satisfied": True},
    {"dep_id": "DEP-150", "phase_ref": "Phase 150", "source": "advanced_backtest_governance", "requirement": "Backtest governance and bias control contracts", "satisfied": True},
    {"dep_id": "DEP-151", "phase_ref": "Phase 151", "source": "advanced_benchmark_evaluation", "requirement": "Benchmark comparison and strategy evaluation contracts", "satisfied": True},
    {"dep_id": "DEP-145", "phase_ref": "Phase 145", "source": "advanced_ml_acceptance", "requirement": "Consolidated Advanced ML block acceptance", "satisfied": True},
    {"dep_id": "DEP-144", "phase_ref": "Phase 144", "source": "advanced_model_governance", "requirement": "Model governance and model card contracts", "satisfied": True},
    {"dep_id": "DEP-137", "phase_ref": "Phase 137", "source": "advanced_ml_dataset_registry", "requirement": "Dataset contracts and split registry", "satisfied": True},
    {"dep_id": "DEP-134", "phase_ref": "Phase 134", "source": "ml.feature_store", "requirement": "FeatureStore contracts and metadata catalog", "satisfied": True},
    {"dep_id": "DEP-135", "phase_ref": "Phase 135", "source": "advanced_regime_acceptance", "requirement": "Regime classification block acceptance", "satisfied": True},
]


def build_backtest_acceptance_dependency_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Backtest acceptance dependencies."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for dep in DEPENDENCIES:
        records.append({
            "dep_id": dep["dep_id"],
            "phase_ref": dep["phase_ref"],
            "source": dep["source"],
            "requirement": dep["requirement"],
            "satisfied": dep["satisfied"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": DEPENDENCY_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "total_dependencies": len(records),
        "satisfied_dependencies": len([r for r in records if r["satisfied"]]),
        "all_satisfied": all(r["satisfied"] for r in records),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
