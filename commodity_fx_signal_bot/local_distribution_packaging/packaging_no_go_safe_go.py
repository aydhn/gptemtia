import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile

def build_packaging_governance_no_go_conditions(profile: LocalDistributionPackagingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "real archive creation claim", "type": "no-go"},
        {"condition": "ZIP/TAR/RAR/7z generated claim", "type": "no-go"},
        {"condition": "binary artifact generated claim", "type": "no-go"},
        {"condition": "installer generated claim", "type": "no-go"},
        {"condition": "executable package claim", "type": "no-go"},
        {"condition": "package publish claim", "type": "no-go"},
        {"condition": "docker build/push claim", "type": "no-go"},
        {"condition": "git tag claim", "type": "no-go"},
        {"condition": "cloud upload claim", "type": "no-go"},
        {"condition": "deployment claim", "type": "no-go"},
        {"condition": "official release claim", "type": "no-go"},
        {"condition": "official handover claim", "type": "no-go"},
        {"condition": "legal/compliance approval claim", "type": "no-go"},
        {"condition": "production approval claim", "type": "no-go"},
        {"condition": "official acceptance claim", "type": "no-go"},
        {"condition": "broker readiness claim", "type": "no-go"},
        {"condition": "live trading claim", "type": "no-go"},
        {"condition": "investment advice wording", "type": "no-go"},
        {"condition": "model deployment claim", "type": "no-go"},
        {"condition": "web server/dashboard claim", "type": "no-go"},
        {"condition": "telemetry claim", "type": "no-go"},
        {"condition": "external LLM/API claim", "type": "no-go"},
        {"condition": "vector/embedding claim", "type": "no-go"},
        {"condition": "raw secret output", "type": "no-go"},
        {"condition": "file deletion/move/overwrite claim", "type": "no-go"}
    ])

def build_packaging_governance_safe_go_conditions(profile: LocalDistributionPackagingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "distribution bundle rehearsal documented", "type": "safe-go"},
        {"condition": "portable docs bundle documented", "type": "safe-go"},
        {"condition": "release folder manifest documented", "type": "safe-go"},
        {"condition": "ZIP-map documented", "type": "safe-go"},
        {"condition": "inclusion/exclusion matrices available", "type": "safe-go"},
        {"condition": "packaging governance binder available", "type": "safe-go"},
        {"condition": "source/output/command maps available", "type": "safe-go"},
        {"condition": "no real archive/release/publish/deploy/live/broker/advice", "type": "safe-go"},
        {"condition": "manual review required", "type": "safe-go"}
    ])

def build_packaging_governance_no_go_safe_go_summary(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_packaging_governance_no_go_conditions(profile)
    safe_go = build_packaging_governance_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_packaging_no_go_safe_go(df)

def summarize_packaging_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(summary_df)}
