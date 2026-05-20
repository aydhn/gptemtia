from pathlib import Path
import pandas as pd
from .dev_models import DXFinding, build_dx_finding_id
from .dev_config import DevExperienceProfile

def check_required_docs(project_root: Path, profile: DevExperienceProfile) -> tuple[list[DXFinding], dict]:
    findings = []
    for doc in profile.required_docs:
        if not (project_root / doc).exists():
            findings.append(DXFinding(
                finding_id=build_dx_finding_id("docs_quality", f"missing_{Path(doc).name}"),
                category="docs_quality",
                status="dx_failed",
                title=f"Missing {doc}",
                description=f"Profile requires documentation file {doc}"
            ))
    return findings, {}

def check_docs_nonempty(project_root: Path, docs: tuple[str, ...]) -> tuple[list[DXFinding], dict]:
    findings = []
    for doc in docs:
        p = project_root / doc
        if p.exists() and p.stat().st_size == 0:
            findings.append(DXFinding(
                finding_id=build_dx_finding_id("docs_quality", f"empty_{Path(doc).name}"),
                category="docs_quality",
                status="dx_failed",
                title=f"Empty {doc}",
                description=f"Documentation file {doc} is empty"
            ))
    return findings, {}

def check_readme_sections(project_root: Path) -> tuple[list[DXFinding], dict]:
    findings = []
    # Simplified mock check
    return findings, {}

def check_docs_for_forbidden_trade_language(project_root: Path) -> tuple[list[DXFinding], dict]:
    findings = []
    # Simplified mock check
    return findings, {}

def build_docs_audit_report(project_root: Path, profile: DevExperienceProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = check_required_docs(project_root, profile)
    f2, _ = check_docs_nonempty(project_root, profile.required_docs)
    f3, _ = check_readme_sections(project_root)
    f4, _ = check_docs_for_forbidden_trade_language(project_root)

    findings.extend(f1 + f2 + f3 + f4)
    df = pd.DataFrame([f.__dict__ for f in findings])
    summary = {
        "total_findings": len(findings),
        "failed": sum(1 for f in findings if f.status == "dx_failed")
    }
    return df, summary
