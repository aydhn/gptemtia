import pandas as pd
from .training_config import LocalTrainingProfile

def build_assessment_questions(profile: LocalTrainingProfile) -> pd.DataFrame:
    qs = ["dry-run nedir?", "Bu sistem canlı emir gönderir mi?", "Rapor yatırım tavsiyesi midir?", "Hangi komutlar güvenlidir?", "Raw secret görürsen ne yaparsın?", "Readiness score ne değildir?", "Restore drill simulation ne değildir?", "DataLake outputs nasıl okunur?", "Missing report durumunda ne yapılır?"]
    return pd.DataFrame([{"question": q} for q in qs])

def build_assessment_answer_key(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([{"question": "dry-run nedir?", "answer": "offline test"}])

def evaluate_assessment_safety(question_df: pd.DataFrame, answer_df: pd.DataFrame, profile: LocalTrainingProfile) -> dict:
    return {"is_safe": True}

def build_training_assessment_dry_run(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_assessment_questions(profile)
    return df, summarize_training_assessment(df)

def summarize_training_assessment(assessment_df: pd.DataFrame) -> dict:
    if assessment_df is None or assessment_df.empty: return {"count": 0}
    return {"count": len(assessment_df)}
