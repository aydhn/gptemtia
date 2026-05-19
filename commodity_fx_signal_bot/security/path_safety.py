from pathlib import Path
import pandas as pd
import re
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

def is_path_within_base(path: Path, base_dir: Path) -> bool:
    try:
        path.resolve().relative_to(base_dir.resolve())
        return True
    except ValueError:
        return False

def sanitize_filename_component(value: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_-]', '_', value)

def detect_path_traversal_patterns(text: str) -> dict:
    if "../" in text or "..\\" in text: return {"has_traversal": True}
    return {"has_traversal": False}

def check_datalake_paths_within_project(data_lake: object, project_root: Path) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"issues_found": 0}
    if hasattr(data_lake, "paths"):
        paths_obj = data_lake.paths
        for attr in dir(paths_obj):
            if attr.startswith("_"): continue
            val = getattr(paths_obj, attr)
            if isinstance(val, Path):
                if not is_path_within_base(val, project_root):
                    findings.append(SecurityFinding(
                        finding_id=build_security_finding_id("path_safety", f"outside_path_{attr}"),
                        category="path_safety", severity="high", status="security_failed",
                        title=f"Path outside project root: {attr}", description=f"Path {val} resolves outside project root.", blocking=True
                    ))
                    summary["issues_found"] += 1
    return findings, summary

def scan_code_for_unsafe_path_join(project_root: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}

def build_path_safety_report(project_root: Path, data_lake: object, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings, _ = check_datalake_paths_within_project(data_lake, project_root)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
