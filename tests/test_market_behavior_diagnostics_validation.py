from advanced_market_behavior_diagnostics.market_behavior_diagnostics_validation import (
    build_market_behavior_diagnostics_validation_report,
    validate_no_lookahead_behavior_diagnostics,
    validate_no_forbidden_behavior_claims,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)


def test_market_behavior_diagnostics_validation():
    profile = get_default_market_behavior_diagnostics_profile()
    df, summary = build_market_behavior_diagnostics_validation_report(profile=profile)

    assert not df.empty
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True


def test_validation_guards():
    profile = get_default_market_behavior_diagnostics_profile()
    assert validate_no_lookahead_behavior_diagnostics(profile) is True
    assert validate_no_forbidden_behavior_claims(profile) is True
