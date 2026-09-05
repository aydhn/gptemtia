from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_state_dataset_contracts import (
    build_regime_state_dataset_contract_registry,
    build_regime_state_dataset_contracts,
    validate_regime_state_dataset_contract,
    CORE_STATE_DATASET_CONTRACTS,
)


def test_build_regime_state_dataset_contracts():
    prof = get_default_regime_matrix_profile()
    df, s = build_regime_state_dataset_contracts(prof)
    assert len(df) == 4
    assert s["total_dataset_contracts"] == 4
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert s["all_no_target_label_prediction"] is True

    names = set(df["dataset_name"].values)
    assert "regime_state_research_dataset_contract" in names
    assert "regime_state_candidate_context_dataset_contract" in names


def test_validate_regime_state_dataset_contract():
    c = CORE_STATE_DATASET_CONTRACTS[0]
    res = validate_regime_state_dataset_contract(c)
    assert res["is_valid"] is True
    assert res["non_signal"] is True
