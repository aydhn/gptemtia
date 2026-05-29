import pandas as pd
from scenario_regression.regression_config import ScenarioRegressionProfile

def detect_golden_output_drift(golden_compare_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> pd.DataFrame:
    if golden_compare_df.empty:
        return pd.DataFrame()

    results = []
    for _, row in golden_compare_df.iterrows():
        matched = row.get("matched", False)
        drift = "no_drift" if matched else "unexpected_output_drift"
        results.append({
            "scenario_id": row.get("scenario_id"),
            "drift_type": "golden_output",
            "drift_label": drift
        })
    return pd.DataFrame(results)

def detect_snapshot_drift(snapshot_diff_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> pd.DataFrame:
    if snapshot_diff_df.empty:
        return pd.DataFrame()

    results = []
    for _, row in snapshot_diff_df.iterrows():
        diff_label = row.get("diff_label")
        if diff_label == "snapshot_identical":
            drift = "no_drift"
        elif diff_label in ["snapshot_numeric_diff_within_tolerance", "snapshot_text_diff_within_tolerance"]:
            drift = "minor_expected_drift"
        elif diff_label == "snapshot_major_diff":
            if row.get("schema_changed"):
                drift = "schema_drift"
            else:
                drift = "unexpected_output_drift"
        elif diff_label == "snapshot_missing":
            drift = "missing_output_drift"
        else:
            drift = "unknown_drift"

        results.append({
            "scenario_id": row.get("scenario_id"),
            "drift_type": "snapshot",
            "drift_label": drift
        })
    return pd.DataFrame(results)

def detect_replay_consistency_drift(replay_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> pd.DataFrame:
    if replay_df.empty:
        return pd.DataFrame()

    results = []
    for _, row in replay_df.iterrows():
        status = row.get("replay_status")
        drift = "no_drift" if status == "replay_consistent" else "replay_drift"
        results.append({
            "scenario_id": row.get("scenario_id"),
            "drift_type": "replay",
            "drift_label": drift
        })
    return pd.DataFrame(results)

def build_scenario_drift_report(golden_compare_df: pd.DataFrame | None, snapshot_diff_df: pd.DataFrame | None, replay_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    dfs = []
    if golden_compare_df is not None and not golden_compare_df.empty:
        dfs.append(detect_golden_output_drift(golden_compare_df, profile))
    if snapshot_diff_df is not None and not snapshot_diff_df.empty:
        dfs.append(detect_snapshot_drift(snapshot_diff_df, profile))
    if replay_df is not None and not replay_df.empty:
        dfs.append(detect_replay_consistency_drift(replay_df, profile))

    if not dfs:
        return pd.DataFrame(), {"warnings": ["No data provided to detect drift"]}

    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df, summarize_scenario_drift(combined_df)

def summarize_scenario_drift(drift_df: pd.DataFrame) -> dict:
    if drift_df.empty:
        return {"total_drift_records": 0}
    return {
        "total_drift_records": len(drift_df),
        "by_label": drift_df["drift_label"].value_counts().to_dict() if "drift_label" in drift_df else {},
        "by_type": drift_df["drift_type"].value_counts().to_dict() if "drift_type" in drift_df else {},
    }
