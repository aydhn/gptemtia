import pytest
from pathlib import Path
from command_center.project_status import (
    collect_module_status_files,
    collect_latest_report_outputs,
    collect_data_lake_module_outputs,
    build_project_status_table,
    summarize_project_status
)

def test_project_status_collection():
    root = Path(".")

    df1 = collect_module_status_files(root)
    assert not df1.empty

    df2 = collect_latest_report_outputs(root)
    assert not df2.empty

    df3 = collect_data_lake_module_outputs(root)
    assert not df3.empty

def test_project_status_table():
    root = Path(".")
    df = build_project_status_table(root)
    assert not df.empty
    assert "module_name" in df.columns
    assert "status_label" in df.columns

    summary = summarize_project_status(df)
    assert summary["num_modules"] == len(df)
