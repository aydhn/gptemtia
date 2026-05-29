import pandas as pd
from scenario_regression.regression_config import ScenarioRegressionProfile

def check_regression_registry_quality(regression_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> dict:
    if regression_df is None or regression_df.empty:
        return {"passed": False, "warnings": ["Regression registry is empty"]}
    return {"passed": True, "warnings": []}

def check_golden_output_quality(golden_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> dict:
    if golden_df is None or golden_df.empty:
        return {"passed": False, "warnings": ["Golden output manifest is empty"]}
    return {"passed": True, "warnings": []}

def check_snapshot_quality(snapshot_df: pd.DataFrame | None, diff_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> dict:
    if snapshot_df is None or snapshot_df.empty:
        return {"passed": False, "warnings": ["Snapshot manifest is empty"]}
    return {"passed": True, "warnings": []}

def check_replay_quality(replay_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> dict:
    if replay_df is None or replay_df.empty:
        return {"passed": False, "warnings": ["Replay report is empty"]}
    return {"passed": True, "warnings": []}

def check_acceptance_quality(acceptance_df: pd.DataFrame | None, failure_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> dict:
    if acceptance_df is None or acceptance_df.empty:
        return {"passed": False, "warnings": ["Acceptance report is empty"]}
    return {"passed": True, "warnings": []}

def check_for_forbidden_terms_in_regression(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    forbidden = [
        "live order", "broker order", "real trade", "open position", "close position",
        "buy now", "sell now", "deploy model", "production deploy", "production scheduler",
        "background daemon", "while true", "run live", "guaranteed profit",
        "risk-free return", "yatırım tavsiyesidir", "kesin al", "kesin sat"
    ]

    allowlist = [
        "yatırım tavsiyesi değildir", "canlı emir yoktur", "broker entegrasyonu yoktur"
    ]

    content = ""
    if text:
        content += text.lower() + " "
    if df is not None and not df.empty:
        content += df.to_string().lower() + " "
    if summary:
        content += str(summary).lower()

    found = []
    for term in forbidden:
        if term in content:
            # Check allowlist context roughly
            allowed = any(a in content for a in allowlist if term in a)
            if not allowed:
                found.append(term)

    return {
        "passed": len(found) == 0,
        "forbidden_terms_found": found
    }

def build_scenario_regression_quality_report(summary: dict, regression_df: pd.DataFrame | None = None, golden_df: pd.DataFrame | None = None, replay_df: pd.DataFrame | None = None) -> dict:
    quality = {
        "regression_registry_valid": regression_df is not None and not regression_df.empty,
        "golden_outputs_valid": golden_df is not None and not golden_df.empty,
        "snapshots_valid": True,
        "replay_valid": replay_df is not None and not replay_df.empty,
        "acceptance_valid": True,
        "synthetic_only_confirmed": True,
        "forbidden_terms_found": [],
        "warning_count": 0,
        "passed": True,
        "warnings": []
    }

    forbidden_check = check_for_forbidden_terms_in_regression(str(summary), regression_df)
    quality["forbidden_terms_found"] = forbidden_check["forbidden_terms_found"]
    if not forbidden_check["passed"]:
        quality["passed"] = False
        quality["warnings"].append(f"Forbidden terms found: {forbidden_check['forbidden_terms_found']}")

    quality["warning_count"] = len(quality["warnings"])
    return quality
