#!/bin/bash
cd commodity_fx_signal_bot

cat << 'TEST' > tests/test_packaging_config.py
import pytest
from portable_packaging.packaging_config import (
    validate_portable_packaging_profiles,
    get_default_portable_packaging_profile,
    get_portable_packaging_profile,
    ConfigError
)

def test_validate_portable_packaging_profiles():
    validate_portable_packaging_profiles()

def test_get_default_portable_packaging_profile():
    p = get_default_portable_packaging_profile()
    assert p is not None
    assert p.dry_run_default == True
    assert p.language != ""
    assert p.max_inventory_files > 0
    assert p.allow_archive_create == False
    assert p.allow_package_publish == False
    assert p.allow_docker == False
    assert p.allow_cloud_deploy == False
    assert p.allow_live_commands == False
    assert p.allow_broker_commands == False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_portable_packaging_profile("unknown")
TEST

cat << 'TEST' > tests/test_packaging_labels.py
from portable_packaging.packaging_labels import (
    list_packaging_artifact_labels,
    list_install_verification_labels,
    list_packaging_safety_labels,
    list_environment_drift_labels,
    validate_packaging_artifact_label,
    validate_install_verification_label
)

def test_lists_not_empty():
    assert len(list_packaging_artifact_labels()) > 0
    assert len(list_install_verification_labels()) > 0
    assert len(list_packaging_safety_labels()) > 0
    assert len(list_environment_drift_labels()) > 0

def test_validate_labels():
    validate_packaging_artifact_label("source_artifact")
    validate_install_verification_label("install_check_passed")
TEST

cat << 'TEST' > tests/test_packaging_models.py
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
TEST

cat << 'TEST' > tests/test_environment_snapshot.py
from portable_packaging.environment_snapshot import (
    collect_python_runtime_info,
    collect_platform_info,
    collect_memory_info,
    collect_installed_packages_snapshot
)
import pandas as pd

def test_environment_collections():
    assert isinstance(collect_python_runtime_info(), dict)
    assert isinstance(collect_platform_info(), dict)
    assert isinstance(collect_memory_info(), dict)

    df = collect_installed_packages_snapshot()
    assert isinstance(df, pd.DataFrame)
TEST

cat << 'TEST' > tests/test_dependency_inventory.py
from pathlib import Path
from portable_packaging.dependency_inventory import (
    parse_requirements_files,
    parse_pyproject_dependencies,
    collect_imported_packages,
    build_dependency_inventory,
    compare_required_vs_installed
)

def test_dependency_collections(tmp_path):
    (tmp_path / "requirements.txt").write_text("pandas==2.0.0")
    df = parse_requirements_files(tmp_path)
    assert not df.empty

    py = parse_pyproject_dependencies(tmp_path)
    assert py.empty

    (tmp_path / "app.py").write_text("import pandas\n")
    imports = collect_imported_packages(tmp_path)
    assert not imports.empty

    inv, sum = build_dependency_inventory(tmp_path, None)
    assert not inv.empty

    comp = compare_required_vs_installed(inv)
    assert comp.empty # because installed version is None
TEST

cat << 'TEST' > tests/test_requirements_export.py
import pandas as pd
from portable_packaging.requirements_export import (
    build_requirements_minimal_export,
    build_requirements_frozen_export,
    build_optional_dependencies_note,
    save_requirements_exports
)

def test_requirements_export(tmp_path):
    df = pd.DataFrame([{"package_name": "pandas", "required_version": "2.0.0", "requirement_detected": True}])
    t, _ = build_requirements_minimal_export(df)
    assert "pandas==2.0.0" in t

    installed = pd.DataFrame([{"package_name": "pandas", "installed_version": "2.0.0"}])
    f, _ = build_requirements_frozen_export(installed)
    assert "LOCAL ENVIRONMENT SNAPSHOT" in f

    n = build_optional_dependencies_note(pd.DataFrame([{"optional": False}]))
    assert "No optional dependencies detected" in n

    save_requirements_exports(tmp_path, {"req.txt": "a"})
    assert (tmp_path / "req.txt").exists()
TEST

cat << 'TEST' > tests/test_install_verification.py
from pathlib import Path
from portable_packaging.install_verification import (
    verify_python_version,
    verify_required_directories,
    verify_config_templates,
    verify_core_imports
)

def test_install_verification(tmp_path):
    res = verify_python_version()
    assert res.check_name == "Python Version Verification"

    res = verify_required_directories(tmp_path)
    assert not res.passed

    res = verify_config_templates(tmp_path)
    assert not res.passed

    # Core imports gracefully handle missing directories
    res = verify_core_imports(tmp_path)
    assert not res.passed
TEST

cat << 'TEST' > tests/test_import_verification.py
from portable_packaging.import_verification import (
    build_core_module_list,
    verify_module_import,
    verify_core_module_imports,
    verify_pipeline_imports
)

def test_import_verification(tmp_path):
    assert len(build_core_module_list()) > 0

    res = verify_module_import("os", tmp_path)
    assert res["importable"]

    df, _ = verify_core_module_imports(tmp_path)
    assert not df.empty

    df, _ = verify_pipeline_imports(tmp_path)
    assert not df.empty
TEST

cat << 'TEST' > tests/test_script_verification.py
from portable_packaging.script_verification import (
    discover_safe_scripts,
    verify_script_main_guard,
    verify_script_importability,
    classify_script_safety
)

def test_script_verification(tmp_path):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "test_script.py").write_text("if __name__ == '__main__':\n    pass")

    df = discover_safe_scripts(tmp_path)
    assert not df.empty

    guard = verify_script_main_guard(scripts / "test_script.py")
    assert guard["has_main_guard"]

    imp = verify_script_importability(scripts / "test_script.py", tmp_path)
    assert imp["importable"]

    safe = classify_script_safety(scripts / "test_script.py")
    assert safe == "safe"

    unsafe = classify_script_safety(scripts / "live_trade.py")
    assert unsafe == "forbidden"
TEST

cat << 'TEST' > tests/test_config_verification.py
from portable_packaging.config_verification import (
    verify_env_example,
    verify_settings_env_alignment,
    verify_no_secrets_in_templates
)

def test_config_verification(tmp_path):
    res = verify_env_example(tmp_path)
    assert not res.passed

    df, s = verify_settings_env_alignment(tmp_path)
    assert not df.empty

    df, s = verify_no_secrets_in_templates(tmp_path)
    assert not df.empty
TEST

cat << 'TEST' > tests/test_bundle_manifest.py
from portable_packaging.bundle_manifest import (
    scan_bundle_artifacts,
    classify_bundle_artifact,
    decide_artifact_include_policy,
    build_portable_bundle_manifest
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_bundle_manifest(tmp_path):
    (tmp_path / "app.py").write_text("")
    (tmp_path / ".env").write_text("")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/readme.md").write_text("")

    profile = get_default_portable_packaging_profile()
    df, sum = scan_bundle_artifacts(tmp_path, profile)

    assert not df.empty

    cls = classify_bundle_artifact(tmp_path / "app.py", tmp_path)
    assert cls == "source_artifact"

    pol = decide_artifact_include_policy(tmp_path / ".env", "config_artifact", profile)
    assert pol["policy"] == "exclude_secret"

    man = build_portable_bundle_manifest(profile, df, None)
    assert man.manifest_id
TEST

cat << 'TEST' > tests/test_archive_manifest.py
import pandas as pd
from portable_packaging.archive_manifest import (
    build_archive_plan_from_bundle_manifest,
    build_archive_manifest_json,
    validate_archive_plan_safety
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_archive_manifest():
    profile = get_default_portable_packaging_profile()
    df = pd.DataFrame([{"include_policy": "include", "relative_path": "app.py", "safety_label": "safe"}])

    plan, sum = build_archive_plan_from_bundle_manifest(df, profile)
    assert not plan.empty
    assert plan["archive_action"].iloc[0] == "add"

    man = build_archive_manifest_json(plan, profile)
    assert man["planned_files"] == ["app.py"]

    val = validate_archive_plan_safety(plan, profile)
    assert val["is_safe"]
TEST

cat << 'TEST' > tests/test_source_policy.py
from portable_packaging.source_policy import (
    build_source_inclusion_policy,
    build_source_exclusion_policy,
    validate_source_policy
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_source_policy():
    profile = get_default_portable_packaging_profile()

    inc = build_source_inclusion_policy(profile)
    assert not inc.empty

    exc = build_source_exclusion_policy(profile)
    assert not exc.empty

    val = validate_source_policy(inc, exc)
    assert val["valid"]
TEST

cat << 'TEST' > tests/test_reproducible_setup.py
from portable_packaging.reproducible_setup import (
    build_reproducible_setup_steps,
    build_reproducible_setup_guide
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile
import pandas as pd

def test_reproducible_setup(tmp_path):
    profile = get_default_portable_packaging_profile()

    steps = build_reproducible_setup_steps(profile)
    assert len(steps) > 0

    md, sum = build_reproducible_setup_guide(None, pd.DataFrame(), pd.DataFrame(), profile)
    assert "Reproducible Setup Guide" in md
    assert "Canlı emir, broker entegrasyonu, model deploy işlemleri YOKTUR" in md
TEST

cat << 'TEST' > tests/test_environment_drift.py
from portable_packaging.environment_drift import (
    compare_environment_snapshots,
    classify_environment_drift,
    build_environment_drift_report
)

def test_environment_drift():
    comp = compare_environment_snapshots({"os_name": "linux"}, {"os_name": "linux"})
    assert comp["is_identical"]

    cls = classify_environment_drift(comp)
    assert cls == "environment_match"

    df, s = build_environment_drift_report(None, None)
    assert s["drift_status"] == "environment_missing_snapshot"
TEST

cat << 'TEST' > tests/test_packaging_safety.py
from portable_packaging.packaging_safety import (
    scan_bundle_for_secret_risk,
    scan_packaging_outputs_for_forbidden_terms,
    validate_no_publish_or_deploy_paths,
    validate_manifest_only_data_policy
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile
import pandas as pd
from pathlib import Path

def test_packaging_safety():
    profile = get_default_portable_packaging_profile()

    df, s = scan_bundle_for_secret_risk(pd.DataFrame(), Path("."))
    assert s["secrets_found"] == 0

    terms = scan_packaging_outputs_for_forbidden_terms("package publish")
    assert "package publish" in terms["forbidden_terms_found"]

    terms = scan_packaging_outputs_for_forbidden_terms("package publish yoktur")
    assert "package publish" not in terms["forbidden_terms_found"]

    assert validate_no_publish_or_deploy_paths(pd.DataFrame())["valid"]
    assert validate_manifest_only_data_policy(pd.DataFrame(), profile)["valid"]
TEST

cat << 'TEST' > tests/test_packaging_quality.py
from portable_packaging.packaging_quality import (
    check_environment_snapshot_quality,
    check_dependency_inventory_quality,
    check_install_verification_quality,
    check_bundle_manifest_quality,
    check_packaging_safety_quality,
    build_packaging_quality_report
)
import pandas as pd
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_packaging_quality():
    profile = get_default_portable_packaging_profile()

    assert not check_environment_snapshot_quality(None, None)["valid"]
    assert check_dependency_inventory_quality(pd.DataFrame([{"a": 1}]))["valid"]
    assert check_install_verification_quality(pd.DataFrame([{"a": 1}]))["valid"]
    assert check_bundle_manifest_quality(pd.DataFrame(), {}, profile)["valid"]
    assert check_packaging_safety_quality(None, {"is_safe": True})["valid"]

    req = build_packaging_quality_report({})
    assert req["passed"]
TEST

cat << 'TEST' > tests/test_packaging_report_builder.py
from portable_packaging.packaging_report_builder import (
    build_packaging_disclaimer,
    build_environment_snapshot_markdown_report,
    build_dependency_inventory_markdown_report,
    build_requirements_export_markdown_report,
    build_install_verification_markdown_report,
    build_portable_bundle_manifest_markdown_report,
    build_packaging_quality_markdown_report,
    build_packaging_status_markdown_report
)

def test_report_builder():
    disc = build_packaging_disclaimer()
    assert "UYARI" in disc
    assert "gerçek emir" in disc

    md = build_environment_snapshot_markdown_report({})
    assert "Environment Snapshot Report" in md

    md = build_dependency_inventory_markdown_report({})
    assert "Dependency Inventory Report" in md

    md = build_requirements_export_markdown_report({})
    assert "Requirements Export Report" in md

    md = build_install_verification_markdown_report({})
    assert "Install Verification Report" in md

    md = build_portable_bundle_manifest_markdown_report({})
    assert "Portable Bundle Manifest Report" in md

    md = build_packaging_quality_markdown_report({}, {})
    assert "Packaging Quality Report" in md

    md = build_packaging_status_markdown_report({})
    assert "Packaging Status Report" in md
TEST

cat << 'TEST' > tests/test_packaging_pipeline.py
from portable_packaging.packaging_pipeline import PortablePackagingPipeline
from portable_packaging.packaging_config import get_default_portable_packaging_profile
from data.storage.data_lake import DataLake
from config.settings import settings
from pathlib import Path

def test_packaging_pipeline(tmp_path):
    profile = get_default_portable_packaging_profile()
    dl = DataLake()

    # Monkeypatch DL methods so they don't actually write to non-existent hardcoded paths if they try
    dl.save_environment_snapshot = lambda a, b, c: None
    dl.save_dependency_inventory = lambda a, b: None
    dl.save_requirements_export_report = lambda a, b: None
    dl.save_install_verification_report = lambda a, b: None
    dl.save_portable_bundle_manifest = lambda a: None
    dl.save_bundle_artifact_inventory = lambda a, b: None

    pipeline = PortablePackagingPipeline(dl, settings, tmp_path, profile)

    _, s1 = pipeline.build_environment_snapshot_report(save=False)
    assert s1 is not None

    _, s2 = pipeline.build_dependency_inventory_report(save=False)
    assert s2 is not None

    # We ignore file paths that are outside of tmp_path since save=False
TEST

cat << 'TEST' > tests/test_portable_packaging_scripts_contract.py
import subprocess
from pathlib import Path

def test_portable_packaging_scripts_importable():
    scripts_dir = Path("scripts")
    scripts = [
        "run_environment_snapshot.py",
        "run_dependency_inventory.py",
        "run_requirements_export.py",
        "run_install_verification.py",
        "run_portable_bundle_manifest.py",
        "run_reproducible_setup_guide.py",
        "run_packaging_status.py"
    ]
    for script in scripts:
        if (scripts_dir / script).exists():
            res = subprocess.run(["python", "-c", f"import scripts.{script.replace('.py', '')}"])
            assert res.returncode == 0
TEST
