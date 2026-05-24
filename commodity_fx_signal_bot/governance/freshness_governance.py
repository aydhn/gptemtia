from datetime import datetime, timezone

import pandas as pd


def calculate_artifact_age_hours(modified_at_utc: str | None) -> float | None:
    if not modified_at_utc:
        return None
    try:
        dt = datetime.fromisoformat(modified_at_utc.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        diff = now - dt
        return diff.total_seconds() / 3600.0
    except Exception:
        return None

def classify_artifact_freshness(age_hours: float | None, artifact_type: str) -> str:
    if age_hours is None:
        return "unknown_freshness"

    # Example thresholds (can be customized)
    if age_hours < 24:
        return "fresh"
    elif age_hours < 72:
        return "acceptable"
    elif age_hours < 168:
        return "stale"
    else:
        return "very_stale"

def build_freshness_governance_table(inventory_df: pd.DataFrame) -> pd.DataFrame:
    records = []
    if inventory_df.empty:
        return pd.DataFrame()

    for _, row in inventory_df.iterrows():
        age = calculate_artifact_age_hours(row.get("modified_at_utc"))
        label = classify_artifact_freshness(age, row.get("artifact_type"))

        records.append({
            "artifact_id": row["artifact_id"],
            "artifact_type": row["artifact_type"],
            "path": row["relative_path"],
            "age_hours": age,
            "freshness": label
        })

    return pd.DataFrame(records)

def summarize_freshness_governance(freshness_df: pd.DataFrame) -> dict:
    if freshness_df.empty:
        return {"total": 0}

    stale_count = len(freshness_df[freshness_df["freshness"].isin(["stale", "very_stale"])])

    warnings = []
    if stale_count > 0:
        warnings.append("Note: Stale freshness is a data maintenance warning, NOT a live trade alarm.")

    return {
        "total": len(freshness_df),
        "labels": freshness_df["freshness"].value_counts().to_dict(),
        "stale_count": stale_count,
        "warnings": warnings
    }
