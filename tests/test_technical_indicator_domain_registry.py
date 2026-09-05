from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_domain_registry import build_technical_indicator_domain_registry


def test_technical_indicator_domain_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_technical_indicator_domain_registry(prof)

    assert not df.empty
    assert len(df) >= 20
    assert summary["status"] == "READY"
    assert "price_action_domain" in df["domain_label"].values
    assert "moving_average_domain" in df["domain_label"].values
