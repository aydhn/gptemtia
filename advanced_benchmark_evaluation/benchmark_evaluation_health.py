# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Health Check Module.

Validates the presence and operational integrity of all upstream blocks,
modules, directories, and data lake/feature store components.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_HEALTH_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

HEALTH_CHECKS: List[Dict[str, Any]] = [
    {
        "check_id": "HEALTH_01_BACKTEST_GOVERNANCE",
        "component": "advanced_backtest_governance",
        "description": "Phase 150 Backtest Governance and Bias Control package availability",
    },
    {
        "check_id": "HEALTH_02_MONTE_CARLO",
        "component": "advanced_monte_carlo_robustness",
        "description": "Phase 149 Monte Carlo Robustness and Parameter Stability package availability",
    },
    {
        "check_id": "HEALTH_03_STRESS_TESTING",
        "component": "advanced_stress_testing",
        "description": "Phase 148 Stress Testing and Scenario Simulation package availability",
    },
    {
        "check_id": "HEALTH_04_WALK_FORWARD",
        "component": "advanced_walk_forward_validation",
        "description": "Phase 147 Walk-Forward Validation package availability",
    },
    {
        "check_id": "HEALTH_05_REALISTIC_BACKTEST",
        "component": "advanced_realistic_backtest",
        "description": "Phase 146 Realistic Backtest package availability",
    },
    {
        "check_id": "HEALTH_06_ML_ACCEPTANCE",
        "component": "advanced_ml_acceptance",
        "description": "Phase 145 Advanced ML Acceptance package availability",
    },
    {
        "check_id": "HEALTH_07_MODEL_GOVERNANCE",
        "component": "advanced_model_governance",
        "description": "Phase 144 Model Governance package availability",
    },
    {
        "check_id": "HEALTH_08_REGIME_ACCEPTANCE",
        "component": "advanced_regime_acceptance",
        "description": "Phase 135 Regime Acceptance package availability",
    },
    {
        "check_id": "HEALTH_09_FEATURESTORE",
        "component": "ml.feature_store",
        "description": "FeatureStore v2 metadata catalog availability",
    },
    {
        "check_id": "HEALTH_10_DATALAKE",
        "component": "data.storage.data_lake",
        "description": "DataLake storage subsystem availability",
    },
    {
        "check_id": "HEALTH_11_BENCHMARK_EVALUATION",
        "component": "advanced_benchmark_evaluation",
        "description": "Phase 151 Benchmark Evaluation package availability",
    },
]


def build_benchmark_evaluation_health_check(
    project_root: Path | None = None,
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute health checks across all required components."""
    root = project_root or Path(__file__).resolve().parent.parent
    rows: List[Dict[str, Any]] = []

    for check in HEALTH_CHECKS:
        comp = check["component"]
        # Determine existence
        if comp.startswith("ml."):
            exists = (root / "ml" / "feature_store.py").exists()
        elif comp.startswith("data."):
            exists = (root / "data" / "storage" / "data_lake.py").exists()
        else:
            exists = (root / comp).is_dir()

        status = "HEALTHY" if exists else "UNHEALTHY"
        rows.append(
            {
                "check_id": check["check_id"],
                "component": comp,
                "description": check["description"],
                "status": status,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    all_healthy = bool((df["status"] == "HEALTHY").all()) if not df.empty else True

    summary = {
        "domain": LABEL_HEALTH_DOMAIN,
        "total_checks": len(df),
        "healthy_count": int((df["status"] == "HEALTHY").sum()),
        "all_healthy": all_healthy,
        "status": STATUS_EVALUATION_CONTRACT_READY if all_healthy else "HEALTH_CHECK_FAILED",
        "non_signal": True,
    }
    return df, summary
