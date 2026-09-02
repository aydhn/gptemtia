"""
Archival No-Go Safe-Go.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def build_archival_no_go_conditions(profile: LocalArchivalProfile) -> pd.DataFrame:
    conditions = [
        {"condition": "raw secret included in hash output", "status": "no-go"},
        {"condition": "sensitive file hashed", "status": "no-go"},
        {"condition": ".env hashed", "status": "no-go"},
        {"condition": "cloud archive claim", "status": "no-go"},
        {"condition": "legal hold claim", "status": "no-go"},
        {"condition": "compliance claim", "status": "no-go"},
        {"condition": "immutable lock claim", "status": "no-go"},
        {"condition": "chmod/permission change claim", "status": "no-go"},
        {"condition": "package publish claim", "status": "no-go"},
        {"condition": "live/broker/deploy claim", "status": "no-go"},
        {"condition": "investment advice wording", "status": "no-go"}
    ]
    return pd.DataFrame(conditions)

def build_archival_safe_go_conditions(profile: LocalArchivalProfile) -> pd.DataFrame:
    conditions = [
        {"condition": "local-only archival rehearsal documented", "status": "safe-go"},
        {"condition": "sensitive exclusions documented", "status": "safe-go"},
        {"condition": "hash policy documented", "status": "safe-go"},
        {"condition": "hash catalog generated", "status": "safe-go"},
        {"condition": "hash-of-hashes generated", "status": "safe-go"},
        {"condition": "provenance lockfile generated", "status": "safe-go"},
        {"condition": "custody guide generated", "status": "safe-go"},
        {"condition": "manual review required", "status": "safe-go"}
    ]
    return pd.DataFrame(conditions)

def build_archival_no_go_safe_go_summary(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    nogo = build_archival_no_go_conditions(profile)
    safego = build_archival_safe_go_conditions(profile)
    df = pd.concat([nogo, safego], ignore_index=True)
    return df, summarize_archival_no_go_safe_go(df)

def summarize_archival_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total_conditions": len(summary_df) if summary_df is not None else 0}
