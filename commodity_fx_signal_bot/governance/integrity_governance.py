import pandas as pd


def check_artifact_integrity_from_record(record: dict) -> dict:
    issues = []

    # Needs a path
    if not record.get("path"):
        issues.append("Missing path")

    size = record.get("size_bytes")
    if size is None or size == 0:
        issues.append("Size is zero or unknown")

    ext = record.get("extension", "")

    if ext in [".csv", ".parquet"]:
        if not record.get("schema_fingerprint"):
            issues.append("Missing schema_fingerprint for tabular data")

    if not record.get("content_fingerprint") and "size_limit" not in str(record.get("warnings", [])):
        issues.append("Missing content fingerprint without size limit reason")

    if record.get("warnings"):
        issues.append("Has extraction warnings")

    return {
        "is_intact": len(issues) == 0,
        "issues": issues
    }

def build_integrity_governance_table(inventory_df: pd.DataFrame) -> pd.DataFrame:
    records = []
    if inventory_df.empty:
        return pd.DataFrame()

    for _, row in inventory_df.iterrows():
        rec_dict = row.to_dict()
        check = check_artifact_integrity_from_record(rec_dict)

        records.append({
            "artifact_id": row["artifact_id"],
            "artifact_type": row["artifact_type"],
            "path": row["relative_path"],
            "is_intact": check["is_intact"],
            "issues": check["issues"]
        })

    return pd.DataFrame(records)

def summarize_integrity_governance(integrity_df: pd.DataFrame) -> dict:
    if integrity_df.empty:
        return {"total": 0}

    intact = len(integrity_df[integrity_df["is_intact"] == True])
    failed = len(integrity_df[integrity_df["is_intact"] == False])

    return {
        "total": len(integrity_df),
        "intact_count": intact,
        "failed_count": failed,
        "note": "Integrity passed is NOT a production compliance approval."
    }

def identify_integrity_risk_artifacts(integrity_df: pd.DataFrame) -> pd.DataFrame:
    if integrity_df.empty:
        return pd.DataFrame()
    return integrity_df[integrity_df["is_intact"] == False]
