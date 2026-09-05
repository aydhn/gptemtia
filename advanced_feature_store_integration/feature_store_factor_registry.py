"""Phase 124 Feature Store Factor Registry.

Aggregates factor definitions and contracts from Phase 122 & 123
into the centralized feature store.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

CORE_STORE_FACTORS = [
    {
        "factor_name": "factor__technical__fx__eurusd__sma_spread__20_50",
        "factor_family": "technical",
        "entity_type": "entity_fx_pair",
        "source_phase": 122,
        "input_feature_set_ref": "sma_20,sma_50",
        "validation_dependency_ref": "DEP_VAL_121_EURUSD_SMA",
        "quality_dependency_ref": "DEP_QUAL_123_EURUSD_SMA",
        "manifest_ref": "MAN_FACTOR_TECH_001",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "factor_name": "factor__trend__commodity__brent__adx_proxy__14",
        "factor_family": "trend",
        "entity_type": "entity_commodity_symbol",
        "source_phase": 122,
        "input_feature_set_ref": "atr_14,high,low,close",
        "validation_dependency_ref": "DEP_VAL_121_BRENT_ADX",
        "quality_dependency_ref": "DEP_QUAL_123_BRENT_ADX",
        "manifest_ref": "MAN_FACTOR_TREND_002",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "factor_name": "factor__momentum__fx__eurusd__rsi_norm__14",
        "factor_family": "momentum",
        "entity_type": "entity_fx_pair",
        "source_phase": 122,
        "input_feature_set_ref": "rsi_14",
        "validation_dependency_ref": "DEP_VAL_121_EURUSD_RSI",
        "quality_dependency_ref": "DEP_QUAL_123_EURUSD_RSI",
        "manifest_ref": "MAN_FACTOR_MOM_003",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "factor_name": "factor__volatility__commodity__brent__bollinger_bandwidth__20",
        "factor_family": "volatility",
        "entity_type": "entity_commodity_symbol",
        "source_phase": 122,
        "input_feature_set_ref": "bb_upper_20,bb_lower_20,bb_mid_20",
        "validation_dependency_ref": "DEP_VAL_121_BRENT_BB",
        "quality_dependency_ref": "DEP_QUAL_123_BRENT_BB",
        "manifest_ref": "MAN_FACTOR_VOL_004",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "factor_name": "factor__macro_context__multi__us10y_yield_spread__30",
        "factor_family": "macro_context",
        "entity_type": "entity_macro_indicator",
        "source_phase": 122,
        "input_feature_set_ref": "us10y_yield,fedfunds_rate",
        "validation_dependency_ref": "DEP_VAL_121_MACRO_US10Y",
        "quality_dependency_ref": "DEP_QUAL_123_MACRO_US10Y",
        "manifest_ref": "MAN_FACTOR_MACRO_005",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "factor_name": "factor__cross_asset_context__multi__dxy_crude_beta__60",
        "factor_family": "cross_asset_context",
        "entity_type": "entity_cross_asset_context",
        "source_phase": 122,
        "input_feature_set_ref": "dxy_return_60,brent_return_60",
        "validation_dependency_ref": "DEP_VAL_121_CROSS_BETA",
        "quality_dependency_ref": "DEP_QUAL_123_CROSS_BETA",
        "manifest_ref": "MAN_FACTOR_CROSS_006",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
]


def build_feature_store_factor_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature store factors."""
    prof = profile or get_default_feature_store_integration_profile()
    records = []
    for f in CORE_STORE_FACTORS:
        item = dict(f)
        item["current_phase"] = prof.current_phase
        item["target_final_phase"] = prof.target_final_phase
        records.append(item)

    df = pd.DataFrame(records)
    summary = {
        "total_factors": len(records),
        "factor_families": sorted(list(set(r["factor_family"] for r in records))),
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    }
    return df, summary


def summarize_feature_store_factor_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor registry."""
    if df.empty:
        return {"total_factors": 0, "non_signal": True, "source_preserved": True}
    return {
        "total_factors": len(df),
        "all_non_signal": bool(all(df.get("non_signal", [True]))),
        "all_source_preserved": bool(all(df.get("source_preserved", [True]))),
    }
