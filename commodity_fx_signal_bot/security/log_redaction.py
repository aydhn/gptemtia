from pathlib import Path
import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id
from security.secret_hygiene import detect_secret_like_value, mask_secret_value

def redact_sensitive_text(text: str, profile: SecurityProfile | None = None) -> str: return text
def redact_sensitive_dict(data: dict, profile: SecurityProfile | None = None) -> dict:
    redacted = {}
    for k, v in data.items():
        is_sensitive_key = False
        if profile: is_sensitive_key = any(s.lower() in k.lower() for s in profile.sensitive_env_names)
        else: is_sensitive_key = any(s.lower() in k.lower() for s in ["token", "secret", "password", "key"])
        if isinstance(v, dict): redacted[k] = redact_sensitive_dict(v, profile)
        elif isinstance(v, list): redacted[k] = [redact_sensitive_dict(i, profile) if isinstance(i, dict) else (mask_secret_value(str(i)) if is_sensitive_key else i) for i in v]
        else: redacted[k] = mask_secret_value(str(v)) if is_sensitive_key and v else v
    return redacted

def scan_log_file_for_secrets(path: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"scanned": False, "issues_found": 0}
    if not path.exists(): return findings, summary
    try:
        if path.stat().st_size > profile.max_file_scan_mb * 1024 * 1024: return findings, summary
        summary["scanned"] = True
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f):
                det = detect_secret_like_value(line)
                if det["is_secret"]:
                     findings.append(SecurityFinding(
                        finding_id=build_security_finding_id("log_redaction", "secret_in_log", str(path), i+1),
                        category="log_redaction", severity="high", status="security_failed",
                        title="Secret found in log", description=f"Secret type {det['type']} found in log file.",
                        file_path=str(path), line_number=i+1, blocking=profile.fail_on_secret_leak
                     ))
                     summary["issues_found"] += 1
    except Exception: pass
    return findings, summary

def scan_observability_logs(log_dir: Path, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    if log_dir.exists():
        for path in log_dir.rglob("*.log"):
            f, _ = scan_log_file_for_secrets(path, profile)
            findings.extend(f)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}

def build_log_redaction_report(project_root: Path, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    return scan_observability_logs(project_root / "logs", profile)
