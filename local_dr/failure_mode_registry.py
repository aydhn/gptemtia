import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import FailureMode, build_failure_mode_id, failure_mode_to_dict

def build_default_failure_modes(profile: LocalDRProfile) -> list[FailureMode]:
    return [
        FailureMode(
            failure_id=build_failure_mode_id("archive_restore_dr", "Corruption"),
            domain_label="archive_restore_dr",
            failure_name="Corruption",
            severity="high"
        )
    ]

def classify_failure_severity(failure_name: str, domain_label: str) -> str:
    if "corruption" in failure_name.lower():
        return "high"
    return "medium"

def build_failure_mode_registry(profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    modes = build_default_failure_modes(profile)
    df = pd.DataFrame([failure_mode_to_dict(m) for m in modes])
    summary = summarize_failure_modes(df)
    return df, summary

def summarize_failure_modes(failure_df: pd.DataFrame) -> dict:
    return {
        "total_failures": len(failure_df),
        "high_severity_failures": len(failure_df[failure_df.get("severity") == "high"]) if "severity" in failure_df else 0,
    }
