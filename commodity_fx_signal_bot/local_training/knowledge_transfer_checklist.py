import pandas as pd
from .training_config import LocalTrainingProfile

def build_role_specific_transfer_checklist(role_label: str, profile: LocalTrainingProfile) -> pd.DataFrame:
    items = [
        "README okundu", "SAFE_USAGE_GUIDE okundu", "OPERATOR_MANUAL okundu", "Non-use policy anlaşıldı",
        "Safe commands listesi okundu", "Forbidden actions listesi okundu", "Rapor klasörleri gezildi",
        "DataLake klasörleri gezildi", "Quality/status raporları incelendi", "Manual review queue incelendi",
        "DR/Archive/Maintenance sınırları anlaşıldı"
    ]
    return pd.DataFrame([{"role": role_label, "item": i, "status": "pending"} for i in items])

def build_knowledge_transfer_checklist(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_role_specific_transfer_checklist("operator_role", profile)
    return df, summarize_knowledge_transfer_checklist(df)

def summarize_knowledge_transfer_checklist(checklist_df: pd.DataFrame) -> dict:
    if checklist_df is None or checklist_df.empty: return {"count": 0}
    return {"count": len(checklist_df)}
