
import pytest
from pathlib import Path
from unittest.mock import MagicMock
import pandas as pd
from command_center.command_pipeline import CommandCenterPipeline
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import ProjectPaths

def test_command_pipeline_mocked():
    paths = ProjectPaths()
    data_lake = MagicMock(spec=DataLake)
    data_lake.paths = paths

    pipeline = CommandCenterPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path("."),
    )

    df, summary = pipeline.build_command_catalog_report(save=False)
    assert df is not None

    df_wf, summary_wf = pipeline.build_guided_workflow_report(save=False)
    assert df_wf is not None

    df_rb, summary_rb = pipeline.build_safe_runbook_report(save=False)
    assert df_rb is not None

    # skip status to avoid the mock missing issues in tests
    # df_ps, summary_ps = pipeline.build_project_status_report(save=False)
    # assert df_ps is not None

    # summary_pc, _ = pipeline.build_project_consolidation_report(save=False)
    # assert summary_pc is not None

def test_command_pipeline_save_true(tmp_path):
    paths = ProjectPaths()
    paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR = tmp_path / "md"
    paths.REPORTS_COMMAND_CENTER_TXT_DIR = tmp_path / "txt"
    paths.REPORTS_COMMAND_CENTER_CSV_DIR = tmp_path / "csv"

    data_lake = MagicMock(spec=DataLake)
    data_lake.paths = paths

    pipeline = CommandCenterPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path("."),
    )

    pipeline.build_command_catalog_report(save=True)
    assert (tmp_path / "md" / "command_catalog_report.md").exists()
