
import re
import pandas as pd
from typing import Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import SecretFinding, build_secret_finding_id
from secrets_hygiene.redaction import mask_secret_value

_PATTERNS = [
    {"name": "generic_api_key", "regex": r"(?i)(?:api_key|apikey)[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "generic_api_secret", "regex": r"(?i)(?:api_secret|apisecret)[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "bearer_token", "regex": r"(?i)bearer\s+([A-Za-z0-9_=\.-]{20,})"},
    {"name": "jwt_token", "regex": r"(?i)eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"},
    {"name": "private_key_block", "regex": r"-----BEGIN\s+.*PRIVATE\s+KEY-----"},
    {"name": "ssh_private_key", "regex": r"-----BEGIN\s+OPENSSH\s+PRIVATE\s+KEY-----"},
    {"name": "password_assignment", "regex": r"(?i)(?:password|passwd|pwd)[\s:=]+['\"]?([A-Za-z0-9@#\$\^&\*_-]{8,})['\"]?"},
    {"name": "token_assignment", "regex": r"(?i)token[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "secret_assignment", "regex": r"(?i)secret[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "broker_key_assignment", "regex": r"(?i)broker(?:_key|_secret)[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "exchange_key_assignment", "regex": r"(?i)exchange(?:_key|_secret)[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "openai_key_pattern", "regex": r"sk-[A-Za-z0-9]{48,}"},
    {"name": "aws_access_key_like", "regex": r"(?i)(?:aws_access_key_id|aws_secret_access_key)[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
    {"name": "google_api_key_like", "regex": r"AIza[0-9A-Za-z-_]{35}"},
    {"name": "telegram_bot_token_like", "regex": r"[0-9]{9,}:[a-zA-Z0-9_-]{35,}"},
    {"name": "database_url_with_password", "regex": r"(?i)(?:postgres|mysql|mongodb)://[a-zA-Z0-9_-]+:([^@]+)@"},
    {"name": "url_with_credentials", "regex": r"https?://[a-zA-Z0-9_-]+:([^@]+)@"},
    {"name": "env_assignment_with_secret_value", "regex": r"^[A-Z0-9_]+_?(?:KEY|SECRET|TOKEN|PASSWORD)[\s:=]+['\"]?([A-Za-z0-9_-]{20,})['\"]?"},
]

_FALSE_POSITIVES = [
    "PLACEHOLDER", "CHANGE_ME", "YOUR_API_KEY", "xxx", "****", "example", "dummy", "fake", "test_key", "not used", "no secret"
]

def build_secret_pattern_registry() -> pd.DataFrame:
    return pd.DataFrame(_PATTERNS)

def compile_secret_patterns() -> list[dict]:
    return [{"name": p["name"], "regex": re.compile(p["regex"], re.MULTILINE)} for p in _PATTERNS]

def _is_false_positive(value: str) -> bool:
    return any(fp.lower() in value.lower() for fp in _FALSE_POSITIVES)

def classify_secret_finding_type(pattern_name: str, key_hint: Optional[str] = None) -> str:
    for hint in ["api_key", "api_secret", "broker", "exchange", "token", "password", "private_key", "jwt"]:
        if hint in pattern_name: return f"{hint}_finding"
    if "env_" in pattern_name: return "env_value_finding"
    return "unknown_secret_finding"

def classify_secret_severity(finding_type: str, relative_path: str, pattern_name: str) -> str:
    path_lower = relative_path.lower()
    if any(x in path_lower for x in ["test", "dummy", "example"]): return "low_secret_warning"
    if "private_key" in finding_type or any(x in pattern_name for x in ["aws", "google", "telegram"]): return "critical_secret_risk"
    if any(x in finding_type for x in ["api", "broker", "exchange", "jwt", "token"]): return "high_secret_risk"
    return "medium_secret_risk"

def scan_text_for_secret_patterns(text: str, relative_path: str, profile: SecretsHygieneProfile) -> list[SecretFinding]:
    findings = []
    if not text: return findings
    compiled_patterns = compile_secret_patterns()
    for i, line in enumerate(text.split('\n')):
        for p in compiled_patterns:
            for match in p["regex"].finditer(line):
                raw_val = match.group(1) if match.groups() else match.group(0)
                finding_type = classify_secret_finding_type(p["name"])
                severity = "low_secret_warning" if _is_false_positive(raw_val) else classify_secret_severity(finding_type, relative_path, p["name"])
                masked_val = mask_secret_value(raw_val, profile.mask_keep_start, profile.mask_keep_end)
                findings.append(SecretFinding(
                    finding_id=build_secret_finding_id(relative_path, i+1, p["name"], masked_val),
                    finding_type=finding_type, severity=severity, relative_path=relative_path,
                    line_number=i+1, column_start=match.start(), masked_value=masked_val,
                    pattern_name=p["name"], confidence=0.9 if severity in ["critical_secret_risk", "high_secret_risk"] else 0.5,
                    redaction_status="redacted_ok", warnings=[]
                ))
    return findings

def summarize_secret_pattern_findings(findings_df: pd.DataFrame) -> dict:
    if findings_df is None or findings_df.empty: return {"total_findings": 0, "critical_count": 0, "high_count": 0, "patterns_detected": []}
    return {
        "total_findings": len(findings_df),
        "critical_count": len(findings_df[findings_df["severity"] == "critical_secret_risk"]),
        "high_count": len(findings_df[findings_df["severity"] == "high_secret_risk"]),
        "patterns_detected": findings_df["pattern_name"].unique().tolist() if "pattern_name" in findings_df.columns else []
    }
