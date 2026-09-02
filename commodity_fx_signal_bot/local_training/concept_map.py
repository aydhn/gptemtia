import pandas as pd
from .training_config import LocalTrainingProfile

def build_concept_relationships(profile: LocalTrainingProfile) -> pd.DataFrame:
    rels = [
        ("reports", "DataLake"), ("DataLake", "FeatureStore"), ("evidence", "controls"),
        ("metadata", "artifacts"), ("graph", "relationships"), ("timeline", "events"),
        ("consistency", "coherence"), ("readiness", "handoff"), ("maintenance", "sustainability"),
        ("archive", "preservation"), ("DR", "rehearsal"), ("training", "handover education")
    ]
    data = [{"source": r[0], "target": r[1], "warnings": "Concept map external graph DB değildir. Kesin nedensellik iddiası yok. Eğitim amaçlı local map’tir."} for r in rels]
    return pd.DataFrame(data)

def build_concept_map_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_concept_relationships(profile)
    return df, summarize_concept_map(df)

def summarize_concept_map(concept_df: pd.DataFrame) -> dict:
    if concept_df is None or concept_df.empty: return {"count": 0}
    return {"count": len(concept_df)}
