# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Source Preservation Guards."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_source_preservation_guards import (
    build_backtest_source_preservation_guard_registry,
    validate_backtest_source_preservation_action,
    SOURCE_PRESERVATION_RULES,
)


def test_build_backtest_source_preservation_guards():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_source_preservation_guard_registry(profile)

    assert not df.empty
    assert len(df) == 4
    assert "guard_id" in df.columns
    assert "guard_name" in df.columns
    assert (df["status"] == "ACTIVE").all()
    assert summary["all_active"] is True
    assert summary["total_guards"] == 4
    assert len(SOURCE_PRESERVATION_RULES) == 4


def test_validate_backtest_source_preservation_action():
    blocked = validate_backtest_source_preservation_action("overwrite raw data")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_backtest_source_preservation_action("read-only inspect contracts")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
