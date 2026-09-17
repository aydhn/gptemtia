# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Labels."""

from advanced_stress_testing.stress_testing_labels import (
    DOMAIN_LABELS,
    STRESS_CONTRACT_READY,
    EXECUTION_BLOCKED_NO_STRESS_TEST,
    EXECUTION_CONTRACT_ONLY,
)


def test_labels():
    assert len(DOMAIN_LABELS) >= 30
    assert STRESS_CONTRACT_READY == "stress_contract_ready"
    assert EXECUTION_BLOCKED_NO_STRESS_TEST == "execution_blocked_no_stress_test"
    assert EXECUTION_CONTRACT_ONLY == "execution_contract_only"
