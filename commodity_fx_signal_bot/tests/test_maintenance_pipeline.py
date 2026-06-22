import pytest
import pandas as pd
from unittest.mock import MagicMock
from pathlib import Path
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.maintenance_pipeline import LocalMaintenancePipeline

def test_maintenance_pipeline(tmp_path):
    mock_data_lake = MagicMock()
    profile = get_default_local_maintenance_profile()

    pipeline = LocalMaintenancePipeline(
        data_lake=mock_data_lake,
        settings=MagicMock(),
        project_root=tmp_path,
        profile=profile
    )

    # Test one of the methods to ensure integration works
    tables, summary = pipeline.build_maintenance_domain_registry(save=True)

    assert "domains" in tables
    assert "tasks" in tables
    assert mock_data_lake.save_maintenance_domain_registry.called
    assert mock_data_lake.save_maintenance_task_registry.called

def test_pipeline_sustainability_report(tmp_path):
    mock_data_lake = MagicMock()
    profile = get_default_local_maintenance_profile()

    pipeline = LocalMaintenancePipeline(
        data_lake=mock_data_lake,
        settings=MagicMock(),
        project_root=tmp_path,
        profile=profile
    )

    tables, summary = pipeline.build_maintenance_sustainability_report(save=True)

    assert "score" in tables
    assert mock_data_lake.save_sustainability_score_report.called
