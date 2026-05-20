from devtools.package_audit import check_pyproject_metadata, check_requirements_files, check_pytest_config, check_makefile, build_package_audit_report
from devtools.dev_config import get_default_dev_experience_profile

def test_package_audit_checks(tmp_path):
    p1, _ = check_pyproject_metadata(tmp_path)
    assert len(p1) > 0 # should find missing

    p2, _ = check_requirements_files(tmp_path)
    assert len(p2) > 0

    p3, _ = check_pytest_config(tmp_path)
    assert len(p3) > 0

    profile = get_default_dev_experience_profile()
    p4, _ = check_makefile(tmp_path, profile)
    assert len(p4) > 0
