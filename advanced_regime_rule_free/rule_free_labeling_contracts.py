"""Phase 128: Rule-Free Labeling Contracts.

Defines candidate state annotation contracts without supervised target labels or trade signals.
"""

from typing import Dict, List, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import RuleFreeLabelingContract

RULE_FREE_CONTRACTS = [
    RuleFreeLabelingContract(
        contract_name="volatility_candidate_state_contract",
        candidate_state_family="volatility",
        source_matrix_contract_ref="technical_indicator_matrix_contract",
        required_feature_families=["volatility_features", "range_features", "return_features"],
        required_factor_families=["volatility_factors", "technical_factors"],
        required_context_inputs=["rolling_std", "atr", "realized_volatility"],
        required_quality_inputs=["feature_quality_score", "staleness_score"],
    ),
    RuleFreeLabelingContract(
        contract_name="trend_candidate_state_contract",
        candidate_state_family="trend",
        source_matrix_contract_ref="technical_indicator_matrix_contract",
        required_feature_families=["trend_features", "moving_average_features", "momentum_features"],
        required_factor_families=["trend_factors", "momentum_factors"],
        required_context_inputs=["ma_distance", "adx_dmi", "rsi"],
        required_quality_inputs=["feature_quality_score", "drift_score"],
    ),
    RuleFreeLabelingContract(
        contract_name="range_candidate_state_contract",
        candidate_state_family="range",
        source_matrix_contract_ref="technical_indicator_matrix_contract",
        required_feature_families=["range_features", "channel_features", "mean_reversion_features"],
        required_factor_families=["range_factors", "mean_reversion_factors"],
        required_context_inputs=["bollinger_bandwidth", "range_zscore", "donchian_position"],
        required_quality_inputs=["feature_quality_score"],
    ),
    RuleFreeLabelingContract(
        contract_name="macro_event_candidate_state_contract",
        candidate_state_family="macro_event",
        source_matrix_contract_ref="macro_event_context_matrix_contract",
        required_feature_families=["macro_features", "calendar_event_features", "release_features"],
        required_factor_families=["macro_factors", "calendar_factors"],
        required_context_inputs=["surprise_score", "event_impact_weight"],
        required_quality_inputs=["macro_quality_score", "release_verification"],
    ),
    RuleFreeLabelingContract(
        contract_name="news_attention_candidate_state_contract",
        candidate_state_family="news_attention",
        source_matrix_contract_ref="news_metadata_context_matrix_contract",
        required_feature_families=["news_metadata_features", "topic_intensity_features"],
        required_factor_families=["news_metadata_factors"],
        required_context_inputs=["headline_count", "urgency_flag", "source_diversity"],
        required_quality_inputs=["license_compliance", "metadata_only_verification"],
    ),
    RuleFreeLabelingContract(
        contract_name="cross_asset_candidate_state_contract",
        candidate_state_family="cross_asset",
        source_matrix_contract_ref="cross_asset_alignment_matrix_contract",
        required_feature_families=["cross_asset_correlation_features", "relative_strength_features"],
        required_factor_families=["cross_asset_factors"],
        required_context_inputs=["fx_commodity_correlation", "spread_divergence"],
        required_quality_inputs=["session_alignment_score"],
    ),
    RuleFreeLabelingContract(
        contract_name="transition_candidate_state_contract",
        candidate_state_family="transition",
        source_matrix_contract_ref="regime_feature_matrix_contract",
        required_feature_families=["volatility_features", "trend_features", "momentum_features"],
        required_factor_families=["volatility_factors", "trend_factors"],
        required_context_inputs=["acceleration_factor", "volatility_breakout"],
        required_quality_inputs=["feature_quality_score", "drift_score"],
    ),
    RuleFreeLabelingContract(
        contract_name="uncertain_candidate_state_contract",
        candidate_state_family="uncertain",
        source_matrix_contract_ref="regime_feature_matrix_contract",
        required_feature_families=["quality_drift_features", "staleness_features"],
        required_factor_families=["quality_drift_factors"],
        required_context_inputs=["missingness_rate", "drift_index"],
        required_quality_inputs=["overall_quality_score"],
    ),
]


def build_rule_free_labeling_contract_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for rule-free labeling contracts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for c in RULE_FREE_CONTRACTS:
        row = c.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_rule_free_labeling_contracts(df)
    return df, summary


def validate_rule_free_labeling_contract(contract: dict) -> dict:
    """Validate that a rule-free labeling contract strictly adheres to non-signal boundaries."""
    violations = []
    name = contract.get("contract_name", "unknown")

    if not contract.get("non_signal_required", False):
        violations.append("non_signal_required must be True")
    if not contract.get("target_label_forbidden", False):
        violations.append("target_label_forbidden must be True")
    if not contract.get("prediction_forbidden", False):
        violations.append("prediction_forbidden must be True")
    if contract.get("model_training_allowed", True):
        violations.append("model_training_allowed must be False")
    if contract.get("clustering_allowed", True):
        violations.append("clustering_allowed must be False")

    # Check for forbidden signal terms in name or family
    for term in ["buy", "sell", "long", "short", "position", "target", "predict"]:
        if term in name.lower() or term in contract.get("candidate_state_family", "").lower():
            violations.append(f"Forbidden term '{term}' found in contract definition")

    return {
        "contract_name": name,
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_rule_free_labeling_contracts(df: pd.DataFrame) -> Dict:
    """Summarize rule-free labeling contracts."""
    total_contracts = len(df)
    all_non_signal = bool(df["non_signal_required"].all()) if not df.empty else True
    all_target_forbidden = bool(df["target_label_forbidden"].all()) if not df.empty else True
    all_prediction_forbidden = bool(df["prediction_forbidden"].all()) if not df.empty else True
    all_clustering_forbidden = bool((~df["clustering_allowed"]).all()) if not df.empty else True
    all_training_forbidden = bool((~df["model_training_allowed"]).all()) if not df.empty else True

    return {
        "total_contracts": total_contracts,
        "all_non_signal": all_non_signal,
        "all_target_forbidden": all_target_forbidden,
        "all_prediction_forbidden": all_prediction_forbidden,
        "all_clustering_forbidden": all_clustering_forbidden,
        "all_training_forbidden": all_training_forbidden,
        "contracts_status": "VALID" if all_non_signal and all_target_forbidden else "INVALID",
    }
