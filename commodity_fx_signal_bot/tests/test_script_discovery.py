import pytest
from pathlib import Path
from command_center.script_discovery import (
    classify_script,
    infer_script_module,
    discover_scripts,
    build_script_availability_matrix,
    summarize_script_discovery
)

def test_classify_script():
    assert classify_script(Path("run_abc_status.py")) == "status_script"
    assert classify_script(Path("run_abc_report.py")) == "report_script"
    assert classify_script(Path("run_abc_query.py")) == "query_script"
    assert classify_script(Path("run_abc.py")) == "pipeline_script"
    assert classify_script(Path("abc.py")) == "unknown_script"

def test_infer_script_module():
    assert infer_script_module(Path("run_modulea_status.py")) == "modulea"
    assert infer_script_module(Path("run_moduleb_report.py")) == "moduleb"

def test_script_discovery(tmp_path):
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir()
    (scripts_dir / "run_test_status.py").write_text("print('hello')", encoding="utf-8")
    (scripts_dir / "run_live_trading.py").write_text("print('live order')", encoding="utf-8")

    df = discover_scripts(tmp_path)
    assert not df.empty

    warnings_list = [w for ws in df["warnings"] for w in ws]
    assert "potentially_unsafe_content" in warnings_list

def test_script_availability_matrix(tmp_path):
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir()
    (scripts_dir / "run_test_status.py").write_text("print('hello')", encoding="utf-8")

    df = build_script_availability_matrix(tmp_path)
    assert not df.empty
    assert "status_script" in df.columns
