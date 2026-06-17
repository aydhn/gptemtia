import pytest
from unittest.mock import MagicMock
from pathlib import Path
from local_timeline.timeline_pipeline import LocalTimelinePipeline
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_pipeline_initialization():
    mock_data_lake = MagicMock()
    mock_settings = MagicMock()
    profile = get_default_local_timeline_profile()

    pipeline = LocalTimelinePipeline(mock_data_lake, mock_settings, Path("."), profile)
    assert pipeline.profile.name == "balanced_local_timeline"

def test_build_project_event_registry_no_save():
    mock_data_lake = MagicMock()
    mock_settings = MagicMock()
    profile = get_default_local_timeline_profile()

    pipeline = LocalTimelinePipeline(mock_data_lake, mock_settings, Path("."), profile)
    df, summary = pipeline.build_project_event_registry(save=False)

    assert "total_events" in summary
    mock_data_lake.save_project_event_registry.assert_not_called()

def test_build_timeline_status_no_save():
    mock_data_lake = MagicMock()
    mock_settings = MagicMock()
    profile = get_default_local_timeline_profile()

    pipeline = LocalTimelinePipeline(mock_data_lake, mock_settings, Path("."), profile)
    df, summary = pipeline.build_timeline_status(save=False)

    assert "total_files" in summary
