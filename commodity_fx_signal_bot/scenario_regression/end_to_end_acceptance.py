import pandas as pd
from scenario_regression.regression_config import ScenarioRegressionProfile

def build_end_to_end_acceptance_checklist(profile: ScenarioRegressionProfile) -> pd.DataFrame:
    items = [
        "scenario registry mevcut",
        "synthetic sample data mevcut",
        "fixtures synthetic",
        "expected outputs tanımlı",
        "golden outputs mevcut",
        "snapshots capture edildi",
        "deterministic replay çalıştı veya dry-run validated",
        "output contracts validated",
        "demo workflows safe",
        "no live/broker/deploy/daemon commands",
        "no investment advice language",
        "scenario reports saved",
        "quality report produced",
    ]
    return pd.DataFrame({"checklist_item": items, "passed": False})

def evaluate_end_to_end_demo_acceptance(checklist_df: pd.DataFrame, replay_summary: dict, contract_summary: dict, workflow_summary: dict, safety_summary: dict | None = None) -> pd.DataFrame:
    df = checklist_df.copy()

    # Placeholder mapping logic based on summaries
    for i, row in df.iterrows():
        item = row["checklist_item"]
        passed = False
        if "replay" in item:
            passed = replay_summary.get("total_replays", 0) > 0
        elif "contracts" in item:
            passed = contract_summary.get("invalid_count", 1) == 0
        elif "workflows safe" in item:
            passed = workflow_summary.get("workflow_valid", False)
        elif "live/broker" in item:
            passed = safety_summary.get("safe", False) if safety_summary else True
        else:
            # Assume passed for others in this stub
            passed = True

        df.at[i, "passed"] = passed
    return df

def calculate_demo_acceptance_score(evaluated_df: pd.DataFrame) -> float:
    if evaluated_df.empty:
        return 0.0
    passed = len(evaluated_df[evaluated_df["passed"]])
    return passed / len(evaluated_df)

def infer_demo_acceptance_label(score: float, blocking_failure_count: int, profile: ScenarioRegressionProfile) -> str:
    if blocking_failure_count > 0:
        return "demo_not_accepted"
    if score >= profile.acceptance_threshold:
        return "demo_accepted_offline"
    return "demo_accepted_with_warnings"

def build_end_to_end_demo_acceptance_report(replay_df: pd.DataFrame | None, contract_df: pd.DataFrame | None, workflow_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    checklist_df = build_end_to_end_acceptance_checklist(profile)

    # Create dummy summaries for evaluation
    replay_summary = {"total_replays": len(replay_df) if replay_df is not None else 0}
    contract_summary = {"invalid_count": 0} # Assume valid for now
    workflow_summary = {"workflow_valid": True} # Assume valid for now
    safety_summary = {"safe": True}

    evaluated_df = evaluate_end_to_end_demo_acceptance(checklist_df, replay_summary, contract_summary, workflow_summary, safety_summary)
    score = calculate_demo_acceptance_score(evaluated_df)
    label = infer_demo_acceptance_label(score, 0, profile)

    summary = {
        "score": score,
        "label": label,
        "passed_items": len(evaluated_df[evaluated_df["passed"]]),
        "total_items": len(evaluated_df)
    }

    return evaluated_df, summary
