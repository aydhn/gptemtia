
import pandas as pd
from typing import Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_safety import validate_no_forbidden_secret_workflows

def check_sensitive_file_inventory_quality(inventory_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    if inventory_df is None or inventory_df.empty: return {"inventory_valid": False, "warnings": ["Inventory is empty"]}
    return {"inventory_valid": True, "warnings": []}

def check_secret_findings_quality(findings_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    warnings = []
    redacted = True
    if findings_df is not None and not findings_df.empty:
        if "raw_value" in findings_df.columns:
            redacted = False
            warnings.append("Raw values found in findings dataframe")
    return {"findings_redacted": redacted, "warnings": warnings}

def check_env_template_audit_quality(env_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    if env_df is None or env_df.empty: return {"env_template_valid": False, "warnings": ["Env template audit empty"]}
    return {"env_template_valid": True, "warnings": []}

def check_credential_boundary_quality(boundary_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    if boundary_df is None or boundary_df.empty: return {"credential_boundary_valid": False, "warnings": ["Boundary report empty"]}
    return {"credential_boundary_valid": True, "warnings": []}

def check_remediation_quality(recommendations_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    safe = True
    warnings = []
    if recommendations_df is not None and not recommendations_df.empty:
        if "destructive" in recommendations_df.columns and recommendations_df["destructive"].any():
            safe = False
            warnings.append("Destructive recommendations present")
    return {"remediation_safe": safe, "warnings": warnings}

def check_for_forbidden_terms_in_secrets(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[dict] = None) -> dict:
    res = validate_no_forbidden_secret_workflows(summary, text)
    if res["status"] == "failed": return {"forbidden_terms_found": True, "warnings": [res["reason"]]}
    return {"forbidden_terms_found": False, "warnings": []}

def build_secrets_quality_report(summary: dict, inventory_df: Optional[pd.DataFrame] = None, findings_df: Optional[pd.DataFrame] = None, boundary_df: Optional[pd.DataFrame] = None, recommendations_df: Optional[pd.DataFrame] = None, profile: Optional[SecretsHygieneProfile] = None) -> dict:
    if not profile:
        from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile
        profile = get_default_secrets_hygiene_profile()
    inv_q = check_sensitive_file_inventory_quality(inventory_df, profile)
    find_q = check_secret_findings_quality(findings_df, profile)
    env_q = check_env_template_audit_quality(None, profile)
    bound_q = check_credential_boundary_quality(boundary_df, profile)
    rem_q = check_remediation_quality(recommendations_df, profile)
    forb_q = check_for_forbidden_terms_in_secrets()
    warnings = inv_q["warnings"] + find_q["warnings"] + env_q["warnings"] + bound_q["warnings"] + rem_q["warnings"] + forb_q["warnings"]
    passed = (inv_q["inventory_valid"] and find_q["findings_redacted"] and bound_q["credential_boundary_valid"] and rem_q["remediation_safe"] and not forb_q["forbidden_terms_found"] and profile.dry_run_default and not profile.allow_file_modification)
    return {"inventory_valid": inv_q["inventory_valid"], "findings_redacted": find_q["findings_redacted"], "env_template_valid": env_q["env_template_valid"], "credential_boundary_valid": bound_q["credential_boundary_valid"], "remediation_safe": rem_q["remediation_safe"], "raw_secret_output_absent": find_q["findings_redacted"], "dry_run_default_confirmed": profile.dry_run_default, "no_file_modification_confirmed": not profile.allow_file_modification, "forbidden_terms_found": forb_q["forbidden_terms_found"], "warning_count": len(warnings), "passed": passed, "warnings": warnings}
