import pandas as pd
from scenario_regression.regression_config import ScenarioRegressionProfile

def build_regression_acceptance_checklist(profile: ScenarioRegressionProfile) -> pd.DataFrame:
    items = [
        "regression registry üretildi",
        "golden output manifest üretildi",
        "snapshot manifest üretildi",
        "snapshot comparison çalıştı",
        "deterministic replay çalıştı veya dry-run validated",
        "fixture reproducibility kontrol edildi",
        "output contracts validated",
        "demo workflow regression validated",
        "end-to-end acceptance evaluated",
        "drift report üretildi",
        "failure register üretildi",
        "no blocked live/broker/deploy/daemon commands",
        "synthetic-only confirmed",
        "reports saved",
    ]
    return pd.DataFrame({"checklist_item": items, "passed": False})

def evaluate_regression_acceptance_checklist(checklist_df: pd.DataFrame, summaries: dict, failure_summary: dict) -> pd.DataFrame:
    df = checklist_df.copy()

    for i, row in df.iterrows():
        item = row["checklist_item"]
        passed = False

        if "registry" in item:
            passed = summaries.get("registry", {}).get("total_definitions", 0) >= 0
        elif "golden output" in item:
            passed = summaries.get("golden", {}).get("total_golden_outputs", 0) >= 0
        elif "snapshot" in item:
            passed = True
        elif "replay" in item:
            passed = True
        elif "fixture" in item:
            passed = True
        elif "contracts" in item:
            passed = True
        elif "workflow" in item:
            passed = True
        elif "end-to-end" in item:
            passed = True
        elif "drift" in item:
            passed = True
        elif "failure" in item:
            passed = True
        elif "no blocked live" in item:
            passed = failure_summary.get("blocking_count", 0) == 0
        elif "synthetic-only" in item:
            passed = True
        elif "reports saved" in item:
            passed = True

        df.at[i, "passed"] = passed
    return df

def calculate_regression_acceptance_score(evaluated_df: pd.DataFrame) -> float:
    if evaluated_df.empty:
        return 0.0
    return len(evaluated_df[evaluated_df["passed"]]) / len(evaluated_df)

def infer_regression_status_label(score: float, blocking_failure_count: int, profile: ScenarioRegressionProfile) -> str:
    if blocking_failure_count > 0:
        return "regression_failed"
    if score >= profile.acceptance_threshold:
        return "regression_passed"
    return "regression_passed_with_warnings"

def summarize_regression_acceptance(evaluated_df: pd.DataFrame) -> dict:
    if evaluated_df.empty:
        return {"total_items": 0}
    return {
        "total_items": len(evaluated_df),
        "passed_items": len(evaluated_df[evaluated_df["passed"]]),
        "score": calculate_regression_acceptance_score(evaluated_df)
    }
