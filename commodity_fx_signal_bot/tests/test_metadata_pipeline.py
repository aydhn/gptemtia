import pandas as pd
import pytest
from pathlib import Path
from artifact_metadata.metadata_pipeline import ArtifactMetadataPipeline
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

class MockDataLake:
    pass

def test_pipeline_methods():
    profile = get_default_artifact_metadata_profile()
    pipeline = ArtifactMetadataPipeline(MockDataLake(), None, Path("/dummy"), profile)

    # Just checking they don't crash and return expected structure
    df, s1 = pipeline.build_research_artifact_inventory(save=False)
    assert isinstance(s1, dict)

    t2, s2 = pipeline.build_model_dataset_cards(save=False)
    assert "model_cards" in t2

    t3, s3 = pipeline.build_experiment_reproducibility_cards(save=False)
    assert "reproducibility_cards" in t3

    t4, s4 = pipeline.build_scenario_regression_cards(save=False)
    assert "scenario_cards" in t4

    t5, s5 = pipeline.build_research_metadata_export(save=False)
    assert "export_index" in t5

    q_rep, s6 = pipeline.build_metadata_quality_report(save=False)
    assert "passed" in q_rep
