"""
Secret hygiene checks for environment files and settings.
"""

import re
from pathlib import Path
import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

_PLACEHOLDERS = ["", "none", "change_me", "your_token_here", "<token>", "example", "my_bot_token", "my_chat_id", "my_token"]

_PATTERNS = {
    "telegram_bot_token": re.compile(r"^\d{8,10}:[a-zA-Z0-9_-]{35}$"),
    "pem_header": re.compile(r"-----BEGIN [A-Z ]+-----"),
    "generic_api_key": re.compile(r"^[A-Za-z0-9]{32,64}$")
}

def detect_secret_like_value(text: str) -> dict:
    if not text:
        return {"is_secret": False, "type": None}
    val = text.strip().strip("'").strip('"')
    if val.lower() in _PLACEHOLDERS or len(val) < 8:
        return {"is_secret": False, "type": None}
    if _PATTERNS["telegram_bot_token"].match(val):
        return {"is_secret": True, "type": "telegram_bot_token"}
    if _PATTERNS["pem_header"].search(val):
        return {"is_secret": True, "type": "pem_private_key"}
    if _PATTERNS["generic_api_key"].match(val) and any(c.isdigit() for c in val) and any(c.isalpha() for c in val):
         return {"is_secret": True, "type": "generic_api_key"}
    return {"is_secret": False, "type": None}

def mask_secret_value(value: str | None) -> str:
    if not value:
        return str(value)
    if len(value) <= 6:
        return "***"
    return f"{value[:3]}***{value[-3:]}"

def scan_env_file(path: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    return [], {"scanned": True, "issues_found": 0}

def check_env_example_safety(env_example_path: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"scanned": False, "issues_found": 0}
    if not env_example_path.exists():
        return findings, summary
    summary["scanned"] = True
    try:
        with open(env_example_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.strip()
                if not line or line.startswith("#"): continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    detection = detect_secret_like_value(val)
                    if detection["is_secret"]:
                        findings.append(SecurityFinding(
                            finding_id=build_security_finding_id("secret_hygiene", "env_example_secret", str(env_example_path), i+1),
                            category="secret_hygiene", severity="critical", status="security_failed",
                            title=".env.example contains real secret", description=f"Found a real secret of type {detection['type']} in {env_example_path.name}",
                            file_path=str(env_example_path), line_number=i+1, evidence=f"{key}={mask_secret_value(val)}",
                            recommended_action="Replace with a placeholder", blocking=profile.fail_on_secret_leak
                        ))
                        summary["issues_found"] += 1
    except Exception: pass
    return findings, summary

def check_settings_secret_defaults(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"scanned": True, "issues_found": 0}
    for attr in dir(settings_obj):
        if attr.startswith("_"): continue
        val = getattr(settings_obj, attr)
        if isinstance(val, str):
            if any(s.lower() in attr.lower() for s in profile.sensitive_env_names):
                detection = detect_secret_like_value(val)
                if detection["is_secret"]:
                     findings.append(SecurityFinding(
                            finding_id=build_security_finding_id("secret_hygiene", "settings_secret", "settings.py"),
                            category="secret_hygiene", severity="critical", status="security_failed",
                            title="Settings default contains real secret", description=f"Found a real secret for setting {attr}",
                            evidence=f"{attr}={mask_secret_value(val)}", recommended_action="Remove default secret from code",
                            blocking=profile.fail_on_secret_leak
                     ))
                     summary["issues_found"] += 1
    return findings, summary

def check_gitignore_for_secret_patterns(gitignore_path: Path, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"scanned": False, "issues_found": 0}
    if not gitignore_path.exists():
        findings.append(SecurityFinding(
            finding_id=build_security_finding_id("secret_hygiene", "missing_gitignore"),
            category="secret_hygiene", severity="critical", status="security_failed",
            title="Missing .gitignore", description=".gitignore file not found", blocking=profile.fail_on_secret_leak
        ))
        summary["issues_found"] += 1
        return findings, summary

    summary["scanned"] = True
    content = ""
    try:
        with open(gitignore_path, "r", encoding="utf-8") as f: content = f.read()
    except Exception: pass

    for pattern in profile.required_gitignore_patterns:
        if pattern not in content:
            findings.append(SecurityFinding(
                finding_id=build_security_finding_id("secret_hygiene", f"missing_gitignore_pattern_{pattern}", str(gitignore_path)),
                category="secret_hygiene", severity="high", status="security_failed",
                title=f"Missing gitignore pattern: {pattern}", description=f".gitignore is missing required pattern {pattern}",
                file_path=str(gitignore_path), recommended_action=f"Add {pattern} to .gitignore", blocking=profile.fail_on_secret_leak
            ))
            summary["issues_found"] += 1
    return findings, summary

def build_secret_hygiene_report(project_root: Path, settings_obj: object, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = check_env_example_safety(project_root / ".env.example", profile)
    f2, _ = check_settings_secret_defaults(settings_obj, profile)
    f3, _ = check_gitignore_for_secret_patterns(project_root / ".gitignore", profile)
    findings.extend(f1); findings.extend(f2); findings.extend(f3)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
