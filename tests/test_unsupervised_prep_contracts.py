from advanced_regime_rule_free.unsupervised_prep_contracts import (
    build_unsupervised_prep_contract_registry,
    validate_unsupervised_prep_contract,
)


def test_build_unsupervised_prep_contract_registry():
    df, summary = build_unsupervised_prep_contract_registry()
    assert len(df) == 6
    assert summary["all_non_signal"] is True
    assert summary["all_no_training"] is True
    assert summary["all_no_clustering"] is True
    assert summary["prep_status"] == "VALID"

    names = df["contract_name"].tolist()
    assert "unsupervised_matrix_readiness_contract" in names
    assert "candidate_state_feature_selection_placeholder_contract" in names
    assert "unsupervised_normalization_prep_contract" in names
    assert "unsupervised_distance_metric_prep_contract" in names


def test_validate_unsupervised_prep_contract():
    valid = {
        "contract_name": "unsupervised_matrix_readiness_contract",
        "fit_transform_allowed": False,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "dimensionality_reduction_allowed": False,
        "non_signal": True,
    }
    assert validate_unsupervised_prep_contract(valid)["is_valid"] is True

    invalid = {
        "contract_name": "unsupervised_cluster_exec",
        "fit_transform_allowed": True,
        "clustering_allowed": True,
        "model_training_allowed": True,
        "non_signal": False,
    }
    assert validate_unsupervised_prep_contract(invalid)["is_valid"] is False
