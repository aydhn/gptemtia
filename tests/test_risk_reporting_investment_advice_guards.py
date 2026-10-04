# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Investment Advice Guards."""

import pytest
import pandas as pd
from advanced_risk_reporting.risk_reporting_investment_advice_guards import (
    build_risk_reporting_investment_advice_guard_registry,
    validate_risk_reporting_investment_advice_request,
)
from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile

def test_build_risk_reporting_investment_advice_guard_registry_with_profile():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_investment_advice_guard_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.iloc[0]["guard_name"] == "investment_advice_guard"
    assert bool(df.iloc[0]["is_active"]) is True

    assert "guard_count" in summary
    assert summary["guard_count"] == 1
    assert summary["all_active"] is True

def test_build_risk_reporting_investment_advice_guard_registry_without_profile():
    df, summary = build_risk_reporting_investment_advice_guard_registry(None)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.iloc[0]["guard_name"] == "investment_advice_guard"
    assert bool(df.iloc[0]["is_active"]) is True

    assert "guard_count" in summary
    assert summary["guard_count"] == 1
    assert summary["all_active"] is True


@pytest.mark.parametrize(
    "request_text, expected_blocked",
    [
        ("What is the current exposure to gold?", False),
        ("Show me the risk metrics for USD", False),
        ("I should buy some EUR", True),
        ("Should we SELL our positions?", True),
        ("Give me a trade_recommendation", True),
        ("Any investment_advice for today?", True),
        ("I need a position_recommendation", True),
        ("yavsiye in Turkish means advice", True),
        ("al_sat refers to buy-sell", True),
        ("Long position opened", True),
        ("SHORT the market", True),
        (12345, False), # non-string
        ({"query": "buy more"}, True), # Dict containing prohibited word
        ({"query": "show risk"}, False), # Dict not containing prohibited word
    ],
)
def test_validate_risk_reporting_investment_advice_request(request_text, expected_blocked):
    result = validate_risk_reporting_investment_advice_request(request_text)

    assert result["is_blocked"] == expected_blocked
    assert result["is_safe"] == (not expected_blocked)

    if expected_blocked:
        assert result["action"] == "BLOCK"
        assert result["reason"] == "Investment advice strictly prohibited"
    else:
        assert result["action"] == "ALLOW"
        assert result["reason"] == "No violation"
