"""Test suite for Phase 139 Training Loop Stub Contracts."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.training_loop_stub_contracts import (
    FORBIDDEN_TRAINING_LOOP_METHODS,
    build_training_loop_stub_contract_registry,
    summarize_training_loop_stub_contracts,
    validate_training_loop_stub_contract,
)


def test_build_training_loop_stub_contract_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_training_loop_stub_contract_registry(profile)

    assert len(df) == 5
    assert summary["total_contracts"] == 5
    assert summary["all_execution_disabled"] is True
    assert summary["all_dry_run"] is True
    assert summary["non_signal"] is True


def test_validate_training_loop_stub_contract():
    valid_contract = {
        "contract_name": "valid_contract",
        "allowed_execution": False,
        "dry_run_only": True,
        "blocked_keywords": ",".join(FORBIDDEN_TRAINING_LOOP_METHODS),
    }
    res = validate_training_loop_stub_contract(valid_contract)
    assert res["is_valid"] is True
    assert len(res["violations"]) == 0

    invalid_contract = {
        "contract_name": "invalid_contract",
        "allowed_execution": True,
        "dry_run_only": False,
        "blocked_keywords": "fit,train",
    }
    res_inv = validate_training_loop_stub_contract(invalid_contract)
    assert res_inv["is_valid"] is False
    assert len(res_inv["violations"]) >= 3
