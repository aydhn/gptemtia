# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Disabled Execution Safeguards and Reports."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_execution_disabled import (
    build_walk_forward_execution_disabled_report,
)
from advanced_walk_forward_validation.oos_benchmark_execution_disabled import (
    build_oos_benchmark_execution_disabled_report,
)
from advanced_walk_forward_validation.benchmark_metric_calculation_disabled import (
    build_benchmark_metric_calculation_disabled_report,
)
from advanced_walk_forward_validation.validation_optimizer_disabled import (
    build_validation_optimizer_disabled_report,
)
from advanced_walk_forward_validation.validation_model_training_disabled import (
    build_validation_model_training_disabled_report,
)
from advanced_walk_forward_validation.validation_prediction_disabled import (
    build_validation_prediction_disabled_report,
)
from advanced_walk_forward_validation.validation_live_trading_disabled import (
    build_validation_live_trading_disabled_report,
)
from advanced_walk_forward_validation.validation_broker_execution_disabled import (
    build_validation_broker_execution_disabled_report,
)
from advanced_walk_forward_validation.validation_performance_claim_disabled import (
    build_validation_performance_claim_disabled_report,
)


def test_disabled_execution_reports():
    prof = get_default_walk_forward_profile()

    df_wf, s_wf = build_walk_forward_execution_disabled_report(prof)
    assert not df_wf.empty
    assert s_wf["all_blocked"] is True
    assert (df_wf["is_blocked"] == True).all()

    df_bm, s_bm = build_oos_benchmark_execution_disabled_report(prof)
    assert not df_bm.empty
    assert s_bm["all_blocked"] is True
    assert (df_bm["is_blocked"] == True).all()

    df_mc, s_mc = build_benchmark_metric_calculation_disabled_report(prof)
    assert not df_mc.empty
    assert s_mc["all_blocked"] is True
    assert (df_mc["is_blocked"] == True).all()

    df_opt, s_opt = build_validation_optimizer_disabled_report(prof)
    assert not df_opt.empty
    assert s_opt["all_blocked"] is True
    assert (df_opt["is_blocked"] == True).all()

    df_tr, s_tr = build_validation_model_training_disabled_report(prof)
    assert not df_tr.empty
    assert s_tr["all_blocked"] is True
    assert (df_tr["is_blocked"] == True).all()

    df_pr, s_pr = build_validation_prediction_disabled_report(prof)
    assert not df_pr.empty
    assert s_pr["all_blocked"] is True
    assert (df_pr["is_blocked"] == True).all()

    df_lv, s_lv = build_validation_live_trading_disabled_report(prof)
    assert not df_lv.empty
    assert s_lv["all_blocked"] is True
    assert (df_lv["is_blocked"] == True).all()

    df_br, s_br = build_validation_broker_execution_disabled_report(prof)
    assert not df_br.empty
    assert s_br["all_blocked"] is True
    assert (df_br["is_blocked"] == True).all()

    df_cl, s_cl = build_validation_performance_claim_disabled_report(prof)
    assert not df_cl.empty
    assert s_cl["all_blocked"] is True
    assert (df_cl["is_blocked"] == True).all()
