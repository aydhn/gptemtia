# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Disabled Execution Reports."""

import pytest
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_execution_disabled import (
    build_stress_execution_disabled_report,
)
from advanced_stress_testing.scenario_simulation_disabled import (
    build_scenario_simulation_disabled_report,
)
from advanced_stress_testing.stress_metric_calculation_disabled import (
    build_stress_metric_calculation_disabled_report,
)
from advanced_stress_testing.stress_live_trading_disabled import (
    build_stress_live_trading_disabled_report,
)
from advanced_stress_testing.stress_broker_execution_disabled import (
    build_stress_broker_execution_disabled_report,
)
from advanced_stress_testing.stress_optimizer_disabled import (
    build_stress_optimizer_disabled_report,
)
from advanced_stress_testing.stress_model_training_disabled import (
    build_stress_model_training_disabled_report,
)
from advanced_stress_testing.stress_prediction_disabled import (
    build_stress_prediction_disabled_report,
)
from advanced_stress_testing.stress_performance_claim_disabled import (
    build_stress_performance_claim_disabled_report,
)


@pytest.fixture
def profile():
    return get_default_stress_testing_profile()


def test_core_disabled_execution_reports(profile):
    df_st, s_st = build_stress_execution_disabled_report(profile)
    assert not df_st.empty
    assert s_st["is_blocked"] is True
    assert s_st["enforced"] is True
    assert s_st["non_signal"] is True

    df_sc, s_sc = build_scenario_simulation_disabled_report(profile)
    assert not df_sc.empty
    assert s_sc["is_blocked"] is True
    assert s_sc["enforced"] is True

    df_mc, s_mc = build_stress_metric_calculation_disabled_report(profile)
    assert not df_mc.empty
    assert s_mc["is_blocked"] is True
    assert s_mc["enforced"] is True


def test_trading_and_broker_disabled_reports(profile):
    df_lt, s_lt = build_stress_live_trading_disabled_report(profile)
    assert not df_lt.empty
    assert s_lt["is_blocked"] is True
    assert s_lt["enforced"] is True

    df_br, s_br = build_stress_broker_execution_disabled_report(profile)
    assert not df_br.empty
    assert s_br["is_blocked"] is True
    assert s_br["enforced"] is True


def test_model_and_claim_disabled_reports(profile):
    df_opt, s_opt = build_stress_optimizer_disabled_report(profile)
    assert not df_opt.empty
    assert s_opt["is_blocked"] is True

    df_tr, s_tr = build_stress_model_training_disabled_report(profile)
    assert not df_tr.empty
    assert s_tr["is_blocked"] is True

    df_pr, s_pr = build_stress_prediction_disabled_report(profile)
    assert not df_pr.empty
    assert s_pr["is_blocked"] is True

    df_pc, s_pc = build_stress_performance_claim_disabled_report(profile)
    assert not df_pc.empty
    assert s_pc["is_blocked"] is True
