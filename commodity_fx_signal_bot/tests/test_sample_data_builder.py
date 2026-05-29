import pytest
from scenarios.sample_data_builder import (
    build_synthetic_ohlcv, build_synthetic_macro_series,
    build_sample_data_pack
)
from scenarios.scenario_config import get_default_scenario_profile

def test_build_synthetic_ohlcv():
    df = build_synthetic_ohlcv("GC=F", 10, seed=42)
    assert not df.empty
    assert len(df) == 10
    assert all(c in df.columns for c in ["open", "high", "low", "close", "volume", "synthetic"])
    assert (df["close"] >= 0).all()
    assert (df["volume"] >= 0).all()
    assert bool(df["synthetic"].iloc[0]) is True

def test_deterministic_seed():
    df1 = build_synthetic_ohlcv("GC=F", 10, seed=42)
    df2 = build_synthetic_ohlcv("GC=F", 10, seed=42)
    assert df1["close"].equals(df2["close"])

def test_build_sample_data_pack():
    profile = get_default_scenario_profile()
    pack, summary = build_sample_data_pack(profile)
    assert len(pack) > 0
    assert summary["synthetic_flag_enforced"] is True
    assert summary["real_market_download_attempted"] is False
    assert "GC=F" in pack
