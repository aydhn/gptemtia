"""Unit tests for Phase 119 master orchestration pipeline and data lake saves."""

import pytest
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_cross_asset_alignment.cross_asset_alignment_config import get_default_cross_asset_alignment_profile
from advanced_cross_asset_alignment.cross_asset_alignment_pipeline import CrossAssetAlignmentPipeline


def test_cross_asset_alignment_pipeline_run_full():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_cross_asset_alignment_profile()

    pipeline = CrossAssetAlignmentPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    result = pipeline.run_full_pipeline(save=True)
    assert result["phase"] == 119
    assert result["target_final_phase"] == 160
    assert result["next_phase"] == 120
    assert result["pipeline_status"] == "SUCCESS"
    assert result["non_signal"] is True
    assert result["future_data_allowed"] is False
    assert result["total_tables_generated"] >= 25
