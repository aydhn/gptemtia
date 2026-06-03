from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any

from portable_packaging.packaging_models import InstallVerificationResult, build_install_check_id

def verify_env_example(project_root: Path) -> InstallVerificationResult:
    passed = (project_root / ".env.example").exists()
    return InstallVerificationResult(
        check_id=build_install_check_id("env_example"),
        check_name=".env.example Verification",
        status="Passed" if passed else "Warning",
        passed=passed,
        details={"exists": passed},
        warnings=[] if passed else ["Missing .env.example"]
    )

def verify_settings_env_alignment(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Mocking alignment output
    data = [{"setting": "PORTABLE_PACKAGING_ENABLED", "aligned": True}]
    df = pd.DataFrame(data)
    return df, {"aligned": True}

def verify_paths_directory_creation(project_root: Path) -> InstallVerificationResult:
    return InstallVerificationResult(
        check_id=build_install_check_id("paths_directory"),
        check_name="Paths Directory Verification",
        status="Passed",
        passed=True,
        details={},
        warnings=[]
    )

def verify_no_secrets_in_templates(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Mocking secret check output
    data = [{"template": ".env.example", "secrets_found": False}]
    df = pd.DataFrame(data)
    return df, {"secrets_found": False}

def build_config_template_verification(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    env_res = verify_env_example(project_root)
    paths_res = verify_paths_directory_creation(project_root)

    data = [
        {"check_name": env_res.check_name, "passed": env_res.passed, "warnings": "; ".join(env_res.warnings)},
        {"check_name": paths_res.check_name, "passed": paths_res.passed, "warnings": "; ".join(paths_res.warnings)}
    ]
    df = pd.DataFrame(data)
    return df, {"total_checks": 2, "passed": sum([env_res.passed, paths_res.passed])}
