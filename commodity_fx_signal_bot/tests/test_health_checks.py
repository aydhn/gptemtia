import pytest
from pathlib import Path

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from observability.health_checks import (
    check_config_health,
    check_paths_health,
    check_data_lake_health,
    check_disk_space_health,
    check_python_environment_health,
    build_system_health_report
)

def test_check_config_health():
    settings = Settings()
    health = check_config_health(settings)
    assert health.component == "config"
    assert health.status in ["healthy", "degraded", "unhealthy"]

def test_check_paths_health(tmp_path):
    class MockPaths:
        DATA_DIR = tmp_path / "data"
        LAKE_DIR = tmp_path / "data/lake"
        lake_dir = LAKE_DIR

    health = check_paths_health(MockPaths)
    assert health.component == "paths"
    assert health.checks_passed > 0

def test_check_data_lake_health(tmp_path):
    class MockPaths:
        DATA_DIR = tmp_path / "data"
        LAKE_DIR = tmp_path / "data/lake"
        lake_dir = LAKE_DIR

    # Setup mock lake
    paths = MockPaths()
    paths.LAKE_DIR.mkdir(parents=True, exist_ok=True)

    lake = DataLake(paths)
    health = check_data_lake_health(lake)

    assert health.component == "data_lake"
    assert health.checks_passed > 0

def test_check_disk_space_health(tmp_path):
    # Pass a very high threshold to force a failure/critical status
    health = check_disk_space_health(tmp_path, min_free_mb=999999999)
    assert health.component == "disk_space"
    assert health.status == "critical"

    # Pass a low threshold to pass
    health_pass = check_disk_space_health(tmp_path, min_free_mb=1)
    assert health_pass.status == "healthy"

def test_check_python_environment_health():
    health = check_python_environment_health()
    assert health.component == "python_environment"
    assert health.checks_passed > 0

def test_build_system_health_report():
    h1 = check_python_environment_health()

    class MockPaths:
        DATA_DIR = Path("/tmp/data_test_sys")
        LAKE_DIR = Path("/tmp/data_test_sys/lake")
    h2 = check_paths_health(MockPaths)

    df, summary = build_system_health_report([h1, h2])
    assert not df.empty
    assert len(df) == 2
    assert "overall_status" in summary
    assert "overall_score" in summary
