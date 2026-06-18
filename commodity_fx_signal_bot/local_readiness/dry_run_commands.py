import pandas as pd
from .readiness_config import LocalReadinessProfile

FORBIDDEN_TERMS = [
    "live", "broker order", "buy", "sell", "open position", "close position",
    "deploy", "daemon", "server", "cloud upload", "external llm", "real market download",
    "scraping", "delete", "overwrite"
]

def build_dry_run_command_checklist(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    from .operator_checklist import build_safe_operator_command_sequence
    df, _ = build_safe_operator_command_sequence(profile)

    results = []
    for cmd in df["safe_command"].tolist():
        safety = classify_command_safety(cmd)
        results.append({
            "command": cmd,
            "is_safe": safety["is_safe"],
            "forbidden_terms": safety["forbidden_terms"]
        })
    res_df = pd.DataFrame(results)
    return res_df, summarize_dry_run_commands(res_df)

def classify_command_safety(command: str) -> dict:
    forbidden = detect_forbidden_command_terms(command)
    return {
        "is_safe": len(forbidden) == 0,
        "forbidden_terms": forbidden
    }

def detect_forbidden_command_terms(command: str) -> list[str]:
    found = []
    cmd_lower = command.lower()
    for term in FORBIDDEN_TERMS:
        if term in cmd_lower:
            found.append(term)
    return found

def summarize_dry_run_commands(command_df: pd.DataFrame) -> dict:
    return {
        "total_commands": len(command_df),
        "safe_commands": len(command_df[command_df["is_safe"] == True]),
        "unsafe_commands": len(command_df[command_df["is_safe"] == False])
    }
