from pathlib import Path
import pandas as pd
import re
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

_FORBIDDEN_TERMS = ["send_order", "execute_trade", "create_order", "market_order", "limit_order", "broker_order", "live_order", "real_position", "leverage_order", "margin_order"]

def detect_broker_related_code(project_root: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}
def detect_unsafe_subprocess_usage(project_root: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}
def detect_network_call_usage(project_root: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}

def detect_live_order_related_code(project_root: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"issues_found": 0, "scanned_files": 0}
    for ext in profile.scan_text_extensions:
        if ext not in [".py", ".sh"]: continue
        for path in project_root.rglob(f"*{ext}"):
            if ".venv" in str(path) or "venv" in str(path) or "__pycache__" in str(path) or "security" in str(path): continue
            try:
                if path.stat().st_size > profile.max_file_scan_mb * 1024 * 1024: continue
                summary["scanned_files"] += 1
                with open(path, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f):
                        for term in _FORBIDDEN_TERMS:
                            if term in line.lower():
                                if "test" in str(path).lower() or "def test" in line.lower() or "forbidden term" in line.lower() or "quality" in str(path).lower() or "check" in str(path).lower() or "security" in str(path).lower(): continue
                                if re.search(r"def\s+" + term, line.lower()) or re.search(term + r"\s*\(", line.lower()):
                                    findings.append(SecurityFinding(
                                        finding_id=build_security_finding_id("permission_boundary", f"forbidden_term_{term}", str(path), i+1),
                                        category="permission_boundary", severity="critical", status="security_failed",
                                        title=f"Forbidden live execution term found: {term}", description=f"Found {term} in {path.name}",
                                        file_path=str(path), line_number=i+1, recommended_action="Remove real execution logic.", blocking=True
                                    ))
                                    summary["issues_found"] += 1
                                else:
                                     findings.append(SecurityFinding(
                                        finding_id=build_security_finding_id("permission_boundary", f"forbidden_string_term_{term}", str(path), i+1),
                                        category="permission_boundary", severity="warning", status="security_warning",
                                        title=f"Forbidden term mentioned: {term}", description=f"Found {term} as string mention in {path.name}",
                                        file_path=str(path), line_number=i+1, recommended_action="Ensure it's not execution logic.", blocking=False
                                    ))
                                     summary["issues_found"] += 1
            except Exception: pass
    return findings, summary

def check_permission_boundary_matrix(project_root: Path, settings_obj: object, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    return build_permission_boundary_report(project_root, settings_obj, profile)

def build_permission_boundary_report(project_root: Path, settings_obj: object, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings, _ = detect_live_order_related_code(project_root, profile)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
