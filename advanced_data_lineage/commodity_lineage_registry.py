from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


COMMODITY_LINEAGE_ITEMS = [
    {
        "lineage_item_id": "com_lin_symbol_norm",
        "domain": "commodity_lineage_domain",
        "provider_profile": "balanced_no_scraping_commodity_provider",
        "raw_field": "symbol",
        "canonical_field": "normalized_symbol",
        "schema_ref": "canonical://schema/commodity_spot_canonical_v1",
        "normalization_rule": "commodity_symbol_normalization_enforcement",
        "quality_rule_ref": "commodity_symbol_sanity_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Root mapped (e.g. GOLD -> XAU/USD, BRENT -> BRENT_CRUDE_SPOT); raw symbol preserved",
    },
    {
        "lineage_item_id": "com_lin_futures_meta",
        "domain": "commodity_lineage_domain",
        "provider_profile": "balanced_no_scraping_commodity_provider",
        "raw_field": "contract_code, expiry",
        "canonical_field": "canonical_futures_root",
        "schema_ref": "canonical://schema/commodity_futures_canonical_v1",
        "normalization_rule": "futures_contract_root_derivation",
        "quality_rule_ref": "futures_contract_sanity_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Continuous contract placeholder metadata attached; zero order execution",
    },
    {
        "lineage_item_id": "com_lin_roll_adjust",
        "domain": "commodity_lineage_domain",
        "provider_profile": "balanced_no_scraping_commodity_provider",
        "raw_field": "roll_date, roll_spread",
        "canonical_field": "canonical_roll_adjustment_requirement",
        "schema_ref": "canonical://schema/commodity_roll_adjustment_v1",
        "normalization_rule": "session_alignment_requirements",
        "quality_rule_ref": "roll_adjustment_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Roll-adjustment metadata logged for Phase 115 benchmark comparison",
    },
]


def build_commodity_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(COMMODITY_LINEAGE_ITEMS)
    summary = summarize_commodity_lineage_registry(df)
    return df, summary


def summarize_commodity_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_commodity_lineage_items": len(df),
        "canonical_fields": df["canonical_field"].tolist() if "canonical_field" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
