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
