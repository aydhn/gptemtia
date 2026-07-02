import pytest
from pathlib import Path
from unittest.mock import MagicMock
from local_archive.archive_pipeline import LocalArchivePipeline
from local_archive.archive_config import get_default_local_archive_profile

def test_archive_pipeline(tmp_path):
    mock_lake = MagicMock()
    mock_settings = MagicMock()

    # Just touch a file
    (tmp_path / "test.txt").write_text("Hello")

    pipeline = LocalArchivePipeline(
        data_lake=mock_lake,
        settings=mock_settings,
        project_root=tmp_path,
        profile=get_default_local_archive_profile()
    )

    # Run the core parts with save=True to see if it invokes datalake
    dfs, sum1 = pipeline.build_archive_domain_registry(save=True)
    assert mock_lake.save_archive_domain_registry.called

    dfs2, sum2 = pipeline.build_project_snapshot_catalog(save=True)
    assert mock_lake.save_project_snapshot_catalog.called

    dfs3, sum3 = pipeline.build_cold_storage_manifest(save=True)
    assert mock_lake.save_cold_storage_manifest.called

    dfs4, sum4 = pipeline.build_archive_integrity_plan(save=True)
    assert mock_lake.save_archive_integrity_verification_plan.called

    txt, sum5 = pipeline.build_preservation_binder(save=True)
    assert mock_lake.save_long_horizon_preservation_binder.called

    qual, sum6 = pipeline.build_archive_quality_report(save=True)
    assert mock_lake.save_archive_quality.called

    stat, sum7 = pipeline.build_archive_status(save=False)
    assert not stat.empty
