from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.quote_feature_catalog import build_quote_feature_catalog


def test_quote_feature_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_quote_feature_catalog(profile)

    assert not df.empty
    assert len(df) >= 4
    names = df["feature_name"].tolist()
    assert "bid_ask_spread" in names
    assert "bid_ask_spread_pct" in names
    assert "mid_price" in names
    assert summary["all_non_signal"] is True
