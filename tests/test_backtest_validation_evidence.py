# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Validation Evidence."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_validation_evidence import (
    build_backtest_validation_evidence_registry,
)


def test_build_validation_evidence():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_validation_evidence_registry(prof)
    assert not df.empty
    assert len(df) >= 6
    assert summary["all_verified"] is True
    assert summary["non_signal"] is True
    assert (df["verified"] == True).all()
