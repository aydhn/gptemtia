import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def classify_incident_risk(row: pd.Series, profile: LocalIncidentResponseProfile) -> str:
    return "incident_info"

def build_incident_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [{"risk_area": "mock_area", "risk_level": "incident_info"}]
    df = pd.DataFrame(data)
    summary = summarize_incident_risks(df)
    return df, summary

def build_incident_risk_digest(risk_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[str, Dict]:
    text = "Risk Digest: Mock digest.\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
    summary = summarize_incident_risks(risk_df)
    return text, summary

def summarize_incident_risks(risk_df: pd.DataFrame) -> Dict:
    return {
        "count": len(risk_df),
        "note": "Not an investment risk."
    }
