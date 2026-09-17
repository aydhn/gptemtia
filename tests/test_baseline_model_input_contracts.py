"""Test suite for Phase 138 Baseline Model Input Contracts."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_input_contracts import (
    INPUT_CONTRACT_DEFINITIONS,
    build_baseline_model_input_contract_registry,
    summarize_baseline_model_input_contracts,
)


def test_baseline_model_input_contracts_data():
    assert len(INPUT_CONTRACT_DEFINITIONS) == 3
    contract_ids = [c["input_contract_id"] for c in INPUT_CONTRACT_DEFINITIONS]
    assert "input_contract_commodity_fx_v1" in contract_ids


def test_build_baseline_model_input_contract_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_model_input_contract_registry(profile)

    assert len(df) == 3
    assert summary["total_input_contracts"] == 3
    assert summary["all_materialization_blocked"] is True
    assert summary["all_validated"] is True
    assert summary["non_signal"] is True
    assert bool((df["dataset_materialized"] == False).all())
    assert bool((df["feature_snapshot_materialized"] == False).all())
