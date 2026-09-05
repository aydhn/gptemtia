"""Phase 127: Regime Matrix Environmental Context Inputs.

Catalogs non-signal contextual inputs that provide market backdrop to the regime matrix.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

CONTEXT_INPUTS_CATALOG: List[Dict[str, Any]] = [
    {
        "context_id": "context_macro_regime",
        "context_type": "macro_context",
        "name": "Macroeconomic Growth and Rate Context",
        "description": "Macroeconomic backdrop including inflation pressures and yield curve slope.",
        "source_phase": 120,
        "metadata_only": True,
        "non_signal": True,
    },
    {
        "context_id": "context_event_regime",
        "context_type": "event_context",
        "name": "Economic Calendar Event Window Context",
        "description": "Temporal distance to high-impact economic releases (pre-event, post-event).",
        "source_phase": 120,
        "metadata_only": True,
        "non_signal": True,
    },
    {
        "context_id": "context_news_metadata_regime",
        "context_type": "news_metadata_context",
        "name": "News Metadata Attention Context",
        "description": "Numerical attention volume and topic frequency tags (zero full text or NLP sentiment).",
        "source_phase": 120,
        "metadata_only": True,
        "non_signal": True,
    },
    {
        "context_id": "context_cross_asset_regime",
        "context_type": "cross_asset_context",
        "name": "Cross-Asset Intermarket Coupling Context",
        "description": "Correlation and spread divergence across commodity, currency, and rates markets.",
        "source_phase": 119,
        "metadata_only": True,
        "non_signal": True,
    },
    {
        "context_id": "context_volatility_regime",
        "context_type": "volatility_context",
        "name": "Market Volatility State Context",
        "description": "High vs low volatility state, expansion vs compression phases.",
        "source_phase": 126,
        "metadata_only": True,
        "non_signal": True,
    },
    {
        "context_id": "context_trend_regime",
        "context_type": "trend_context",
        "name": "Trend Persistence Context",
        "description": "Moving average alignment, directionality, and momentum slope.",
        "source_phase": 126,
        "metadata_only": True,
        "non_signal": True,
    },
    {
        "context_id": "context_range_regime",
        "context_type": "range_context",
        "name": "Range and Mean-Reversion Context",
        "description": "Bandwidth compression and price location within historical channels.",
        "source_phase": 126,
        "metadata_only": True,
        "non_signal": True,
    },
]


def build_regime_matrix_context_input_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the context input registry for Phase 127."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for c in CONTEXT_INPUTS_CATALOG:
        c_copy = c.copy()
        c_copy["current_phase"] = p.current_phase
        c_copy["target_final_phase"] = p.target_final_phase
        c_copy["next_phase"] = p.next_phase
        c_copy["source_preserved"] = True
        c_copy["status"] = "matrix_ready"
        rows.append(c_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_context_inputs(df)
    return df, summary


def summarize_regime_matrix_context_inputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize context inputs registry."""
    return {
        "total_context_inputs": len(df),
        "total_contexts": len(df),
        "context_types": df["context_type"].tolist() if not df.empty else [],
        "all_metadata_only": bool(df["metadata_only"].all()) if not df.empty else True,
        "no_article_text_guaranteed": True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_context_inputs_registry = build_regime_matrix_context_input_registry

