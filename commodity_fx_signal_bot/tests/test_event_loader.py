import pytest
import pandas as pd
from config.symbols import get_symbol_spec
from signals.event_loader import EventLoader


class MockDataLake:
    def has_features(self, spec, timeframe, feature_set_name):
        return True

    def load_features(self, spec, timeframe, feature_set_name):
        return pd.DataFrame(
            {"bullish": [True, False]}, index=pd.date_range("2023-01-01", periods=2)
        )


class MockFeatureStore:
    def load_macro_events(self):
        return pd.DataFrame(
            {"macro": [1, 2]}, index=pd.date_range("2023-01-01", periods=2)
        )

    def load_asset_profile_events(self, spec, timeframe):
        return pd.DataFrame(
            {"asset_profile": [1, 2]}, index=pd.date_range("2023-01-01", periods=2)
        )

    def load_mtf_features(self, spec, timeframe):
        return pd.DataFrame({"a": [1]})

    def load_regime_features(self, spec, timeframe):
        return pd.DataFrame({"a": [1]})

    def load_macro_features(self):
        return pd.DataFrame({"a": [1]})

    def load_asset_profile_features(self, spec, timeframe):
        return pd.DataFrame({"a": [1]})


def test_load_event_frames():
    dl = MockDataLake()
    loader = EventLoader(dl)
    loader.feature_store = MockFeatureStore()

    spec = get_symbol_spec("GC=F")

    frames, summary = loader.load_event_frames(
        spec, "1d", ("momentum", "trend", "unknown_group")
    )
    assert "momentum" in frames
    assert "trend" in frames
    assert "unknown_group" not in frames
    assert "unknown_group" in summary["missing_event_groups"]


def test_load_context_frames():
    dl = MockDataLake()
    loader = EventLoader(dl)
    loader.feature_store = MockFeatureStore()

    spec = get_symbol_spec("GC=F")

    frames, summary = loader.load_context_frames(spec, "1d")
    assert "technical" in frames
    assert "trend" in frames
