# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Go / No-Go Boundaries."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_go_no_go_boundaries import (
    GO_ACTIONS,
    NO_GO_ACTIONS,
    build_portfolio_acceptance_go_no_go_boundary_registry,
    validate_portfolio_acceptance_go_no_go_request,
    summarize_portfolio_acceptance_go_no_go,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    GO_NO_GO_BOUNDARY_DOMAIN,
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_UNKNOWN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_go_no_go_boundary_registry_structure():
    """Verify Go/No-Go registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_go_no_go_boundary_registry()

    assert isinstance(df, pd.DataFrame)
    total_expected = len(GO_ACTIONS) + len(NO_GO_ACTIONS)
    assert len(df) == total_expected

    expected_cols = {
        "action_name",
        "decision",
        "boundary_label",
        "description",
        "is_permitted",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)

    assert isinstance(summary, dict)
    assert summary["domain"] == GO_NO_GO_BOUNDARY_DOMAIN
    assert summary["total_rules"] == total_expected
    assert summary["go_count"] == len(GO_ACTIONS)
    assert summary["no_go_count"] == len(NO_GO_ACTIONS)
    assert summary["zero_trust_enforced"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_validate_go_request():
    """Verify permitted contract action resolves to GO."""
    res = validate_portfolio_acceptance_go_no_go_request("proceed_to_phase_158_full_system_integration_contracts")
    assert res["decision"] == "GO"
    assert res["permitted"] is True
    assert res["boundary_label"] == GO_CONTRACT_ONLY
    assert res["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_validate_no_go_request():
    """Verify prohibited action resolves to NO-GO."""
    res = validate_portfolio_acceptance_go_no_go_request("live_trading")
    assert res["decision"] == "NO-GO"
    assert res["permitted"] is False
    assert res["boundary_label"] == NO_GO_LIVE_TRADING
    assert res["status"] == "BLOCKED_BY_POLICY"

    res_dict = validate_portfolio_acceptance_go_no_go_request({"action": "portfolio_optimization"})
    assert res_dict["decision"] == "NO-GO"
    assert res_dict["permitted"] is False


def test_validate_unknown_request_zero_trust():
    """Verify unrecognized action is blocked by default."""
    res = validate_portfolio_acceptance_go_no_go_request("execute_arbitrary_unregistered_trade")
    assert res["decision"] == "NO-GO"
    assert res["permitted"] is False
    assert res["boundary_label"] == NO_GO_UNKNOWN
    assert res["status"] == "BLOCKED_BY_DEFAULT"


def test_summarize_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_go_no_go(empty_df)
    assert summary["total_rules"] == 0
    assert summary["go_count"] == 0
    assert summary["no_go_count"] == 0
