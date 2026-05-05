from decisions.neutral_filter import should_mark_neutral, should_mark_no_trade
from decisions.decision_config import get_default_decision_profile


def test_should_mark_neutral():
    assert should_mark_neutral(0.4, 0.5) is True
    assert should_mark_neutral(0.6, 0.1, neutral_zone_threshold=0.15) == True
    assert should_mark_neutral(0.6, 0.2, neutral_zone_threshold=0.15) == False


def test_should_mark_no_trade():
    prof = get_default_decision_profile()
    is_nt, reasons = should_mark_no_trade(0.1, 0.9, 0.1, prof)
    assert is_nt is True
    assert len(reasons) > 0
