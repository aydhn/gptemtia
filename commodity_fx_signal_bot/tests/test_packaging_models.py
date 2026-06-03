from portable_packaging.packaging_models import (
    build_environment_snapshot_id,
    build_dependency_id,
    build_bundle_artifact_id,
    build_install_check_id,
    EnvironmentSnapshot,
    environment_snapshot_to_dict
)

def test_deterministic_ids():
    assert build_environment_snapshot_id("2024") == build_environment_snapshot_id("2024")
    assert build_dependency_id("requests", "reqs") == build_dependency_id("requests", "reqs")
    assert build_bundle_artifact_id("app.py") == build_bundle_artifact_id("app.py")
    assert build_install_check_id("py") == build_install_check_id("py")

def test_to_dict():
    s = EnvironmentSnapshot("id", "utc", "os", "plat", "3.10", "exe", 4, 1024, False, 10, [])
    d = environment_snapshot_to_dict(s)
    assert d["snapshot_id"] == "id"
    assert d["python_version"] == "3.10"
