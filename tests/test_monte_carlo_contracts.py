# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Robustness & Bootstrap Contracts."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_robustness_contracts import (
    build_monte_carlo_robustness_contract_registry,
    validate_monte_carlo_robustness_contract,
)
from advanced_monte_carlo_robustness.bootstrap_simulation_contracts import (
    build_bootstrap_simulation_contract_registry,
)
from advanced_monte_carlo_robustness.block_bootstrap_contracts import (
    build_block_bootstrap_contract_registry,
)
from advanced_monte_carlo_robustness.stationary_bootstrap_contracts import (
    build_stationary_bootstrap_contract_registry,
)
from advanced_monte_carlo_robustness.return_path_resampling_contracts import (
    build_return_path_resampling_contract_registry,
)
from advanced_monte_carlo_robustness.trade_sequence_reshuffling_contracts import (
    build_trade_sequence_reshuffling_contract_registry,
)


def test_core_robustness_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_robustness_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 9
    assert summary["all_contracts_valid"] is True
    assert summary["all_executions_blocked"] is True

    for _, row in df.iterrows():
        res = validate_monte_carlo_robustness_contract(row.to_dict())
        assert res["valid"] is True


def test_bootstrap_simulation_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_bootstrap_simulation_contract_registry(profile)
    assert not df.empty
    assert summary["total_methods"] >= 3
    assert summary["all_unexecuted"] is True


def test_block_bootstrap_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_block_bootstrap_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 3
    assert summary["all_unexecuted"] is True


def test_stationary_bootstrap_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_stationary_bootstrap_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 2
    assert summary["all_unexecuted"] is True


def test_return_path_resampling_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_return_path_resampling_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 3
    assert summary["all_unexecuted"] is True


def test_trade_sequence_reshuffling_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_trade_sequence_reshuffling_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 3
    assert summary["all_unexecuted"] is True
