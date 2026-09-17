# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Transaction Cost Shock Contracts."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.transaction_cost_shock_contracts import (
    build_transaction_cost_shock_contract_registry,
)


def test_transaction_cost_shock_contracts():
    prof = get_default_stress_testing_profile()
    df, summary = build_transaction_cost_shock_contract_registry(prof)
    assert not df.empty
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
