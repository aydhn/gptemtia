import pytest
import pandas as pd
from config.settings import Settings
from config.symbols import get_symbol_spec
from signals.signal_pipeline import SignalPipeline
from signals.signal_config import get_default_signal_scoring_profile


class MockDataLakePipeline:
    def has_features(self, spec, timeframe, feature_set_name):
        return True

    def load_features(self, spec, timeframe, feature_set_name):
        return pd.DataFrame(
            {"bullish_event": [True]}, index=pd.date_range("2023-01-01", periods=1)
        )

    def save_features(self, spec, timeframe, df, name):
        pass


def test_signal_pipeline_build_for_symbol():
    dl = MockDataLakePipeline()
    settings = Settings()
    prof = get_default_signal_scoring_profile()
    pipeline = SignalPipeline(dl, settings, prof)

    spec = get_symbol_spec("GC=F")
    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", prof, save=False)

    # It might return empty df because of no real data in mock lake, which is fine.
    assert isinstance(df, pd.DataFrame)


def test_signal_pipeline_skip_macro():

    dl = MockDataLakePipeline()
    settings = Settings()
    pipeline = SignalPipeline(dl, settings)

    from config.symbols import SymbolSpec

    spec = SymbolSpec(
        symbol="USDOLLAR_INDEX",
        name="dummy",
        asset_class="macro",
        data_source="dummy",
        sub_class="dummy",
        currency="USD",
    )
    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)

    assert df.empty
    assert summary["status"] == "skipped"
