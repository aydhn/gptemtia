from pathlib import Path
import pandas as pd
from .dev_models import DXFinding, build_dx_finding_id
from .dev_config import DevExperienceProfile

def check_pyproject_exists(project_root: Path) -> dict:
    return {"exists": (project_root / "pyproject.toml").exists()}

def check_pyproject_metadata(project_root: Path) -> tuple[list[DXFinding], dict]:
    path = project_root / "pyproject.toml"
    findings = []
    if not path.exists():
        findings.append(DXFinding(
            finding_id=build_dx_finding_id("package_metadata", "pyproject_missing"),
            category="package_metadata",
            status="dx_failed",
            title="pyproject.toml is missing",
            description="Required pyproject.toml is missing.",
            blocking=True
        ))
    return findings, {}

def check_requirements_files(project_root: Path) -> tuple[list[DXFinding], dict]:
    findings = []
    if not (project_root / "requirements.txt").exists():
        findings.append(DXFinding(
            finding_id=build_dx_finding_id("package_metadata", "requirements_missing"),
            category="package_metadata",
            status="dx_failed",
            title="requirements.txt is missing",
            description="Required requirements.txt is missing."
        ))
    if not (project_root / "requirements-dev.txt").exists():
        findings.append(DXFinding(
            finding_id=build_dx_finding_id("package_metadata", "requirements_dev_missing"),
            category="package_metadata",
            status="dx_warning",
            title="requirements-dev.txt is missing",
            description="Recommended requirements-dev.txt is missing."
        ))
    return findings, {}

def check_pytest_config(project_root: Path) -> tuple[list[DXFinding], dict]:
    findings = []
    if not (project_root / "pytest.ini").exists() and not (project_root / "pyproject.toml").exists():
         findings.append(DXFinding(
            finding_id=build_dx_finding_id("package_metadata", "pytest_config_missing"),
            category="package_metadata",
            status="dx_warning",
            title="Pytest config missing",
            description="Neither pytest.ini nor pyproject.toml found."
        ))
    return findings, {}

def check_makefile(project_root: Path, profile: DevExperienceProfile) -> tuple[list[DXFinding], dict]:
    findings = []
    if profile.require_makefile and not (project_root / "Makefile").exists():
        findings.append(DXFinding(
            finding_id=build_dx_finding_id("package_metadata", "makefile_missing"),
            category="package_metadata",
            status="dx_failed",
            title="Makefile is missing",
            description="Profile requires a Makefile."
        ))
    return findings, {}

def build_package_audit_report(project_root: Path, profile: DevExperienceProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = check_pyproject_metadata(project_root)
    f2, _ = check_requirements_files(project_root)
    f3, _ = check_pytest_config(project_root)
    f4, _ = check_makefile(project_root, profile)
    findings.extend(f1 + f2 + f3 + f4)
    df = pd.DataFrame([f.__dict__ for f in findings])
    summary = {
        "total_findings": len(findings),
        "failed": sum(1 for f in findings if f.status == "dx_failed")
    }
    return df, summary
