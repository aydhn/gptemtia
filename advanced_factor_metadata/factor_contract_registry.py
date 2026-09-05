"""Phase 122 Factor Contract Registry.

Defines formal contracts for factor inputs, validation dependencies, quality
prerequisites, and namespace bindings. Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_FAMILY_CALENDAR_EVENT,
    FACTOR_FAMILY_COMPOSITE,
    FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
    FACTOR_FAMILY_MACRO_CONTEXT,
    FACTOR_FAMILY_MEAN_REVERSION,
    FACTOR_FAMILY_MOMENTUM,
    FACTOR_FAMILY_NEWS_ATTENTION,
    FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
    FACTOR_FAMILY_REGIME_PREP,
    FACTOR_FAMILY_RETURN,
    FACTOR_FAMILY_TREND,
    FACTOR_FAMILY_VOLATILITY,
    FACTOR_READY,
)
from advanced_factor_metadata.factor_metadata_models import (
    FORBIDDEN_FACTOR_TOKENS,
    FactorContract,
    build_factor_contract_id,
)

CORE_FACTOR_CONTRACTS: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_trend_multi_window_context",
        "factor_family": FACTOR_FAMILY_TREND,
        "required_feature_sets": ["fset_moving_average_grid", "fset_donchian_grid"],
        "optional_feature_sets": ["fset_macd_grid"],
        "validation_dependencies": ["val_no_lookahead", "val_monotonic_timestamp", "val_no_forbidden_columns"],
        "quality_dependencies": ["qual_missingness_under_threshold", "qual_finite_values_only"],
        "namespace": "factor_trend_multi_window_context",
        "output_schema_ref": "schema_factor_trend_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_rsi_roc_context",
        "factor_family": FACTOR_FAMILY_MOMENTUM,
        "required_feature_sets": ["fset_rsi_grid", "fset_roc_grid"],
        "optional_feature_sets": ["fset_stochastic_grid"],
        "validation_dependencies": ["val_no_lookahead", "val_numeric_sanity"],
        "quality_dependencies": ["qual_missingness_under_threshold", "qual_drift_baseline_ready"],
        "namespace": "factor_momentum_rsi_roc_context",
        "output_schema_ref": "schema_factor_momentum_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_atr_realized_context",
        "factor_family": FACTOR_FAMILY_VOLATILITY,
        "required_feature_sets": ["fset_atr_grid", "fset_realized_vol_grid"],
        "optional_feature_sets": ["fset_bollinger_bandwidth_grid"],
        "validation_dependencies": ["val_no_lookahead", "val_positive_values_only"],
        "quality_dependencies": ["qual_missingness_under_threshold", "qual_no_infinite_values"],
        "namespace": "factor_volatility_atr_realized_context",
        "output_schema_ref": "schema_factor_volatility_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_mean_reversion_zscore_context",
        "factor_family": FACTOR_FAMILY_MEAN_REVERSION,
        "required_feature_sets": ["fset_zscore_grid", "fset_distance_to_ma_grid"],
        "optional_feature_sets": ["fset_percentile_rank_grid"],
        "validation_dependencies": ["val_no_lookahead", "val_warmup_nan_preserved"],
        "quality_dependencies": ["qual_finite_values_only", "qual_missingness_under_threshold"],
        "namespace": "factor_mean_reversion_zscore_context",
        "output_schema_ref": "schema_factor_mean_reversion_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_return_multi_horizon_context",
        "factor_family": FACTOR_FAMILY_RETURN,
        "required_feature_sets": ["fset_return_grid"],
        "optional_feature_sets": ["fset_log_return_grid"],
        "validation_dependencies": ["val_no_lookahead", "val_no_forward_returns"],
        "quality_dependencies": ["qual_no_infinite_values"],
        "namespace": "factor_return_multi_horizon_context",
        "output_schema_ref": "schema_factor_return_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_quote_spread_context_placeholder",
        "factor_family": FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
        "required_feature_sets": ["fset_quote_spread_grid"],
        "optional_feature_sets": ["fset_bid_ask_ratio_grid"],
        "validation_dependencies": ["val_monotonic_timestamp"],
        "quality_dependencies": ["qual_liquidity_data_present"],
        "namespace": "factor_quote_spread_context_placeholder",
        "output_schema_ref": "schema_factor_quote_float64",
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_macro_inflation_rate_context",
        "factor_family": FACTOR_FAMILY_MACRO_CONTEXT,
        "required_feature_sets": ["fset_macro_fusion"],
        "optional_feature_sets": ["fset_macro_revision_flags"],
        "validation_dependencies": ["val_macro_release_lag", "val_backward_asof_join"],
        "quality_dependencies": ["qual_point_in_time_guaranteed"],
        "namespace": "factor_macro_inflation_rate_context",
        "output_schema_ref": "schema_factor_macro_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_event_release_context",
        "factor_family": FACTOR_FAMILY_CALENDAR_EVENT,
        "required_feature_sets": ["fset_calendar_event_windows"],
        "optional_feature_sets": ["fset_release_delay_features"],
        "validation_dependencies": ["val_event_window_temporal_integrity"],
        "quality_dependencies": ["qual_event_timestamps_verified"],
        "namespace": "factor_event_release_context",
        "output_schema_ref": "schema_factor_event_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_attention_context",
        "factor_family": FACTOR_FAMILY_NEWS_ATTENTION,
        "required_feature_sets": ["fset_news_topic_fusion", "fset_news_tag_fusion"],
        "optional_feature_sets": ["fset_news_event_linkage"],
        "validation_dependencies": ["val_news_metadata_only", "val_no_full_text_or_scraping"],
        "quality_dependencies": ["qual_metadata_frequency_sanity"],
        "namespace": "factor_news_attention_context",
        "output_schema_ref": "schema_factor_news_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_cross_asset_context",
        "factor_family": FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
        "required_feature_sets": ["fset_cross_domain_matrix"],
        "optional_feature_sets": ["fset_aligned_universe_features"],
        "validation_dependencies": ["val_backward_asof_join", "val_no_lookahead"],
        "quality_dependencies": ["qual_cross_asset_alignment_verified"],
        "namespace": "factor_cross_asset_context",
        "output_schema_ref": "schema_factor_cross_asset_float64",
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_regime_prep_placeholder",
        "factor_family": FACTOR_FAMILY_REGIME_PREP,
        "required_feature_sets": ["fset_volatility_grid", "fset_trend_grid"],
        "optional_feature_sets": ["fset_macro_fusion"],
        "validation_dependencies": ["val_no_lookahead", "val_numeric_sanity"],
        "quality_dependencies": ["qual_phase_126_readiness"],
        "namespace": "factor_regime_prep_placeholder",
        "output_schema_ref": "schema_factor_regime_prep_float64",
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_composite_context_placeholder",
        "factor_family": FACTOR_FAMILY_COMPOSITE,
        "required_feature_sets": ["fset_moving_average_grid", "fset_macro_fusion"],
        "optional_feature_sets": ["fset_cross_domain_matrix"],
        "validation_dependencies": ["val_no_lookahead", "val_no_forbidden_columns"],
        "quality_dependencies": ["qual_composite_stability"],
        "namespace": "factor_composite_context_placeholder",
        "output_schema_ref": "schema_factor_composite_float64",
        "manual_review_required": True,
    },
]


def validate_factor_contract(contract: FactorContract) -> Dict[str, Any]:
    """Validate that a factor contract adheres to safety and formatting standards."""
    errors: List[str] = []
    warnings: List[str] = []

    if not contract.factor_name.startswith("factor_"):
        errors.append(f"Contract {contract.factor_name} must start with 'factor_' prefix")

    lower_name = contract.factor_name.lower()
    for token in FORBIDDEN_FACTOR_TOKENS:
        if token in lower_name:
            errors.append(f"Contract {contract.factor_name} contains forbidden token '{token}'")

    if not contract.required_feature_sets:
        errors.append(f"Contract {contract.factor_name} must define at least one required feature set")

    if not contract.non_signal:
        errors.append(f"Contract {contract.factor_name} non_signal flag must be True")

    is_valid = len(errors) == 0
    return {
        "contract_id": contract.contract_id,
        "factor_name": contract.factor_name,
        "is_valid": is_valid,
        "errors": errors,
        "warnings": warnings,
    }


def build_factor_contract_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Contract Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    items: List[Dict[str, Any]] = []
    validation_results: List[Dict[str, Any]] = []

    for d in CORE_FACTOR_CONTRACTS:
        contract = FactorContract(
            contract_id=build_factor_contract_id(d["factor_name"], d["factor_family"]),
            factor_name=d["factor_name"],
            factor_family=d["factor_family"],
            required_feature_sets=d["required_feature_sets"],
            optional_feature_sets=d["optional_feature_sets"],
            validation_dependencies=d["validation_dependencies"],
            quality_dependencies=d["quality_dependencies"],
            namespace=d["namespace"],
            output_schema_ref=d["output_schema_ref"],
            non_signal=True,
            manual_review_required=d["manual_review_required"],
        )
        val_res = validate_factor_contract(contract)
        validation_results.append(val_res)
        items.append(contract.to_dict())

    df = pd.DataFrame(items)
    all_valid = all(v["is_valid"] for v in validation_results)

    summary = {
        "active_profile": active_profile.name,
        "total_contracts": len(items),
        "valid_contracts": sum(1 for v in validation_results if v["is_valid"]),
        "all_contracts_valid": all_valid,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY if all_valid else "factor_validation_failed",
    }
    return df, summary


def summarize_factor_contract_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor contract registry DataFrame."""
    return {
        "total_contracts": len(df),
        "families_covered": int(df["factor_family"].nunique()) if "factor_family" in df else 0,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df else 0,
        "non_signal": True,
    }
