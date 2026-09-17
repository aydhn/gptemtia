# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Validation and Bias Guards, Policies, Dependencies."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.validation_no_lookahead_guards import (
    build_validation_no_lookahead_guard_registry,
    validate_validation_no_lookahead_columns,
)
from advanced_walk_forward_validation.validation_purge_embargo_guards import (
    build_validation_purge_embargo_guard_registry,
)
from advanced_walk_forward_validation.validation_data_snooping_bias_guards import (
    build_validation_data_snooping_bias_guard_registry,
)
from advanced_walk_forward_validation.validation_overfitting_guards import (
    build_validation_overfitting_guard_registry,
)
from advanced_walk_forward_validation.validation_survivorship_bias_guards import (
    build_validation_survivorship_bias_guard_registry,
)
from advanced_walk_forward_validation.validation_multiple_testing_guards import (
    build_validation_multiple_testing_guard_registry,
)
from advanced_walk_forward_validation.validation_metadata_only_news_guards import (
    build_validation_metadata_only_news_guard_registry,
)
from advanced_walk_forward_validation.validation_source_preservation_guards import (
    build_validation_source_preservation_guard_registry,
)
from advanced_walk_forward_validation.validation_forbidden_column_policies import (
    build_validation_forbidden_column_policy_registry,
    validate_validation_forbidden_columns,
)
from advanced_walk_forward_validation.validation_backtest_dependencies import (
    build_validation_backtest_dependency_registry,
)
from advanced_walk_forward_validation.validation_data_contracts import (
    build_validation_data_contract_registry,
)


def test_validation_guards_and_policies():
    prof = get_default_walk_forward_profile()

    df_nl, s_nl = build_validation_no_lookahead_guard_registry(prof)
    assert not df_nl.empty
    assert s_nl["strict_enforcement"] is True
    # Test lookahead column validator
    valid_res = validate_validation_no_lookahead_columns(["timestamp", "close", "volume"])
    assert valid_res["is_valid"] is True
    invalid_res = validate_validation_no_lookahead_columns(["timestamp", "close", "future_return"])
    assert invalid_res["is_valid"] is False

    df_pe, s_pe = build_validation_purge_embargo_guard_registry(prof)
    assert not df_pe.empty

    df_ds, s_ds = build_validation_data_snooping_bias_guard_registry(prof)
    assert not df_ds.empty

    df_of, s_of = build_validation_overfitting_guard_registry(prof)
    assert not df_of.empty

    df_sb, s_sb = build_validation_survivorship_bias_guard_registry(prof)
    assert not df_sb.empty

    df_mt, s_mt = build_validation_multiple_testing_guard_registry(prof)
    assert not df_mt.empty

    df_nw, s_nw = build_validation_metadata_only_news_guard_registry(prof)
    assert not df_nw.empty

    df_sp, s_sp = build_validation_source_preservation_guard_registry(prof)
    assert not df_sp.empty

    df_fc, s_fc = build_validation_forbidden_column_policy_registry(prof)
    assert not df_fc.empty
    # Test forbidden column check
    col_res = validate_validation_forbidden_columns(["timestamp", "close", "future_price"])
    assert col_res["is_valid"] is True  # future_price is not in FORBIDDEN_COLUMNS directly unless matched

    col_res_bad = validate_validation_forbidden_columns(["timestamp", "close", "future_return"])
    assert col_res_bad["is_valid"] is False
    assert "future_return" in col_res_bad["violating_columns"]

    col_res_ok = validate_validation_forbidden_columns(["timestamp", "close", "volume"])
    assert col_res_ok["is_valid"] is True

    df_dep, s_dep = build_validation_backtest_dependency_registry(prof)
    assert not df_dep.empty

    df_dc, s_dc = build_validation_data_contract_registry(prof)
    assert not df_dc.empty
