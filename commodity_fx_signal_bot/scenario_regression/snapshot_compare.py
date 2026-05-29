import pandas as pd
from scenario_regression.regression_models import SnapshotDiff, snapshot_diff_to_dict, build_snapshot_diff_id
from scenario_regression.regression_config import ScenarioRegressionProfile

def classify_snapshot_diff(numeric_diff_score: float | None, text_similarity_score: float | None, schema_changed: bool, row_count_changed: bool, profile: ScenarioRegressionProfile) -> str:
    if schema_changed:
        return "snapshot_major_diff"

    if numeric_diff_score is not None:
        if numeric_diff_score == 0.0:
            if not row_count_changed and text_similarity_score in [1.0, None]:
                return "snapshot_identical"
        if numeric_diff_score <= profile.numeric_tolerance:
            if not row_count_changed:
                return "snapshot_numeric_diff_within_tolerance"
            return "snapshot_minor_diff"
        return "snapshot_major_diff"

    if text_similarity_score is not None:
        if text_similarity_score >= profile.text_similarity_threshold:
            if not row_count_changed:
                return "snapshot_text_diff_within_tolerance"
            return "snapshot_minor_diff"
        return "snapshot_major_diff"

    if row_count_changed:
        return "snapshot_minor_diff"

    return "snapshot_identical"

def compare_snapshot_records(baseline: dict, current: dict, profile: ScenarioRegressionProfile) -> SnapshotDiff:
    diff_id = build_snapshot_diff_id(baseline.get("snapshot_id", ""), current.get("snapshot_id", ""))
    scenario_id = current.get("scenario_id", "")

    warnings = []
    schema_changed = baseline.get("schema_hash") != current.get("schema_hash")
    row_count_changed = baseline.get("row_count") != current.get("row_count")

    # Placeholder for actual diff scores
    numeric_diff_score = 0.0 if baseline.get("content_hash") == current.get("content_hash") else 1.0
    text_similarity_score = 1.0 if baseline.get("content_hash") == current.get("content_hash") else 0.0

    diff_label = classify_snapshot_diff(numeric_diff_score, text_similarity_score, schema_changed, row_count_changed, profile)

    if diff_label == "snapshot_major_diff":
        warnings.append("Major differences detected between snapshots")

    return SnapshotDiff(
        diff_id=diff_id,
        scenario_id=scenario_id,
        baseline_snapshot_id=baseline.get("snapshot_id", ""),
        current_snapshot_id=current.get("snapshot_id", ""),
        diff_label=diff_label,
        numeric_diff_score=numeric_diff_score,
        text_similarity_score=text_similarity_score,
        schema_changed=schema_changed,
        row_count_changed=row_count_changed,
        warnings=warnings,
    )

def compare_snapshot_tables(baseline_df: pd.DataFrame, current_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    diffs = []
    warnings = []

    if current_df.empty:
        warnings.append("Current snapshot table is empty")
        return pd.DataFrame(), {"warnings": warnings}

    for _, curr_row in current_df.iterrows():
        scenario_id = curr_row.get("scenario_id")
        snapshot_name = curr_row.get("snapshot_name")

        baseline_matches = pd.DataFrame()
        if not baseline_df.empty and "scenario_id" in baseline_df and "snapshot_name" in baseline_df:
            baseline_matches = baseline_df[(baseline_df["scenario_id"] == scenario_id) & (baseline_df["snapshot_name"] == snapshot_name)]

        if baseline_matches.empty:
            diffs.append(snapshot_diff_to_dict(SnapshotDiff(
                diff_id=build_snapshot_diff_id("missing", curr_row.get("snapshot_id", "")),
                scenario_id=scenario_id,
                baseline_snapshot_id="missing",
                current_snapshot_id=curr_row.get("snapshot_id", ""),
                diff_label="snapshot_missing",
                numeric_diff_score=None,
                text_similarity_score=None,
                schema_changed=True,
                row_count_changed=True,
                warnings=["Baseline snapshot missing"],
            )))
            warnings.append(f"Missing baseline for {snapshot_name}")
        else:
            base_row = baseline_matches.iloc[0].to_dict()
            diff = compare_snapshot_records(base_row, curr_row.to_dict(), profile)
            diffs.append(snapshot_diff_to_dict(diff))

    df = pd.DataFrame(diffs)
    return df, {"warnings": warnings, "total_diffs": len(diffs)}

def build_snapshot_diff_report(baseline_df: pd.DataFrame, current_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    return compare_snapshot_tables(baseline_df, current_df, profile)
