"""Phase 132: Macro Indicator Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_MACRO_INDICATOR_CONTEXTS = [
    {
        "context_id": "ctx_macro_inflation_level",
        "context_name": "inflation_regime_context",
        "indicator_id": "macro_us_cpi_yoy",
        "indicator_category": "inflation",
        "description": "US CPI YoY level mapped to macro inflationary regime tier.",
        "regime_context_tier": "elevated_inflation_context",
        "policy_sensitivity": "high",
        "commodity_sensitivity": "high",
        "fx_sensitivity": "high",
    },
    {
        "context_id": "ctx_macro_rate_level",
        "context_name": "rate_regime_context",
        "indicator_id": "macro_us_fed_funds_rate",
        "indicator_category": "interest_rates",
        "description": "Policy interest rate regime level context without trade signal.",
        "regime_context_tier": "restrictive_rate_context",
        "policy_sensitivity": "critical",
        "commodity_sensitivity": "medium",
        "fx_sensitivity": "critical",
    },
    {
        "context_id": "ctx_macro_growth_pmi",
        "context_name": "growth_regime_context",
        "indicator_id": "macro_cn_manufacturing_pmi",
        "indicator_category": "growth",
        "description": "Global manufacturing PMI growth trajectory context.",
        "regime_context_tier": "expansion_neutral_context",
        "policy_sensitivity": "medium",
        "commodity_sensitivity": "critical",
        "fx_sensitivity": "medium",
    },
    {
        "context_id": "ctx_macro_employment_nfp",
        "context_name": "employment_regime_context",
        "indicator_id": "macro_us_nfp",
        "indicator_category": "labor",
        "description": "US Non-Farm Payrolls employment environment context.",
        "regime_context_tier": "tight_labor_market_context",
        "policy_sensitivity": "high",
        "commodity_sensitivity": "medium",
        "fx_sensitivity": "high",
    },
    {
        "context_id": "ctx_macro_policy_stance",
        "context_name": "macro_policy_sensitivity_context",
        "indicator_id": "macro_us_fed_funds_rate",
        "indicator_category": "central_bank",
        "description": "Macro policy sensitivity stance context for cross-asset assessment.",
        "regime_context_tier": "hawkish_pause_context",
        "policy_sensitivity": "critical",
        "commodity_sensitivity": "high",
        "fx_sensitivity": "critical",
    },
    {
        "context_id": "ctx_macro_fx_sensitive",
        "context_name": "fx_sensitive_macro_context",
        "indicator_id": "macro_eu_hicp_yoy",
        "indicator_category": "fx_sensitivity",
        "description": "Eurozone inflation relative policy stance impact context on EUR/USD.",
        "regime_context_tier": "differential_divergence_context",
        "policy_sensitivity": "high",
        "commodity_sensitivity": "medium",
        "fx_sensitivity": "critical",
    },
    {
        "context_id": "ctx_macro_commodity_sensitive",
        "context_name": "commodity_sensitive_macro_context",
        "indicator_id": "macro_cn_manufacturing_pmi",
        "indicator_category": "commodity_sensitivity",
        "description": "Industrial commodity sensitivity context based on leading growth metrics.",
        "regime_context_tier": "cyclical_demand_context",
        "policy_sensitivity": "medium",
        "commodity_sensitivity": "critical",
        "fx_sensitivity": "medium",
    },
]


def build_macro_indicator_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro indicator regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_MACRO_INDICATOR_CONTEXTS:
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
        "total_macro_contexts": len(df),
        "context_names": df["context_name"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_indicator_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for macro indicator regime context."""
    return {
        "total_contexts": len(df),
        "indicator_categories": df["indicator_category"].nunique() if "indicator_category" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
