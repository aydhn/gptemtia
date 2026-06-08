
import re
import pandas as pd
from pathlib import Path
from typing import Tuple, Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import SecretFinding, build_secret_finding_id
from secrets_hygiene.redaction import mask_secret_value

_PRIVATE_PATTERNS = [
    {"name": "email_address", "regex": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"},
    {"name": "phone_like", "regex": r"(?:(?:\+|00)\d{1,3}[\s-]?)?(?:\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}"},
    {"name": "identity_like", "regex": r"\b[1-9][0-9]{10}\b"},
    {"name": "iban_like", "regex": r"\b[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?:[ ]?[0-9]{1,2})?\b"},
    {"name": "credit_card_like", "regex": r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b"},
]

def build_private_data_pattern_registry() -> pd.DataFrame: return pd.DataFrame(_PRIVATE_PATTERNS)

def classify_private_data_severity(pattern_name: str, relative_path: str) -> str:
    path_lower = relative_path.lower()
    if any(x in path_lower for x in ["test", "dummy", "example", "docs"]): return "low_secret_warning"
    return "medium_secret_risk"

def scan_text_for_private_data(text: str, relative_path: str, profile: SecretsHygieneProfile) -> list[SecretFinding]:
    findings = []
    if not text: return findings
    for i, line in enumerate(text.split('\n')):
        for p in _PRIVATE_PATTERNS:
            for match in re.compile(p["regex"]).finditer(line):
                raw_val = match.group(0)
                if p["name"] == "email_address" and any(x in raw_val for x in ["example.com", "test.com", "dummy"]): continue
                severity = classify_private_data_severity(p["name"], relative_path)
                masked_val = mask_secret_value(raw_val, profile.mask_keep_start, profile.mask_keep_end)
                findings.append(SecretFinding(
                    finding_id=build_secret_finding_id(relative_path, i+1, p["name"], masked_val),
                    finding_type="personal_data_finding", severity=severity, relative_path=relative_path,
                    line_number=i+1, column_start=match.start(), masked_value=masked_val,
                    pattern_name=p["name"], confidence=0.8, redaction_status="redacted_ok", warnings=[]
                ))
    return findings

def scan_project_for_private_data(project_root: Path, profile: SecretsHygieneProfile) -> Tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"total_private_findings": 0}

def summarize_private_data_findings(findings_df: pd.DataFrame) -> dict:
    if findings_df is None or findings_df.empty: return {"total_private_findings": 0, "patterns_detected": []}
    return {"total_private_findings": len(findings_df), "patterns_detected": findings_df["pattern_name"].unique().tolist() if "pattern_name" in findings_df.columns else []}
