"""Test pipeline."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_pipeline import LocalReproducibilityGovernancePipeline
from pathlib import Path

class DummyDataLake:
    pass
class DummySettings:
    pass

def test_pipeline():
    pipeline = LocalReproducibilityGovernancePipeline(DummyDataLake(), DummySettings(), Path("."))
    text, summary = pipeline.build_reproducibility_dossier(save=False)
    assert text
