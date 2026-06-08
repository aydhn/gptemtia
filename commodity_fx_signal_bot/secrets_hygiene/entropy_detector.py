
import math
import re
import pandas as pd
from typing import Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import SecretFinding, build_secret_finding_id
from secrets_hygiene.redaction import mask_secret_value

def calculate_shannon_entropy(value: str) -> float:
    if not value: return 0.0
    entropy = 0.0
    for x in set(value):
        p_x = float(value.count(x)) / len(value)
        if p_x > 0: entropy += - p_x * math.log(p_x, 2)
    return entropy

def extract_candidate_tokens(text: str) -> list[dict]:
    candidates = []
    if not text: return candidates
    token_regex = re.compile(r'\b([A-Za-z0-9+/=_-]{16,})\b')
    for i, line in enumerate(text.split('\n')):
        for match in token_regex.finditer(line):
            candidates.append({"line_number": i + 1, "column_start": match.start(), "raw_value": match.group(1)})
    return candidates

def filter_entropy_false_positives(candidates: list[dict]) -> list[dict]:
    filtered = []
    uuid_pattern = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
    hex_pattern = re.compile(r'^[0-9a-fA-F]+$')
    for c in candidates:
        val = c["raw_value"]
        if uuid_pattern.match(val): c.update({"is_false_positive": True, "reason": "uuid"})
        elif hex_pattern.match(val) and len(val) in [32, 40, 64, 128]: c.update({"is_false_positive": True, "reason": "hash"})
        else: c["is_false_positive"] = False
        filtered.append(c)
    return filtered

def scan_text_for_high_entropy_tokens(text: str, relative_path: str, profile: SecretsHygieneProfile) -> list[SecretFinding]:
    findings = []
    if not text: return findings
    for c in filter_entropy_false_positives(extract_candidate_tokens(text)):
        entropy = calculate_shannon_entropy(c["raw_value"])
        if entropy >= profile.entropy_threshold:
            severity = "low_secret_warning" if c.get("is_false_positive") else "medium_secret_risk"
            masked_val = mask_secret_value(c["raw_value"], profile.mask_keep_start, profile.mask_keep_end)
            findings.append(SecretFinding(
                finding_id=build_secret_finding_id(relative_path, c["line_number"], "high_entropy", masked_val),
                finding_type="high_entropy_finding", severity=severity, relative_path=relative_path,
                line_number=c["line_number"], column_start=c["column_start"], masked_value=masked_val,
                pattern_name="high_entropy", confidence=0.5, redaction_status="redacted_ok",
                warnings=[f"Entropy {entropy:.2f} >= {profile.entropy_threshold}"]
            ))
    return findings

def summarize_entropy_findings(findings_df: pd.DataFrame) -> dict:
    if findings_df is None or findings_df.empty: return {"total_entropy_findings": 0, "medium_risk_count": 0}
    return {"total_entropy_findings": len(findings_df), "medium_risk_count": len(findings_df[findings_df["severity"] == "medium_secret_risk"])}
