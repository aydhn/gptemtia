# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Result Disclosure Placeholders."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_result_disclosure_placeholders import (
    build_backtest_result_disclosure_placeholder_registry,
    DISCLOSURE_PLACEHOLDERS,
)


def test_build_backtest_result_disclosure_placeholders():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_result_disclosure_placeholder_registry(profile)

    assert not df.empty
    assert len(df) == 6
    assert "section_id" in df.columns
    assert "section_title" in df.columns
    assert (df["non_signal"] == True).all()
    assert (df["local_only"] == True).all()
    assert summary["total_disclosures"] == 6
    assert len(DISCLOSURE_PLACEHOLDERS) == 6
