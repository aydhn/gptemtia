"""Phase 132: Macro/Event/News Source Phase Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_SOURCE_PHASES = [
    {
        "phase_number": 120,
        "phase_name": "Phase 120: Macro/Calendar/News Feature Fusion",
        "contribution": "Fused multi-source raw feature foundation for macro, calendar, and news.",
        "status": "integrated",
    },
    {
        "phase_number": 121,
        "phase_name": "Phase 121: Feature Validation and Matrix Integrity",
        "contribution": "Lookahead rejection rules, NaN thresholds, and numerical sanity checks.",
        "status": "integrated",
    },
    {
        "phase_number": 123,
        "phase_name": "Phase 123: Feature Quality and Drift Diagnostics",
        "contribution": "Stationarity and quality metrics for macroeconomic factors.",
        "status": "integrated",
    },
    {
        "phase_number": 124,
        "phase_name": "Phase 124: FeatureStore Integration",
        "contribution": "Feature catalog and feature store metadata persistence contracts.",
        "status": "integrated",
    },
    {
        "phase_number": 126,
        "phase_name": "Phase 126: Regime Classification Foundation",
        "contribution": "Baseline market regime definitions and taxonomy.",
        "status": "integrated",
    },
    {
        "phase_number": 127,
        "phase_name": "Phase 127: Regime Feature Matrix Contracts",
        "contribution": "Contracts and schema validation for regime datasets.",
        "status": "integrated",
    },
    {
        "phase_number": 128,
        "phase_name": "Phase 128: Regime Rule-Free Labeling & Unsupervised Prep",
        "contribution": "Non-directional candidate state preparation.",
        "status": "integrated",
    },
    {
        "phase_number": 129,
        "phase_name": "Phase 129: Market Behavior Diagnostics & Regime Quality",
        "contribution": "Behavior metrics across volatility, trend, and range states.",
        "status": "integrated",
    },
    {
        "phase_number": 130,
        "phase_name": "Phase 130: Regime Transition & Stability Analysis",
        "contribution": "Transition matrices and state sequence persistence contracts.",
        "status": "integrated",
    },
    {
        "phase_number": 131,
        "phase_name": "Phase 131: Cross-Asset Regime Context Expansion",
        "contribution": "Multi-asset regime context alignment across FX, Commodities, and Macro.",
        "status": "integrated",
    },
]


def build_macro_event_news_source_phase_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of upstream and connecting source phases."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_SOURCE_PHASES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_source_phases": len(df),
        "phases": df["phase_number"].tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_source_phases(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for source phases registry."""
    return {
        "total_phases": len(df),
        "min_phase": int(df["phase_number"].min()) if "phase_number" in df.columns else 0,
        "max_phase": int(df["phase_number"].max()) if "phase_number" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
