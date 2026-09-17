# -*- coding: utf-8 -*-
"""Unit tests for Phase 152 Backtest Acceptance Labels."""

from advanced_backtest_acceptance.backtest_acceptance_labels import (
    ALL_DOMAINS,
    ALL_STATUSES,
    ALL_BOUNDARIES,
    BACKTEST_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
    NO_GO_LIVE_TRADING,
    GO_CONTRACT_ONLY,
)


def test_labels_defined():
    assert len(ALL_DOMAINS) == 27
    assert BACKTEST_ACCEPTANCE_DOMAIN in ALL_DOMAINS
    assert ACCEPTANCE_READY in ALL_STATUSES
    assert NO_GO_LIVE_TRADING in ALL_BOUNDARIES
    assert GO_CONTRACT_ONLY in ALL_BOUNDARIES
