# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Findings."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_findings import (
    build_backtest_findings_registry,
    create_backtest_finding,
)


def test_build_findings():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_findings_registry(prof)
    assert not df.empty
    assert summary["total_findings"] >= 1
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()


def test_create_finding_helper():
    finding = create_backtest_finding(
        finding_type="CONTRACT_CHECK",
        domain="execution",
        severity_label="LOW",
        message="Minor documentation gap",
        recommendation="Document order assumptions",
    )
    assert finding.domain == "execution"
    assert finding.manual_review_required is True
