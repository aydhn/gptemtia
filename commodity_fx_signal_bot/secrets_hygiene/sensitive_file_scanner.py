
import os
from pathlib import Path
import pandas as pd
from typing import Tuple
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import SensitiveFileRecord, build_sensitive_file_id, SecretFinding
from secrets_hygiene.secret_patterns import scan_text_for_secret_patterns
from secrets_hygiene.entropy_detector import scan_text_for_high_entropy_tokens

def should_scan_file(path: Path, project_root: Path, profile: SecretsHygieneProfile) -> dict:
    try: rel_path = str(path.relative_to(project_root))
    except ValueError: rel_path = str(path)
    allowed_exts = {".py", ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".csv"}
    if any(x in path.parts for x in [".git", "__pycache__", ".pytest_cache"]): return {"scan_allowed": False, "reason": "Ignored dir", "sensitive_hint": False}
    if any(x in path.parts for x in ["venv", ".venv", "node_modules"]): return {"scan_allowed": False, "reason": "Env dir", "sensitive_hint": False}
    if rel_path == ".env": return {"scan_allowed": False, "reason": "Skipping .env", "sensitive_hint": True}
    if rel_path.endswith((".pem", ".key")): return {"scan_allowed": False, "reason": "Skipping raw keys", "sensitive_hint": True}
    if path.suffix.lower() not in allowed_exts and not rel_path.endswith(".example") and not rel_path.endswith("requirements.txt"): return {"scan_allowed": False, "reason": "Ext not allowed", "sensitive_hint": False}
    if not path.is_file(): return {"scan_allowed": False, "reason": "Not a file", "sensitive_hint": False}
    try:
        if path.stat().st_size > profile.max_file_mb * 1024 * 1024: return {"scan_allowed": False, "reason": "Too large", "sensitive_hint": False}
    except Exception: return {"scan_allowed": False, "reason": "Cannot read size", "sensitive_hint": False}
    return {"scan_allowed": True, "reason": "Allowed", "sensitive_hint": False}

def discover_sensitive_scan_files(project_root: Path, profile: SecretsHygieneProfile) -> pd.DataFrame:
    records = []
    for root, dirs, files in os.walk(project_root):
        for d in ['.git', '__pycache__', 'venv']:
            if d in dirs: dirs.remove(d)
        for file in files:
            path = Path(root) / file
            try: rel_path = str(path.relative_to(project_root))
            except: rel_path = str(path)
            scan_info = should_scan_file(path, project_root, profile)
            records.append(SensitiveFileRecord(
                file_id=build_sensitive_file_id(rel_path), relative_path=rel_path, file_type=path.suffix or "unknown",
                size_bytes=path.stat().st_size if path.exists() else None, scan_allowed=scan_info["scan_allowed"],
                scan_reason=scan_info["reason"], sensitive_path_hint=scan_info["sensitive_hint"], warnings=[]
            ))
            if len(records) >= profile.max_files: break
        if len(records) >= profile.max_files: break
    return pd.DataFrame([r.__dict__ for r in records])

def scan_file_for_secrets(path: Path, project_root: Path, profile: SecretsHygieneProfile) -> Tuple[list[SecretFinding], dict]:
    try: rel_path = str(path.relative_to(project_root))
    except: rel_path = str(path)
    summary = {"scanned": False, "error": None}
    scan_info = should_scan_file(path, project_root, profile)
    if not scan_info["scan_allowed"]:
        summary["error"] = scan_info["reason"]
        return [], summary
    try:
        with open(path, "r", encoding="utf-8") as f: text = f.read()
    except Exception as e:
        summary["error"] = f"Failed to read: {e}"
        return [], summary
    findings = scan_text_for_secret_patterns(text, rel_path, profile) + scan_text_for_high_entropy_tokens(text, rel_path, profile)
    summary.update({"scanned": True, "finding_count": len(findings)})
    return findings, summary

def build_sensitive_file_inventory(project_root: Path, profile: SecretsHygieneProfile) -> Tuple[pd.DataFrame, dict]:
    df = discover_sensitive_scan_files(project_root, profile)
    return df, {"total_files": len(df), "scannable_files": len(df[df["scan_allowed"]]) if not df.empty else 0, "sensitive_hints": len(df[df["sensitive_path_hint"]]) if not df.empty else 0}

def build_sensitive_file_scan_report(project_root: Path, profile: SecretsHygieneProfile) -> Tuple[dict[str, pd.DataFrame], dict]:
    inv_df, inv_sum = build_sensitive_file_inventory(project_root, profile)
    patterns, entropy = [], []
    for rel_path in inv_df[inv_df["scan_allowed"]]["relative_path"].tolist() if not inv_df.empty else []:
        finds, _ = scan_file_for_secrets(project_root / rel_path, project_root, profile)
        patterns.extend([f for f in finds if f.finding_type != "high_entropy_finding"])
        entropy.extend([f for f in finds if f.finding_type == "high_entropy_finding"])
    return {"inventory": inv_df, "patterns": pd.DataFrame([f.__dict__ for f in patterns]), "entropy": pd.DataFrame([f.__dict__ for f in entropy])}, {"inventory": inv_sum, "pattern_findings_count": len(patterns), "entropy_findings_count": len(entropy)}
