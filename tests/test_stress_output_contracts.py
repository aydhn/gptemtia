# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Output Contracts."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_output_contracts import (
    build_stress_output_contract_registry,
)


def test_stress_output_contracts():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_output_contract_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
