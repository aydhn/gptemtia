import pandas as pd
from pathlib import Path
from quality_gates.output_contracts import (
    validate_report_output_folders,
    validate_data_lake_output_folders,
    validate_expected_status_outputs,
    validate_csv_json_markdown_outputs,
    build_output_contract_validation_report
)

def test_validate_report_output_folders():
    df = validate_report_output_folders(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_validate_data_lake_output_folders():
    df = validate_data_lake_output_folders(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_validate_expected_status_outputs():
    df = validate_expected_status_outputs(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_validate_csv_json_markdown_outputs():
    df = validate_csv_json_markdown_outputs(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_build_output_contract_validation_report():
    df, summary = build_output_contract_validation_report(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
