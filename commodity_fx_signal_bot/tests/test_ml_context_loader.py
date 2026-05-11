import pytest
from ml_integration.context_loader import MLContextIntegrationLoader
from config.symbols import get_symbol_spec

class MockDataLake:
    def list_ml_integration_reports(self, *args, **kwargs):
        import pandas as pd
        return pd.DataFrame()
    def has_features(self, *args, **kwargs):
        return False
    def load_features(self, *args, **kwargs):
        import pandas as pd
        return pd.DataFrame()
    def load_candidates(self, *args, **kwargs):
        import pandas as pd
        return pd.DataFrame()

def test_context_loader():
    dl = MockDataLake()
    loader = MLContextIntegrationLoader(dl)
    spec = get_symbol_spec("GC=F")

    df, summary = loader.load_ml_prediction_context(spec, "1d")
    assert df.empty
    assert summary["status"] == "unavailable"

    frames, sum2 = loader.load_candidate_context_frames(spec, "1d")
    assert isinstance(frames, dict)
    assert "loaded" in sum2
