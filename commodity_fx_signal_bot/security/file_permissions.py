from pathlib import Path
import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

def check_file_permission_mode(path: Path) -> dict:
    if not path.exists(): return {"exists": False}
    return {"exists": True, "mode": oct(path.stat().st_mode)[-3:]}

def check_sensitive_file_permissions(project_root: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    env_path = project_root / ".env"
    if env_path.exists():
        perm = check_file_permission_mode(env_path)
        if perm.get("mode", "000").endswith("4") or perm.get("mode", "000").endswith("7"):
            findings.append(SecurityFinding(
                finding_id=build_security_finding_id("file_permission", "env_world_readable"),
                category="file_permission", severity="warning", status="security_warning",
                title=".env is world-readable", description="The .env file has world-readable permissions.",
                file_path=str(env_path), recommended_action="chmod 600 .env"
            ))
    return findings, {}

def check_data_lake_write_permissions(data_lake_root: Path) -> tuple[list[SecurityFinding], dict]: return [], {}
def check_report_output_permissions(report_root: Path) -> tuple[list[SecurityFinding], dict]: return [], {}

def build_file_permission_report(project_root: Path, data_lake_root: Path, report_root: Path, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings, _ = check_sensitive_file_permissions(project_root, profile)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
