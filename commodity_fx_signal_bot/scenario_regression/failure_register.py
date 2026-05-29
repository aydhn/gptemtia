import pandas as pd
from scenario_regression.regression_models import RegressionFailure, regression_failure_to_dict, build_regression_failure_id

def classify_failure_severity(row: pd.Series) -> str:
    msg = str(row.get("description", "")).lower()
    if "live" in msg or "broker" in msg or "deploy" in msg:
        return "critical_regression_failure"
    if "synthetic not" in msg or "missing" in msg or "schema changed" in msg:
        return "high_regression_failure"
    if "inconsistent" in msg:
        return "medium_regression_failure"
    if "warning" in msg:
        return "low_regression_warning"
    return "informational_regression_note"

def build_failures_from_regression_results(regression_tables: dict[str, pd.DataFrame], summaries: dict | None = None) -> list[RegressionFailure]:
    failures = []

    # Generic extraction logic from tables
    for tbl_name, df in regression_tables.items():
        if df is None or df.empty:
            continue

        if "warnings" in df.columns:
            for _, row in df.iterrows():
                warns = row["warnings"]
                if not warns:
                    continue
                warn_list = warns.split(";") if isinstance(warns, str) else warns
                for w in warn_list:
                    if not w.strip():
                        continue
                    desc = pd.Series({"description": w})
                    sev = classify_failure_severity(desc)
                    blocking = sev in ["critical_regression_failure", "high_regression_failure"]

                    scenario_id = row.get("scenario_id", "unknown")
                    fail_id = build_regression_failure_id(scenario_id, w[:20])

                    failures.append(RegressionFailure(
                        failure_id=fail_id,
                        scenario_id=scenario_id,
                        regression_type=tbl_name,
                        severity=sev,
                        title=f"{sev.replace('_', ' ').title()}",
                        description=w,
                        recommended_action="Review offline execution constraints and update configurations.",
                        blocking=blocking,
                        warnings=[]
                    ))

    return failures

def regression_failures_to_dataframe(failures: list[RegressionFailure]) -> pd.DataFrame:
    if not failures:
        return pd.DataFrame()
    return pd.DataFrame([regression_failure_to_dict(f) for f in failures])

def summarize_regression_failures(failure_df: pd.DataFrame) -> dict:
    if failure_df.empty:
        return {"total_failures": 0, "blocking_count": 0}
    return {
        "total_failures": len(failure_df),
        "blocking_count": len(failure_df[failure_df["blocking"]]),
        "by_severity": failure_df["severity"].value_counts().to_dict() if "severity" in failure_df else {},
    }
