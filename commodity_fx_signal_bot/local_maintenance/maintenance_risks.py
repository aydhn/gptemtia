import pandas as pd
from typing import Tuple, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def classify_maintenance_risk(row: pd.Series, profile: LocalMaintenanceProfile) -> str:
    # A simple classifier based on gap type or queue source
    source = row.get("source", row.get("gap_type", "unknown"))

    if source in ["missing_cadence", "dependency_aging"]:
        return "sustainability_medium_risk"
    elif source in ["stale_docs", "stale_reports", "stale_tests"]:
        return "sustainability_low_risk"
    elif source == "missing_operator_review_items":
        return "sustainability_high_risk"

    return "sustainability_unknown_risk"

def build_maintenance_risk_summary(
    gap_df: pd.DataFrame,
    queue_df: pd.DataFrame,
    dep_df: pd.DataFrame,
    profile: LocalMaintenanceProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:

    risks = []

    if gap_df is not None and not gap_df.empty:
        for _, row in gap_df.iterrows():
            risks.append({
                "source": row.get("gap_type"),
                "description": row.get("description")
            })

    if queue_df is not None and not queue_df.empty:
        for _, row in queue_df.iterrows():
            risks.append({
                "source": row.get("source"),
                "description": row.get("reason")
            })

    df = pd.DataFrame(risks)
    if not df.empty:
        df["risk_level"] = df.apply(classify_maintenance_risk, profile=profile, axis=1)

    summary = summarize_maintenance_risks(df)
    return df, summary

def build_maintenance_risk_digest(risk_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Tuple[str, Dict[str, Any]]:
    if risk_df is None or risk_df.empty:
        return "No maintenance risks detected.", {"total_risks": 0}

    lines = ["# Maintenance Risk Digest\n"]
    for risk_level, group in risk_df.groupby("risk_level"):
        lines.append(f"## {risk_level}")
        for _, row in group.iterrows():
            lines.append(f"- [{row['source']}] {row['description']}")
        lines.append("")

    lines.append("\n*Disclaimer: Maintenance risk is not investment risk. Critical risk is not a live alarm. Actions must be manual/offline.*")

    return "\n".join(lines), summarize_maintenance_risks(risk_df)

def summarize_maintenance_risks(risk_df: pd.DataFrame) -> Dict[str, Any]:
    if risk_df is None or risk_df.empty:
        return {"total_risks": 0}

    return {
        "total_risks": len(risk_df),
        "risks_by_level": risk_df["risk_level"].value_counts().to_dict() if "risk_level" in risk_df else {},
        "disclaimer": "Maintenance risk is not investment risk."
    }
