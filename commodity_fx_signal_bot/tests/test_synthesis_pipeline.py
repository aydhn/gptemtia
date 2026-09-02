import pytest
from pathlib import Path
from local_synthesis.synthesis_pipeline import LocalSynthesisPipeline
from config.settings import Settings

class MockDataLake:
    pass

def test_synthesis_pipeline():
    pipeline = LocalSynthesisPipeline(MockDataLake(), Settings(), Path("."))
    data, summary = pipeline.build_synthesis_profile_registry(save=False)
    assert "status" in summary
