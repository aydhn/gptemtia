import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_do_dont_examples(profile: LocalBriefingProfile) -> pd.DataFrame:
    examples = [
        ("DO", "offline/local dry-run"),
        ("DO", "karar baglami"),
        ("DO", "manuel review"),
        ("DO", "sinirliliklar"),
        ("DO", "guvenli kullanim sinirlari"),
        ("DONT", "kesin al"),
        ("DONT", "kesin sat"),
        ("DONT", "canli trade hazir"),
        ("DONT", "broker baglandi"),
        ("DONT", "uretime cikti"),
        ("DONT", "resmi onaylandi"),
        ("DONT", "garanti getiri")
    ]
    return pd.DataFrame(examples, columns=["type", "phrase"])

def build_communication_do_dont_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_do_dont_examples(profile)
    return df, summarize_communication_do_dont(df)

def summarize_communication_do_dont(df: pd.DataFrame) -> dict:
    if df is None or df.empty:
        return {"total_do_dont": 0}
    return {"total_do_dont": len(df)}
