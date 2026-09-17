# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Lineage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

LINEAGE_STAGES: List[Dict[str, Any]] = [
    {
        "stage": "Phase 116-125 Feature & Factor Engine",
        "component": "FeatureStore & Quality Drift",
        "description": "Deterministic time-series indicators, factor metadata, and quality boundaries.",
    },
    {
        "stage": "Phase 126-135 Market Regime Context",
        "component": "Regime Classification Acceptance",
        "description": "Unsupervised market behavior context and regime state acceptance.",
    },
    {
        "stage": "Phase 136 ML Runtime Foundation",
        "component": "Hardware Discovery & Runtime",
        "description": "Hardware discovery, CUDA/Torch capability mapping, and non-execution safety.",
    },
    {
        "stage": "Phase 137 ML Dataset Contracts",
        "component": "Dataset Registry & Snapshot Governance",
        "description": "Temporal partition contracts, feature snapshot governance, and experiment registry.",
    },
    {
        "stage": "Phase 138 Baseline ML Model Contracts",
        "component": "Baseline Models & Dry-Run Harness",
        "description": "Linear, Tree, and MLP baseline model contracts with dry-run training stubs.",
    },
    {
        "stage": "Phase 139 GPU Resource Governance",
        "component": "Controlled Dry-Run Resource Layer",
        "description": "Device selection, memory budgeting, and timeout policies.",
    },
    {
        "stage": "Phase 140 Ensemble Model Contracts",
        "component": "Candidate Model Registry & Ensemble Contracts",
        "description": "Candidate model families, compatibility matrix, and non-executing ensemble contracts.",
    },
    {
        "stage": "Phase 141 Calibration & Uncertainty",
        "component": "Probability Calibration & Uncertainty Contracts",
        "description": "Probability calibration contracts, uncertainty estimation contracts, quality gates, and drift handoff.",
    },
]


def build_calibration_uncertainty_lineage_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration and uncertainty lineage."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in LINEAGE_STAGES:
        rows.append(
            {
                "stage": item["stage"],
                "component": item["component"],
                "description": item["description"],
                "non_signal": True,
                "verified": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_lineage(df)
    return df, summary


def summarize_calibration_uncertainty_lineage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration and uncertainty lineage DataFrame."""
    return {
        "total_lineage_stages": len(df),
        "stages": df["stage"].tolist() if not df.empty else [],
        "all_verified": bool(df["verified"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
