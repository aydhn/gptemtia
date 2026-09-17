# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Timestamp Integrity Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.timestamp_integrity_governance import (
    build_timestamp_integrity_governance_registry,
    validate_timestamp_integrity_request,
    TIMESTAMP_RULES,
)


def test_build_timestamp_integrity_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_timestamp_integrity_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "rule_id" in df.columns
    assert "rule_name" in df.columns
    assert (df["status"] == "ACTIVE").all()
    assert summary["total_rules"] == 3
    assert summary["future_joins_strictly_prohibited"] is True
    assert len(TIMESTAMP_RULES) == 3


def test_validate_timestamp_integrity_request():
    blocked_req = validate_timestamp_integrity_request("future_join on next bars")
    assert blocked_req["is_allowed"] is False
    assert blocked_req["is_blocked"] is True

    allowed_req = validate_timestamp_integrity_request("point_in_time asof join on historical bars")
    assert allowed_req["is_allowed"] is True
    assert allowed_req["is_blocked"] is False
