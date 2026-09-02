import pandas as pd
from .training_config import LocalTrainingProfile

def build_default_glossary_terms(profile: LocalTrainingProfile) -> pd.DataFrame:
    terms = ["dry-run", "offline/local", "non-use policy", "DataLake", "FeatureStore", "evidence governance", "artifact metadata", "model card", "dataset card", "experiment card", "local knowledge graph", "timeline", "consistency", "readiness", "maintenance", "archive", "disaster-recovery tabletop", "restore drill simulation", "resilience score", "manual review", "no-go/safe-go"]
    data = [{"term": t, "definition": f"Definition of {t}", "warnings": "Finansal tavsiye sözlüğü değildir. Sınır açıklaması içerir."} for t in terms]
    return pd.DataFrame(data)

def build_glossary_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_glossary_terms(profile)
    return df, summarize_glossary(df)

def summarize_glossary(glossary_df: pd.DataFrame) -> dict:
    if glossary_df is None or glossary_df.empty: return {"count": 0}
    return {"count": len(glossary_df)}
