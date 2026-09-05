from advanced_regime_matrix.regime_matrix_models import (
    RegimeMatrixProfileItem,
    RegimeFeatureMatrixContract,
    RegimeStateDatasetContract,
    RegimeMatrixEntity,
    RegimeMatrixSchemaItem,
    RegimeMatrixInputFeature,
    RegimeStateDatasetSchemaItem,
    RegimeStateCandidateContext,
    RegimeMatrixIntegrityManifest,
    RegimeMatrixManualReviewItem,
)


def test_regime_feature_matrix_contract_model():
    contract = RegimeFeatureMatrixContract(
        contract_name="technical_contract",
        matrix_family="technical",
        required_entity_keys=["entity_id", "timestamp"],
        timestamp_field="timestamp",
        symbol_field="canonical_symbol",
        required_feature_families=["volatility", "trend"],
        required_factor_families=["trend_slope"],
        required_context_inputs=["macro"],
        required_quality_inputs=["missingness"],
    )
    assert contract.non_signal is True
    assert contract.source_preserved is True
    assert contract.contains_target_or_prediction is False
    assert contract.model_training_executed is False
    assert contract.clustering_executed is False


def test_regime_state_dataset_contract_model():
    contract = RegimeStateDatasetContract(
        dataset_name="unsupervised_dataset",
        dataset_purpose="clustering",
        entity_keys=["entity_id", "timestamp"],
        timestamp_field="timestamp",
        regime_state_namespace="regime_state_",
        candidate_context_fields=["volatility_high"],
        forbidden_fields=["target_label", "future_return"],
    )
    assert contract.non_signal is True
    assert contract.source_preserved is True
    assert contract.contains_target_or_prediction is False
    assert contract.model_training_allowed is False


def test_regime_state_candidate_context_model():
    candidate = RegimeStateCandidateContext(
        candidate_name="volatility_expansion_context",
        regime_family="volatility",
        underlying_features=["regime_matrix__volatility_atr_14"],
        underlying_factors=["regime_matrix__factor_vol_ratio_20"],
        context_type="expansion",
        description="Volatility expansion research context",
    )
    assert candidate.is_target_or_label is False
    assert candidate.is_prediction is False
    assert candidate.is_trade_signal is False
    assert candidate.non_signal is True
