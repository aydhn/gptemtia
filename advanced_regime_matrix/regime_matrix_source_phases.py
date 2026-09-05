"""Phase 127: Regime Matrix Source Phases Registry.

Maps upstream feature/factor/context source phases feeding the regime matrix.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

SOURCE_PHASES: List[Dict[str, Any]] = [
    {
        "phase_number": 117,
        "phase_name": "Technical Indicator Expansion",
        "module_name": "advanced_technical_indicators",
        "contribution": "Core technical indicators across trend, momentum, volatility, and range.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 118,
        "phase_name": "Multi-Window Feature Grid",
        "module_name": "advanced_feature_grid",
        "contribution": "Multi-timeframe rolling windows and standardized returns.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 119,
        "phase_name": "Cross-Asset Feature Alignment",
        "module_name": "advanced_cross_asset_alignment",
        "contribution": "Intermarket coupling and synchronized multi-asset observations.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 120,
        "phase_name": "Macro/Calendar/News Feature Fusion",
        "module_name": "advanced_feature_fusion",
        "contribution": "Macroeconomic time series, release windows, and metadata-only news tags.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 121,
        "phase_name": "Feature Validation and No-Lookahead Guard",
        "module_name": "advanced_feature_validation",
        "contribution": "Audit rules, forbidden column quarantine, and leakage prevention.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 122,
        "phase_name": "Factor Metadata and Factor Families",
        "module_name": "advanced_factor_metadata",
        "contribution": "Canonical factor family classifications and factor namespace.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 123,
        "phase_name": "Feature Quality and Drift Diagnostics",
        "module_name": "advanced_feature_quality_drift",
        "contribution": "Missingness ratios, KS/PSI drift diagnostics, and staleness checks.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 124,
        "phase_name": "Feature Store Integration Expansion",
        "module_name": "advanced_feature_store_integration",
        "contribution": "Central metadata store, partition policies, and lineage references.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 125,
        "phase_name": "Feature Store Acceptance & Factor Governance",
        "module_name": "advanced_feature_factor_acceptance",
        "contribution": "Acceptance criteria, factor governance, and pipeline verification.",
        "status": "READY",
        "non_signal": True,
    },
    {
        "phase_number": 126,
        "phase_name": "Regime Classification and Market Behavior Foundation",
        "module_name": "advanced_regime_foundation",
        "contribution": "Market behavior taxonomy, regime state taxonomy, and regime family definitions.",
        "status": "READY",
        "non_signal": True,
    },
]


def is_valid_regime_matrix_source_phase(phase: int) -> bool:
    """Check whether a phase number is a valid upstream source phase for Phase 127."""
    valid_phases = {sp["phase_number"] for sp in SOURCE_PHASES}
    return phase in valid_phases


def build_regime_matrix_source_phase_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the upstream source phases registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for sp in SOURCE_PHASES:
        sp_copy = sp.copy()
        sp_copy["current_phase"] = p.current_phase
        sp_copy["target_final_phase"] = p.target_final_phase
        sp_copy["next_phase"] = p.next_phase
        sp_copy["source_preserved"] = True
        rows.append(sp_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_source_phases(df)
    return df, summary


def summarize_regime_matrix_source_phases(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the source phases registry."""
    return {
        "total_source_phases": len(df),
        "phase_numbers": df["phase_number"].tolist() if not df.empty else [],
        "all_ready": bool((df["status"] == "READY").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty and "source_preserved" in df.columns else True,
        "status": "matrix_ready",
    }


build_regime_matrix_source_phases_registry = build_regime_matrix_source_phase_registry

