"""Phase 132: Macro Regime Context Taxonomy."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_MACRO_TAXONOMIES = [
    {
        "taxonomy_id": "macro_tax_inflation",
        "taxonomy_name": "inflation_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Macro inflation environment contextualization (YoY/MoM metrics without directional bias).",
        "parent_category": "macro_fundamentals",
    },
    {
        "taxonomy_id": "macro_tax_rate",
        "taxonomy_name": "rate_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Central bank policy rate environment and yield regime level context.",
        "parent_category": "macro_fundamentals",
    },
    {
        "taxonomy_id": "macro_tax_growth",
        "taxonomy_name": "growth_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Macro economic expansion/contraction indicators context (GDP, PMIs).",
        "parent_category": "macro_fundamentals",
    },
    {
        "taxonomy_id": "macro_tax_employment",
        "taxonomy_name": "employment_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Labor market tightness and payroll dynamic context.",
        "parent_category": "macro_fundamentals",
    },
    {
        "taxonomy_id": "macro_tax_revision",
        "taxonomy_name": "macro_revision_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Historical revision differential context tracking data restatements.",
        "parent_category": "data_quality_context",
    },
    {
        "taxonomy_id": "macro_tax_surprise",
        "taxonomy_name": "macro_surprise_placeholder_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Consensus vs actual divergence placeholder without trade signal implication.",
        "parent_category": "consensus_context",
    },
    {
        "taxonomy_id": "macro_tax_policy_sens",
        "taxonomy_name": "policy_sensitivity_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Macro policy stance shift context and communication period awareness.",
        "parent_category": "sensitivity_context",
    },
    {
        "taxonomy_id": "macro_tax_comm_sens",
        "taxonomy_name": "commodity_sensitivity_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Macro growth and energy/metals demand cross-linkage context.",
        "parent_category": "cross_asset_sensitivity",
    },
    {
        "taxonomy_id": "macro_tax_fx_sens",
        "taxonomy_name": "fx_sensitivity_context",
        "domain": "macro_context_taxonomy_domain",
        "description": "Interest rate differential and foreign exchange regime linkage context.",
        "parent_category": "cross_asset_sensitivity",
    },
]


def build_macro_regime_context_taxonomy_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build taxonomy registry DataFrame for macro context."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_MACRO_TAXONOMIES:
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
        "total_macro_taxonomies": len(df),
        "domains": df["domain"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_regime_context_taxonomy(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for macro context taxonomy."""
    return {
        "total_taxonomies": len(df),
        "parent_categories": df["parent_category"].nunique() if "parent_category" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
