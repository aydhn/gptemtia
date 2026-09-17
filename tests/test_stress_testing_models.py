# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Models and Invariants."""

import pytest
from advanced_stress_testing.stress_testing_models import (
    StressTestingProfileItem,
    StressScenarioContract,
    ShockScenarioPlaceholder,
    StressMetricPlaceholder,
    StressGuardItem,
    StressDisabledExecutionItem,
    StressFinding,
    StressReadinessScore,
    StressTestingManifest,
    StressManualReviewItem,
)


def test_models_instantiation_and_invariants():
    prof_item = StressTestingProfileItem(
        profile_name="test_prof",
        description="test",
        current_phase=148,
        min_readiness_score=0.8,
    )
    assert prof_item.current_phase == 148

    with pytest.raises(ValueError):
        StressTestingProfileItem(
            profile_name="test_prof",
            description="test",
            min_readiness_score=1.5,
        )

    sc = StressScenarioContract(
        contract_name="test_sc",
        scenario_family="test_family",
        description="test",
        realistic_backtest_ref="ref1",
        walk_forward_ref="ref2",
        transaction_cost_ref="ref3",
        slippage_model_ref="ref4",
        regime_context_ref="ref5",
        no_lookahead_guard_ref="ref6",
        scenario_leakage_guard_ref="ref7",
    )
    assert sc.stress_execution_allowed is False

    with pytest.raises(ValueError):
        StressScenarioContract(
            contract_name="bad_sc",
            scenario_family="f",
            description="d",
            realistic_backtest_ref="r",
            walk_forward_ref="r",
            transaction_cost_ref="r",
            slippage_model_ref="r",
            regime_context_ref="r",
            no_lookahead_guard_ref="r",
            scenario_leakage_guard_ref="r",
            stress_execution_allowed=True,
        )
