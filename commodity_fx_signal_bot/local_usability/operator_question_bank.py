import pandas as pd
from .usability_config import LocalUsabilityProfile

def build_default_operator_questions(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"question": "İlk hangi komutu çalıştırmalıyım?"}])

def build_operator_question_bank(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_operator_questions(profile)
    return df, {"total": len(df)}

def summarize_operator_question_bank(question_df: pd.DataFrame) -> dict:
    return {"total": len(question_df)}
