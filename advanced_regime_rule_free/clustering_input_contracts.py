"""Phase 128: Clustering Input Contracts.

Defines matrix input specifications for future clustering without executing algorithms.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import ClusteringInputContract

CLUSTERING_INPUT_CONTRACTS = [
    ClusteringInputContract(
        input_contract_name="technical_volatility_clustering_input_contract",
        required_matrix_schema="technical_indicator_matrix_contract",
        required_feature_families=["volatility_features", "range_features", "return_features"],
        required_quality_score_refs=["quality_score >= 0.70", "drift_score < 0.25"],
        required_validation_status_refs=["no_lookahead_pass", "forbidden_columns_clean"],
        forbidden_columns=["target", "label", "prediction", "buy", "sell", "future_return"],
    ),
    ClusteringInputContract(
        input_contract_name="technical_trend_clustering_input_contract",
        required_matrix_schema="technical_indicator_matrix_contract",
        required_feature_families=["trend_features", "momentum_features", "moving_average_features"],
        required_quality_score_refs=["quality_score >= 0.70", "drift_score < 0.25"],
        required_validation_status_refs=["no_lookahead_pass", "forbidden_columns_clean"],
        forbidden_columns=["target", "label", "prediction", "buy", "sell", "future_return"],
    ),
    ClusteringInputContract(
        input_contract_name="cross_asset_correlation_clustering_input_contract",
        required_matrix_schema="cross_asset_alignment_matrix_contract",
        required_feature_families=["cross_asset_correlation_features", "spread_divergence_features"],
        required_quality_score_refs=["session_alignment_score >= 0.80"],
        required_validation_status_refs=["no_lookahead_pass", "timestamp_order_pass"],
        forbidden_columns=["target", "label", "prediction", "signal", "future_return"],
    ),
    ClusteringInputContract(
        input_contract_name="macro_event_clustering_input_contract",
        required_matrix_schema="macro_event_context_matrix_contract",
        required_feature_families=["macro_features", "calendar_event_features"],
        required_quality_score_refs=["release_validation_score >= 0.75"],
        required_validation_status_refs=["no_lookahead_pass", "metadata_only_news_pass"],
        forbidden_columns=["target", "label", "prediction", "future_return", "raw_content"],
    ),
    ClusteringInputContract(
        input_contract_name="combined_multimodal_clustering_input_contract",
        required_matrix_schema="regime_feature_matrix_contract",
        required_feature_families=["technical_features", "macro_features", "cross_asset_features", "quality_features"],
        required_quality_score_refs=["overall_quality_score >= 0.75"],
        required_validation_status_refs=["comprehensive_validation_pass"],
        forbidden_columns=["target", "label", "prediction", "buy", "sell", "future_return", "full_text"],
    ),
]


def build_clustering_input_contract_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for clustering input contracts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for c in CLUSTERING_INPUT_CONTRACTS:
        row = c.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_clustering_input_contracts(df)
    return df, summary


def validate_clustering_input_contract(contract: dict) -> dict:
    """Validate that a clustering input contract adheres to zero-execution rules."""
    violations = []
    name = contract.get("input_contract_name", "unknown")

    if contract.get("model_training_allowed", True):
        violations.append("model_training_allowed must be False")
    if contract.get("clustering_allowed", True):
        violations.append("clustering_allowed must be False")
    if not contract.get("non_signal", False):
        violations.append("non_signal must be True")
    if not contract.get("no_lookahead_required", False):
        violations.append("no_lookahead_required must be True")

    for col in contract.get("forbidden_columns", []):
        if col.lower() not in ["target", "label", "prediction", "buy", "sell", "signal", "future_return", "raw_content", "full_text"]:
            pass

    return {
        "contract_name": name,
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_clustering_input_contracts(df: pd.DataFrame) -> Dict:
    """Summarize clustering input contracts."""
    total = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_no_clustering = bool((~df["clustering_allowed"]).all()) if not df.empty else True
    all_no_training = bool((~df["model_training_allowed"]).all()) if not df.empty else True

    return {
        "total_clustering_input_contracts": total,
        "all_non_signal": all_non_signal,
        "all_no_clustering": all_no_clustering,
        "all_no_training": all_no_training,
        "contracts_status": "VALID" if all_non_signal and all_no_clustering and all_no_training else "INVALID",
    }
