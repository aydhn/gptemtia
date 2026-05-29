import pandas as pd
from pathlib import Path
from datetime import datetime, timezone
from scenario_regression.regression_models import SnapshotRecord, snapshot_record_to_dict, build_snapshot_id
from scenario_regression.golden_outputs import calculate_artifact_content_hash, calculate_tabular_schema_hash
from scenario_regression.regression_config import ScenarioRegressionProfile

def capture_snapshot_for_artifact(scenario_id: str, snapshot_name: str, path: Path, profile: ScenarioRegressionProfile) -> SnapshotRecord:
    captured_at = datetime.now(timezone.utc).isoformat()
    snapshot_id = build_snapshot_id(scenario_id, snapshot_name, captured_at)

    content_hash, content_meta = calculate_artifact_content_hash(path)
    schema_hash, schema_meta = calculate_tabular_schema_hash(path)

    row_count = None
    warnings = content_meta.get("warnings", []) + schema_meta.get("warnings", [])

    if path.exists() and path.suffix == ".csv":
        try:
            df = pd.read_csv(path)
            row_count = len(df)
            if row_count > profile.max_snapshot_rows:
                warnings.append(f"Row count {row_count} exceeds max {profile.max_snapshot_rows}, capping for snapshot")
                row_count = profile.max_snapshot_rows
        except Exception as e:
            warnings.append(str(e))

    return SnapshotRecord(
        snapshot_id=snapshot_id,
        scenario_id=scenario_id,
        snapshot_name=snapshot_name,
        artifact_type=path.suffix.lstrip("."),
        path=str(path),
        content_hash=content_hash,
        schema_hash=schema_hash,
        row_count=row_count,
        captured_at_utc=captured_at,
        warnings=warnings,
    )

def capture_snapshots_for_scenario(scenario_id: str, output_paths: list[str], profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    records = []
    warnings = []

    for path_str in output_paths:
        path = Path(path_str)
        snapshot_name = path.stem
        record = capture_snapshot_for_artifact(scenario_id, snapshot_name, path, profile)
        records.append(snapshot_record_to_dict(record))
        if not path.exists():
            warnings.append(f"Artifact {path_str} does not exist for snapshot capture")

    df = pd.DataFrame(records)
    return df, {"warnings": warnings, "total_captured": len(records)}

def build_snapshot_manifest(snapshot_df: pd.DataFrame) -> dict:
    if snapshot_df.empty:
        return {"records": []}
    return {"records": snapshot_df.to_dict(orient="records")}

def load_latest_snapshots(snapshot_dir: Path, scenario_id: str | None = None) -> pd.DataFrame:
    manifest_file = snapshot_dir / "snapshot_manifest.csv"
    if not manifest_file.exists():
        return pd.DataFrame()
    df = pd.read_csv(manifest_file)
    if scenario_id and not df.empty and "scenario_id" in df.columns:
        df = df[df["scenario_id"] == scenario_id]

    if not df.empty and "captured_at_utc" in df.columns:
        # Group by scenario_id and snapshot_name, taking the latest
        df = df.sort_values("captured_at_utc").groupby(["scenario_id", "snapshot_name"]).tail(1).reset_index(drop=True)
    return df

def summarize_snapshots(snapshot_df: pd.DataFrame) -> dict:
    if snapshot_df.empty:
        return {"total_snapshots": 0}
    return {
        "total_snapshots": len(snapshot_df),
        "by_scenario": snapshot_df["scenario_id"].value_counts().to_dict() if "scenario_id" in snapshot_df else {},
    }
