"""Phase 126: Macro Regime Context Registry.

Registers macroeconomic context factors linking monetary, inflation, and growth environments.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

MACRO_CONTEXTS: List[Dict[str, Any]] = [
    {
        "context_id": "macro_ctx_01_inflation",
        "context_name": "inflation_context",
        "regime_family": "regime_family_macro_context",
        "description": "Inflation trajectory context tracking CPI/PPI surprises and headline vs core divergences",
        "underlying_features": "cpi_yoy_trend, ppi_momentum, inflation_surprise_index",
        "source_phases": [109, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "macro_ctx_02_rate",
        "context_name": "rate_context",
        "regime_family": "regime_family_macro_context",
        "description": "Central bank policy rate and sovereign yield curve differential context (e.g., Fed vs ECB / TCMB)",
        "underlying_features": "policy_rate_differential, 2y_yield_spread, 10y2y_curve_slope",
        "source_phases": [109, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "macro_ctx_03_growth",
        "context_name": "growth_context",
        "regime_family": "regime_family_macro_context",
        "description": "Economic growth momentum tracking manufacturing PMI, industrial production, and GDP revisions",
        "underlying_features": "pmi_composite, industrial_prod_growth, gdp_revision_trend",
        "source_phases": [109, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "macro_ctx_04_revision",
        "context_name": "macro_revision_context",
        "regime_family": "regime_family_macro_context",
        "description": "Systematic revisions to prior economic releases indicating historical bias or reporting lags",
        "underlying_features": "nfp_revision_magnitude, gdp_first_to_final_revision",
        "source_phases": [109, 110, 120],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "macro_ctx_05_release",
        "context_name": "macro_release_context",
        "regime_family": "regime_family_macro_context",
        "description": "Temporal proximity to major cyclical releases with publication time normalization",
        "underlying_features": "days_since_last_cpi, days_until_fomc_decision",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
]


def build_macro_regime_context_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for macro regime context registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(MACRO_CONTEXTS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_contexts": len(df),
        "regime_family": "regime_family_macro_context",
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_macro_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize macro regime context DataFrame."""
    return {
        "total_contexts": len(df),
        "context_names": list(df["context_name"].unique()) if "context_name" in df.columns else [],
        "non_signal": True,
    }
