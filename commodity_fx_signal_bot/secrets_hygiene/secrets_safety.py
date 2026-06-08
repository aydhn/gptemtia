
import pandas as pd
from typing import Tuple, Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile

def scan_secret_outputs_for_raw_values(findings_df: Optional[pd.DataFrame], reports: Optional[dict] = None) -> dict:
    if findings_df is not None and not findings_df.empty:
        if "raw_value" in findings_df.columns: return {"status": "failed", "reason": "raw_value column exists in findings DataFrame"}
    return {"status": "passed", "reason": "No raw values detected in schema"}

def validate_no_secret_value_output(findings_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    if profile.allow_secret_value_output: return {"status": "warning", "reason": "Profile allows secret output"}
    return scan_secret_outputs_for_raw_values(findings_df)

def validate_no_file_modification_actions(recommendations_df: Optional[pd.DataFrame], profile: SecretsHygieneProfile) -> dict:
    if profile.allow_file_modification or profile.allow_secret_deletion: return {"status": "failed", "reason": "Profile allows file modifications"}
    if recommendations_df is not None and not recommendations_df.empty:
        if "destructive" in recommendations_df.columns and recommendations_df["destructive"].any(): return {"status": "failed", "reason": "Destructive recommendations found"}
    return {"status": "passed", "reason": "No file modification actions detected"}

def validate_no_forbidden_secret_workflows(summary: Optional[dict] = None, text: Optional[str] = None) -> dict:
    forbidden = ["print secret", "show token", "dump env", "upload secret", "cloud vault connect", "rotate automatically", "delete secret file", "overwrite env", "broker order", "live order", "deploy model", "openai api"]
    if text:
        text_lower = text.lower()
        for f in forbidden:
            if f in text_lower:
                if any(x in text_lower for x in ["secret g\u00f6sterilmez", "token yazd\u0131r\u0131lmaz", "canl\u0131 emir yoktur"]): continue
                return {"status": "failed", "reason": f"Forbidden workflow mentioned: {f}"}
    return {"status": "passed", "reason": "No forbidden workflows detected"}

def build_secrets_safety_report(tables: dict[str, pd.DataFrame], profile: SecretsHygieneProfile) -> Tuple[pd.DataFrame, dict]:
    results = [
        {"check": "no_secret_value_output", **validate_no_secret_value_output(tables.get("findings"), profile)},
        {"check": "no_file_modification", **validate_no_file_modification_actions(tables.get("recommendations"), profile)},
        {"check": "no_forbidden_workflows", **validate_no_forbidden_secret_workflows()}
    ]
    df = pd.DataFrame(results)
    return df, {"total_checks": len(df), "passed": len(df[df["status"] == "passed"]) == len(df)}
