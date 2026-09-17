# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Walk-Forward Split Contracts and Boundaries."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_validation_contracts import (
    build_walk_forward_validation_contract_registry,
)
from advanced_walk_forward_validation.rolling_window_validation_contracts import (
    build_rolling_window_validation_contract_registry,
)
from advanced_walk_forward_validation.expanding_window_validation_contracts import (
    build_expanding_window_validation_contract_registry,
)
from advanced_walk_forward_validation.anchored_window_validation_contracts import (
    build_anchored_window_validation_contract_registry,
)
from advanced_walk_forward_validation.purged_walk_forward_contracts import (
    build_purged_walk_forward_contract_registry,
)
from advanced_walk_forward_validation.embargo_policies import (
    build_embargo_policy_registry,
)
from advanced_walk_forward_validation.train_validation_test_split_contracts import (
    build_train_validation_test_split_contract_registry,
)
from advanced_walk_forward_validation.out_of_sample_split_contracts import (
    build_out_of_sample_split_contract_registry,
)
from advanced_walk_forward_validation.holdout_period_contracts import (
    build_holdout_period_contract_registry,
)
from advanced_walk_forward_validation.temporal_split_boundaries import (
    build_temporal_split_boundary_registry,
)
from advanced_walk_forward_validation.regime_aware_split_contracts import (
    build_regime_aware_split_contract_registry,
)
from advanced_walk_forward_validation.cross_asset_oos_split_contracts import (
    build_cross_asset_oos_split_contract_registry,
)
from advanced_walk_forward_validation.walk_forward_fold_contracts import (
    build_walk_forward_fold_contract_registry,
)
from advanced_walk_forward_validation.walk_forward_schedule_placeholders import (
    build_walk_forward_schedule_placeholder_registry,
)


def test_split_contracts():
    prof = get_default_walk_forward_profile()

    df_wf, s_wf = build_walk_forward_validation_contract_registry(prof)
    assert not df_wf.empty
    assert s_wf["all_execution_blocked"] is True
    assert (df_wf["walk_forward_execution_allowed"] == False).all()

    df_roll, s_roll = build_rolling_window_validation_contract_registry(prof)
    assert not df_roll.empty
    assert s_roll["all_execution_blocked"] is True

    df_exp, s_exp = build_expanding_window_validation_contract_registry(prof)
    assert not df_exp.empty
    assert s_exp["all_execution_blocked"] is True

    df_anc, s_anc = build_anchored_window_validation_contract_registry(prof)
    assert not df_anc.empty
    assert s_anc["all_execution_blocked"] is True

    df_prg, s_prg = build_purged_walk_forward_contract_registry(prof)
    assert not df_prg.empty
    assert s_prg["all_execution_blocked"] is True

    df_emb, s_emb = build_embargo_policy_registry(prof)
    assert not df_emb.empty
    assert s_emb["all_policies_enforced"] is True

    df_tvt, s_tvt = build_train_validation_test_split_contract_registry(prof)
    assert not df_tvt.empty
    assert s_tvt["all_splits_unexecuted"] is True

    df_oos, s_oos = build_out_of_sample_split_contract_registry(prof)
    assert not df_oos.empty
    assert s_oos["zero_split_executed"] is True

    df_hld, s_hld = build_holdout_period_contract_registry(prof)
    assert not df_hld.empty
    assert s_hld["all_sealed"] is True

    df_tmp, s_tmp = build_temporal_split_boundary_registry(prof)
    assert not df_tmp.empty
    assert s_tmp["all_chronological"] is True

    df_reg, s_reg = build_regime_aware_split_contract_registry(prof)
    assert not df_reg.empty
    assert s_reg["all_splits_unexecuted"] is True

    df_crx, s_crx = build_cross_asset_oos_split_contract_registry(prof)
    assert not df_crx.empty
    assert s_crx["all_transfers_unexecuted"] is True

    df_fld, s_fld = build_walk_forward_fold_contract_registry(prof)
    assert not df_fld.empty
    assert s_fld["all_folds_unexecuted"] is True

    df_sch, s_sch = build_walk_forward_schedule_placeholder_registry(prof)
    assert not df_sch.empty
    assert s_sch["all_real_jobs_disabled"] is True
    assert s_sch["zero_scheduler_active"] is True
