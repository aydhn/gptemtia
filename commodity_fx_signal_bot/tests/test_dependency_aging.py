import pytest
from pathlib import Path
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.dependency_aging import (
    discover_dependency_files,
    parse_requirements_file,
    parse_pyproject_dependencies,
    parse_imports_from_source,
    build_dependency_aging_watch_report
)

def test_dependency_aging_discovery(tmp_path):
    (tmp_path / "requirements.txt").touch()
    (tmp_path / "pyproject.toml").touch()

    df = discover_dependency_files(tmp_path)
    assert len(df) == 2

def test_parse_requirements(tmp_path):
    req = tmp_path / "requirements.txt"
    req.write_text("pandas==1.0.0\nnumpy>=1.18.0")
    df = parse_requirements_file(req)
    assert len(df) == 2
    assert df.iloc[0]["dependency_name"] == "pandas"
    assert "1.0.0" in df.iloc[0]["version_spec"]

def test_parse_pyproject(tmp_path):
    pyproj = tmp_path / "pyproject.toml"
    pyproj.write_text("[tool.poetry.dependencies]\npython = \"^3.9\"\npandas = \"^1.0.0\"")
    df = parse_pyproject_dependencies(pyproj)
    # the simple parser will extract both
    assert len(df) == 2

def test_build_dependency_aging_watch_report(tmp_path):
    profile = get_default_local_maintenance_profile()
    (tmp_path / "requirements.txt").write_text("pandas==1.0.0")
    df, summary = build_dependency_aging_watch_report(tmp_path, profile)
    assert not df.empty
    assert summary["total_dependencies"] > 0
    assert "internet" in summary["disclaimer"].lower()
