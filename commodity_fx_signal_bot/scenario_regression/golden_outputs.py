import pandas as pd
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from scenario_regression.regression_models import GoldenOutputRecord, golden_output_record_to_dict, build_golden_output_id
from scenario_regression.regression_config import ScenarioRegressionProfile

class GoldenOutputRegistry:
    def __init__(self, golden_dir: Path):
        self.golden_dir = golden_dir
        self.golden_dir.mkdir(parents=True, exist_ok=True)
        self.manifest_file = self.golden_dir / "golden_output_manifest.csv"

    def add_golden_output(self, record: GoldenOutputRecord) -> Path:
        df = self.load_golden_outputs()
        row = golden_output_record_to_dict(record)
        if not df.empty and record.golden_id in df["golden_id"].values:
            df.loc[df["golden_id"] == record.golden_id] = pd.Series(row)
        else:
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        df.to_csv(self.manifest_file, index=False)
        return self.manifest_file

    def load_golden_outputs(self) -> pd.DataFrame:
        if self.manifest_file.exists():
            return pd.read_csv(self.manifest_file)
        return pd.DataFrame()

    def find_by_scenario(self, scenario_id: str) -> pd.DataFrame:
        df = self.load_golden_outputs()
        if not df.empty:
            return df[df["scenario_id"] == scenario_id]
        return df

    def summarize(self) -> dict:
        df = self.load_golden_outputs()
        if df.empty:
            return {"total_golden_outputs": 0}
        return {
            "total_golden_outputs": len(df),
            "by_scenario": df["scenario_id"].value_counts().to_dict() if "scenario_id" in df else {},
        }

def calculate_artifact_content_hash(path: Path) -> tuple[str | None, dict]:
    if not path.exists():
        return None, {"warnings": ["File does not exist"]}
    try:
        if path.stat().st_size > 100 * 1024 * 1024:
            return None, {"warnings": ["File too large, skipped hashing"]}
        hasher = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest(), {}
    except Exception as e:
        return None, {"warnings": [str(e)]}

def calculate_tabular_schema_hash(path: Path) -> tuple[str | None, dict]:
    if not path.exists() or path.suffix != ".csv":
        return None, {"warnings": ["Not a valid CSV for schema hashing"]}
    try:
        df = pd.read_csv(path, nrows=1)
        columns = sorted(df.columns.tolist())
        hasher = hashlib.md5(json.dumps(columns).encode("utf-8"))
        return hasher.hexdigest(), {}
    except Exception as e:
        return None, {"warnings": [str(e)]}

def build_golden_output_from_artifact(scenario_id: str, output_name: str, path: Path) -> GoldenOutputRecord:
    golden_id = build_golden_output_id(scenario_id, output_name)
    content_hash, content_meta = calculate_artifact_content_hash(path)
    schema_hash, schema_meta = calculate_tabular_schema_hash(path)

    row_count = None
    warnings = content_meta.get("warnings", []) + schema_meta.get("warnings", [])
    if path.exists() and path.suffix == ".csv":
        try:
            df = pd.read_csv(path)
            row_count = len(df)
        except Exception as e:
            warnings.append(str(e))

    return GoldenOutputRecord(
        golden_id=golden_id,
        scenario_id=scenario_id,
        output_name=output_name,
        output_type=path.suffix.lstrip("."),
        path=str(path),
        content_hash=content_hash,
        schema_hash=schema_hash,
        row_count=row_count,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        synthetic_only=True,
        warnings=warnings,
    )

def build_golden_outputs_for_scenario(scenario_id: str, expected_outputs_df: pd.DataFrame, project_root: Path) -> tuple[pd.DataFrame, dict]:
    records = []
    warnings = []
    if not expected_outputs_df.empty:
        for _, row in expected_outputs_df.iterrows():
            output_name = row.get("output_name", "unknown")
            output_path_str = row.get("output_path", "")
            if output_path_str:
                path = project_root / output_path_str
                record = build_golden_output_from_artifact(scenario_id, output_name, path)
                records.append(golden_output_record_to_dict(record))
            else:
                warnings.append(f"Missing output_path for {output_name}")

    df = pd.DataFrame(records)
    return df, {"warnings": warnings, "total": len(records)}

def build_golden_output_manifest(golden_df: pd.DataFrame) -> dict:
    if golden_df.empty:
        return {"records": []}
    return {"records": golden_df.to_dict(orient="records")}

def compare_current_outputs_to_golden(scenario_id: str, golden_df: pd.DataFrame, project_root: Path, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    # Basic comparison logic (to be expanded in snapshot_compare)
    if golden_df.empty:
        return pd.DataFrame(), {"warnings": ["No golden outputs provided for comparison"]}

    comparisons = []
    for _, row in golden_df.iterrows():
        path = project_root / str(row.get("path", ""))
        current_hash, _ = calculate_artifact_content_hash(path)
        comparisons.append({
            "golden_id": row.get("golden_id"),
            "scenario_id": scenario_id,
            "matched": current_hash == row.get("content_hash") if current_hash else False
        })
    return pd.DataFrame(comparisons), {"total_compared": len(comparisons)}
