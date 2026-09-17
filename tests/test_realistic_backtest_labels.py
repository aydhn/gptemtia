# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Labels."""

from advanced_realistic_backtest.realistic_backtest_labels import (
    DOMAIN_LABELS,
    STATUS_LABELS,
    EXECUTION_LABELS,
    EVENT_DRIVEN_CONTRACT_DOMAIN,
    SLIPPAGE_MODEL_DOMAIN,
    TRANSACTION_COST_DOMAIN,
    BIAS_GUARD_DOMAIN,
    BACKTEST_CONTRACT_READY,
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    get_domain_label_description,
    get_status_label_description,
    get_execution_label_description,
)


def test_domain_labels():
    assert len(DOMAIN_LABELS) >= 30
    assert EVENT_DRIVEN_CONTRACT_DOMAIN in DOMAIN_LABELS
    assert SLIPPAGE_MODEL_DOMAIN in DOMAIN_LABELS
    assert TRANSACTION_COST_DOMAIN in DOMAIN_LABELS
    assert BIAS_GUARD_DOMAIN in DOMAIN_LABELS


def test_status_labels():
    assert BACKTEST_CONTRACT_READY in STATUS_LABELS
    assert "backtest_contract_ready_with_warnings" in STATUS_LABELS
    assert "backtest_contract_manual_review_required" in STATUS_LABELS
    assert "backtest_contract_blocked_by_safety" in STATUS_LABELS
    assert "backtest_contract_only" in STATUS_LABELS


def test_execution_labels():
    assert EXECUTION_BLOCKED_NO_LIVE_TRADING in EXECUTION_LABELS
    assert "execution_blocked_no_broker" in EXECUTION_LABELS
    assert "execution_blocked_no_optimizer" in EXECUTION_LABELS
    assert "execution_blocked_no_walk_forward" in EXECUTION_LABELS
    assert "execution_contract_only" in EXECUTION_LABELS


def test_label_descriptions():
    desc = get_domain_label_description(SLIPPAGE_MODEL_DOMAIN)
    assert isinstance(desc, str) and len(desc) > 0
    stat_desc = get_status_label_description(BACKTEST_CONTRACT_READY)
    assert isinstance(stat_desc, str) and len(stat_desc) > 0
    exec_desc = get_execution_label_description(EXECUTION_BLOCKED_NO_LIVE_TRADING)
    assert isinstance(exec_desc, str) and len(exec_desc) > 0
