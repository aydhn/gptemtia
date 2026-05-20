from pathlib import Path
import pandas as pd
from .dev_models import DXFinding, build_dx_finding_id
from .dev_config import DevExperienceProfile

def check_required_files(project_root: Path, profile: DevExperienceProfile) -> tuple[list[DXFinding], dict]:
    findings = []
    for req in profile.required_project_files:
        if not (project_root / req).exists():
            findings.append(DXFinding(
                finding_id=build_dx_finding_id("repo_hygiene", f"missing_{req}"),
                category="repo_hygiene",
                status="dx_failed",
                title=f"Missing {req}",
                description=f"Profile requires {req}"
            ))
    return findings, {}

def check_required_directories(project_root: Path) -> tuple[list[DXFinding], dict]:
    dirs = ["docs", "tests", "scripts"]
    findings = []
    for d in dirs:
        if not (project_root / d).is_dir():
            findings.append(DXFinding(
                finding_id=build_dx_finding_id("repo_hygiene", f"missing_dir_{d}"),
                category="repo_hygiene",
                status="dx_warning",
                title=f"Missing directory {d}",
                description=f"Standard directory {d} is missing"
            ))
    return findings, {}

def check_gitignore_hygiene(project_root: Path) -> tuple[list[DXFinding], dict]:
    findings = []
    path = project_root / ".gitignore"
    if not path.exists():
        findings.append(DXFinding(
            finding_id=build_dx_finding_id("repo_hygiene", "missing_gitignore"),
            category="repo_hygiene",
            status="dx_failed",
            title="Missing .gitignore",
            description=".gitignore is required"
        ))
        return findings, {}

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if ".env" not in content:
        findings.append(DXFinding(
            finding_id=build_dx_finding_id("repo_hygiene", "missing_env_ignore"),
            category="repo_hygiene",
            status="dx_failed",
            title=".env missing from .gitignore",
            description=".env must be ignored to prevent secret leaks"
        ))
    return findings, {}

def check_large_files(project_root: Path, max_mb: int = 25) -> tuple[list[DXFinding], dict]:
    findings = []
    # Simplified mock for large file check
    return findings, {}

def check_empty_init_files(project_root: Path) -> tuple[list[DXFinding], dict]:
    findings = []
    return findings, {}

def build_repo_hygiene_report(project_root: Path, profile: DevExperienceProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = check_required_files(project_root, profile)
    f2, _ = check_required_directories(project_root)
    f3, _ = check_gitignore_hygiene(project_root)
    f4, _ = check_large_files(project_root)
    f5, _ = check_empty_init_files(project_root)

    findings.extend(f1 + f2 + f3 + f4 + f5)
    df = pd.DataFrame([f.__dict__ for f in findings])
    summary = {
        "total_findings": len(findings),
        "failed": sum(1 for f in findings if f.status == "dx_failed")
    }
    return df, summary
