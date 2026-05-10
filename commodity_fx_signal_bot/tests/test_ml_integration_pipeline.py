import pytest
from config.settings import Settings
from config.symbols import get_symbol_spec
from ml_integration.integration_pipeline import MLContextIntegrationPipeline

class MockDataLake:
    def __init__(self, *args, **kwargs):
        pass
    def load_features(self, *args, **kwargs):
        import pandas as pd
        return pd.DataFrame()
    def load_candidates(self, *args, **kwargs):
        import pandas as pd
        return pd.DataFrame()
    def list_feature_timeframes(self, *args, **kwargs):
        return []
    def save_ml_alignment_report(self, *args, **kwargs):
        pass
    def save_ml_conflict_report(self, *args, **kwargs):
        pass
    def save_ml_integration_quality(self, *args, **kwargs):
        pass

def test_pipeline_missing_context():
    s = Settings()
    dl = MockDataLake()
    pipeline = MLContextIntegrationPipeline(dl, s)
    spec = get_symbol_spec("GC=F")

    summary, frames = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert not summary["ml_context_available"]
    assert "quality_report" in summary
