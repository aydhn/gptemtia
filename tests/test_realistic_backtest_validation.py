# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Validation."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_validation import (
    build_realistic_backtest_validation_report,
    validate_no_forbidden_backtest_claims,
)


def test_build_validation_report():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_backtest_validation_report(profile=prof)
    assert not df.empty
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["all_passed"] is True
    assert summary["forbidden_claims_found"] == 0
    assert summary["non_signal"] is True


def test_validate_forbidden_claims_scanner():
    clean_text = "This module is local_only, non-production, dry_run=True, with zero live trading."
    res_clean = validate_no_forbidden_backtest_claims(text=clean_text)
    assert res_clean["is_clean"] is True

    dirty_text = "We have production_ready algorithm with guaranteed_return."
    res_dirty = validate_no_forbidden_backtest_claims(text=dirty_text)
    assert res_dirty["is_clean"] is False
