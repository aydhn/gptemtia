from advanced_regime_matrix.regime_state_dataset_metadata import (
    build_regime_state_dataset_metadata_registry,
    is_valid_regime_state_dataset,
)


def test_build_regime_state_dataset_metadata_registry():
    df, s = build_regime_state_dataset_metadata_registry()
    assert len(df) == 5
    assert s["total_datasets"] == 5
    assert s["all_non_signal"] is True
    assert s["any_target_or_prediction"] is False
    assert is_valid_regime_state_dataset("unsupervised_clustering_input_dataset") is True
    assert is_valid_regime_state_dataset("supervised_target_dataset") is False
