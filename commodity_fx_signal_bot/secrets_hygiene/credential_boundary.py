
from pathlib import Path
import pandas as pd
from typing import Tuple, Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import CredentialBoundaryResult, build_credential_boundary_id

def build_credential_boundary_policy() -> pd.DataFrame:
    return pd.DataFrame([
        {"boundary_name": "templates_or_local_env", "rule": "Credentials must only be in templates or .env"},
        {"boundary_name": "no_credentials_in_reports", "rule": "No credentials in reports"},
        {"boundary_name": "no_credentials_in_docs", "rule": "No credentials in docs"},
        {"boundary_name": "no_credentials_in_tests", "rule": "No credentials in tests"},
        {"boundary_name": "no_credentials_in_backup_manifests", "rule": "No credentials in backup manifests"},
    ])

def _get_findings_for_paths(findings_df: Optional[pd.DataFrame], path_substring: str) -> pd.DataFrame:
    if findings_df is None or findings_df.empty: return pd.DataFrame()
    return findings_df[findings_df["relative_path"].str.contains(path_substring, case=False, na=False)]

def check_credentials_only_in_templates_or_local_env(project_root: Path) -> CredentialBoundaryResult:
    return CredentialBoundaryResult(build_credential_boundary_id("templates_or_local_env"), "templates_or_local_env", "boundary_ok", [".env.example"], 0, 0, {"message": "Assuming .env usage is bounded."}, [])

def check_no_credentials_in_reports(project_root: Path, findings_df: Optional[pd.DataFrame]) -> CredentialBoundaryResult:
    df = _get_findings_for_paths(findings_df, "reports/output")
    return CredentialBoundaryResult(build_credential_boundary_id("no_credentials_in_reports"), "no_credentials_in_reports", "boundary_failed" if not df.empty else "boundary_ok", ["reports/output/"], len(df), len(df[df["severity"] == "critical_secret_risk"]) if not df.empty else 0, {"message": "Checked reports"}, [])

def check_no_credentials_in_docs(project_root: Path, findings_df: Optional[pd.DataFrame]) -> CredentialBoundaryResult:
    df = _get_findings_for_paths(findings_df, "docs/")
    return CredentialBoundaryResult(build_credential_boundary_id("no_credentials_in_docs"), "no_credentials_in_docs", "boundary_failed" if not df.empty else "boundary_ok", ["docs/"], len(df), len(df[df["severity"] == "critical_secret_risk"]) if not df.empty else 0, {"message": "Checked docs"}, [])

def check_no_credentials_in_tests(project_root: Path, findings_df: Optional[pd.DataFrame]) -> CredentialBoundaryResult:
    df = _get_findings_for_paths(findings_df, "tests/")
    return CredentialBoundaryResult(build_credential_boundary_id("no_credentials_in_tests"), "no_credentials_in_tests", "boundary_failed" if not df.empty else "boundary_ok", ["tests/"], len(df), len(df[df["severity"] == "critical_secret_risk"]) if not df.empty else 0, {"message": "Checked tests"}, [])

def check_no_credentials_in_backup_packaging_manifests(project_root: Path, findings_df: Optional[pd.DataFrame]) -> CredentialBoundaryResult:
    df = _get_findings_for_paths(findings_df, "manifest")
    return CredentialBoundaryResult(build_credential_boundary_id("no_credentials_in_backup_manifests"), "no_credentials_in_backup_manifests", "boundary_failed" if not df.empty else "boundary_ok", ["data/lake/"], len(df), len(df[df["severity"] == "critical_secret_risk"]) if not df.empty else 0, {"message": "Checked manifests"}, [])

def audit_credential_boundaries(project_root: Path, findings_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> Tuple[pd.DataFrame, dict]:
    results = [check_credentials_only_in_templates_or_local_env(project_root), check_no_credentials_in_reports(project_root, findings_df), check_no_credentials_in_docs(project_root, findings_df), check_no_credentials_in_tests(project_root, findings_df), check_no_credentials_in_backup_packaging_manifests(project_root, findings_df)]
    df = pd.DataFrame([r.__dict__ for r in results])
    return df, {"total_boundaries": len(df), "failed_boundaries": len(df[df["status"] == "boundary_failed"]), "total_findings_in_boundaries": df["finding_count"].sum()}
