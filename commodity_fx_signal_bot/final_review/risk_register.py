import pandas as pd
from typing import Dict, List, Optional
from final_review.final_review_models import FinalRisk, build_final_risk_id

def classify_risk_severity(row: pd.Series) -> str:
    if row.get("critical", False):
        return "critical_risk"
    return "low_risk"

def build_risks_from_audit_results(audit_tables: Dict[str, pd.DataFrame], summaries: Optional[dict] = None) -> List[FinalRisk]:
    risks = []

    if "safety" in audit_tables and not audit_tables["safety"].empty:
        df = audit_tables["safety"]
        for _, row in df.iterrows():
            if row.get("critical", False):
                risks.append(FinalRisk(
                    risk_id=build_final_risk_id("safety", "safety_violation"),
                    severity="critical_risk",
                    category="safety",
                    title="Safety Violation Found",
                    description=f"Pattern '{row.get('pattern_found')}' found in {row.get('file')}",
                    affected_modules=[str(row.get('file'))],
                    recommended_action="Remove forbidden live trading, broker, deploy, or advice terminology.",
                    blocking=True,
                    warnings=[]
                ))

    return risks

def risks_to_dataframe(risks: List[FinalRisk]) -> pd.DataFrame:
    if not risks:
        return pd.DataFrame(columns=[
            "risk_id", "severity", "category", "title", "description",
            "affected_modules", "recommended_action", "blocking", "warnings"
        ])

    return pd.DataFrame([r.__dict__ for r in risks])

def summarize_final_risks(risk_df: pd.DataFrame) -> dict:
    if risk_df.empty:
        return {"total_risks": 0, "blocking_risks": 0, "critical_risks": 0, "passed": True}

    return {
        "total_risks": len(risk_df),
        "blocking_risks": len(risk_df[risk_df["blocking"] == True]),
        "critical_risks": len(risk_df[risk_df["severity"] == "critical_risk"]),
        "passed": len(risk_df[risk_df["blocking"] == True]) == 0
    }
