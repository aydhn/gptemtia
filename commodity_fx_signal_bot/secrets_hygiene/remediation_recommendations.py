
import pandas as pd
from typing import Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import SecretRemediationRecommendation, build_secret_recommendation_id

def map_finding_to_safe_recommendation(row: pd.Series) -> SecretRemediationRecommendation:
    f_type = str(row.get("finding_type", "unknown"))
    sev = str(row.get("severity", "unknown"))
    rel_path = str(row.get("relative_path", "unknown"))
    action = "Review manually to confirm if it is a real secret."
    if "api" in f_type or "broker" in f_type: action = "Move to .env and use a placeholder in the code or .env.example. If it is real and committed, rotate it at the provider."
    elif "private" in f_type: action = "Ensure private keys are ignored by .gitignore and never committed."
    return SecretRemediationRecommendation(
        recommendation_id=build_secret_recommendation_id(f"Rec for {f_type}"), finding_id=str(row.get("finding_id", "")),
        title=f"Review {sev} in {rel_path}", description=f"Found a potential {f_type} pattern.",
        safe_action=action, destructive=False, requires_manual_review=True, warnings=[]
    )

def build_secret_remediation_recommendations(findings_df: pd.DataFrame, boundary_df: Optional[pd.DataFrame] = None, profile: Optional[SecretsHygieneProfile] = None) -> list[SecretRemediationRecommendation]:
    recs = []
    if findings_df is not None and not findings_df.empty:
        high_crit = findings_df[findings_df["severity"].isin(["high_secret_risk", "critical_secret_risk"])]
        for _, row in high_crit.iterrows(): recs.append(map_finding_to_safe_recommendation(row))
    if boundary_df is not None and not boundary_df.empty:
        failed = boundary_df[boundary_df["status"] == "boundary_failed"]
        for _, row in failed.iterrows():
            b_name = row.get("boundary_name", "unknown")
            recs.append(SecretRemediationRecommendation(
                recommendation_id=build_secret_recommendation_id(f"Rec for boundary {b_name}"), finding_id=None,
                title=f"Fix boundary violation: {b_name}", description="A credential boundary was violated.",
                safe_action="Remove credentials from the restricted path and update git history if necessary.",
                destructive=False, requires_manual_review=True, warnings=[]
            ))
    return recs

def recommendations_to_dataframe(recommendations: list[SecretRemediationRecommendation]) -> pd.DataFrame:
    if not recommendations: return pd.DataFrame()
    return pd.DataFrame([r.__dict__ for r in recommendations])

def summarize_secret_recommendations(recommendations_df: pd.DataFrame) -> dict:
    if recommendations_df is None or recommendations_df.empty: return {"total_recommendations": 0, "destructive_count": 0}
    return {"total_recommendations": len(recommendations_df), "destructive_count": len(recommendations_df[recommendations_df["destructive"]])}
