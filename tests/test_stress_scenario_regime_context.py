# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Regime Context."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_regime_context import (
    build_stress_scenario_regime_context_registry,
)


def test_regime_context():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_scenario_regime_context_registry(prof)
    assert not df.empty
    assert summary["total_regime_contexts"] == len(df)
    assert summary["non_signal"] is True
