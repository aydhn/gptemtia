import pytest
from pathlib import Path
import pandas as pd
from command_center.phase_coverage import (
    parse_phase_log,
    infer_phase_modules,
    build_phase_coverage_matrix,
    summarize_phase_coverage
)

def test_parse_phase_log(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "PHASE_LOG.md").write_text("## Phase 50: Command Center\nSome text.", encoding="utf-8")

    df = parse_phase_log(tmp_path)
    assert not df.empty
    assert df.iloc[0]["phase_number"] == 50

def test_build_phase_coverage_matrix(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "PHASE_LOG.md").write_text("## Phase 50: command_center\nSome text.", encoding="utf-8")

    (tmp_path / "command_center").mkdir()

    df = build_phase_coverage_matrix(tmp_path)
    assert not df.empty

    # command_center should be marked covered
    cc_row = df[df["expected_module"] == "command_center"]
    assert not cc_row.empty
    assert cc_row.iloc[0]["status"] == "covered"

def test_summarize_phase_coverage():
    df = pd.DataFrame([
        {"status": "covered"},
        {"status": "missing"}
    ])
    summary = summarize_phase_coverage(df)
    assert summary["phases_covered"] == 1
    assert summary["phases_missing"] == 1
