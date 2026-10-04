"""Unit tests for Risk Reporting Alert Claim Guards."""

from advanced_risk_reporting.risk_reporting_alert_claim_guards import (
    build_risk_reporting_alert_claim_guard_registry,
    validate_alert_claim_request,
)
from advanced_risk_reporting.risk_reporting_config import (
    get_default_risk_reporting_profile,
)


def test_build_risk_reporting_alert_claim_guard_registry():
    """Test registry building for alert claim guards."""
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_alert_claim_guard_registry(profile)

    assert not df.empty
    assert "guard_name" in df.columns
    assert "is_active" in df.columns
    assert "current_phase" in df.columns
    assert summary["all_active"] is True
    assert summary["guard_count"] == len(df)
    assert (df["is_active"] == True).all()


def test_validate_alert_claim_request_allowed():
    """Test validation allows safe requests."""
    safe_requests = [
        "check system status",
        "calculate metrics",
        {"message": "analyze data"},
        "nothing related to alerting",
    ]

    for req in safe_requests:
        res = validate_alert_claim_request(req)
        assert res["is_blocked"] is False
        assert res["is_safe"] is True
        assert res["action"] == "ALLOW"
        assert res["reason"] == "No violation"


def test_validate_alert_claim_request_blocked():
    """Test validation blocks requests with prohibited claims."""
    blocked_requests = [
        "please send_alert now",
        "i need to dispatch_alert",
        "this is a live_alert test",
        "emit_notification to user",
        {"action": "send to pagerduty"},
        "trigger slack_webhook",
    ]

    for req in blocked_requests:
        res = validate_alert_claim_request(req)
        assert res["is_blocked"] is True
        assert res["is_safe"] is False
        assert res["action"] == "BLOCK"
        assert "prohibited" in res["reason"].lower()
