from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


FX_LINEAGE_ITEMS = [
    {
        "lineage_item_id": "fx_lin_pair_norm",
        "domain": "fx_lineage_domain",
        "provider_profile": "balanced_no_scraping_fx_provider",
        "raw_field": "pair",
        "canonical_field": "normalized_pair",
        "schema_ref": "canonical://schema/fx_quote_canonical_v1",
        "normalization_rule": "fx_symbol_normalization_enforcement",
        "quality_rule_ref": "fx_quote_sanity_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Slashing applied (e.g. EURUSD -> EUR/USD); raw column unchanged",
    },
    {
        "lineage_item_id": "fx_lin_ohlcv_schema",
        "domain": "fx_lineage_domain",
        "provider_profile": "balanced_no_scraping_fx_provider",
        "raw_field": "open, high, low, close, volume",
        "canonical_field": "normalized_ohlcv",
        "schema_ref": "canonical://schema/fx_ohlcv_canonical_v1",
        "normalization_rule": "numeric_type_normalization",
        "quality_rule_ref": "ohlc_geometry_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Safe float casting; zero auto-deletion on outlier",
    },
    {
        "lineage_item_id": "fx_lin_quote_spread",
        "domain": "fx_lineage_domain",
        "provider_profile": "balanced_no_scraping_fx_provider",
        "raw_field": "bid, ask",
        "canonical_field": "canonical_bid_ask_spread",
        "schema_ref": "canonical://schema/fx_quote_canonical_v1",
        "normalization_rule": "quote_spread_consistency_rule",
        "quality_rule_ref": "quote_spread_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Spread non-negativity audit; raw bid/ask preserved",
    },
]


def build_fx_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(FX_LINEAGE_ITEMS)
    summary = summarize_fx_lineage_registry(df)
    return df, summary


def summarize_fx_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_fx_lineage_items": len(df),
        "canonical_fields": df["canonical_field"].tolist() if "canonical_field" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
