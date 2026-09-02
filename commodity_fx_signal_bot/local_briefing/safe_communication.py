import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_safe_communication_rules(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    rules = [
        ("KULLANILACAK", "offline arastirma platformu"),
        ("KULLANILACAK", "yatirim tavsiyesi degildir"),
        ("KULLANILACAK", "canli emir gondermez"),
        ("KULLANILACAK", "manual review gerekir"),
        ("KULLANILACAK", "production release degildir"),
        ("KULLANILACAK", "resmi compliance degildir"),
        ("KULLANILMAYACAK", "garanti getiri"),
        ("KULLANILMAYACAK", "canli trading hazir"),
        ("KULLANILMAYACAK", "broker execution ready")
    ]
    df = pd.DataFrame(rules, columns=["rule_type", "phrase"])
    return df, {"total_rules": len(df)}

def build_safe_communication_guide(profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_safe_communication_rules(profile)
    text = "# Safe Communication Guide\n\n"
    for _, row in df.iterrows():
        text += f"- **{row['rule_type']}**: {row['phrase']}\n"
    return text, summary

def summarize_safe_communication_guide(text: str, rules_df: pd.DataFrame) -> dict:
    if rules_df is None or rules_df.empty:
        return {"total_rules": 0}
    return {"total_rules": len(rules_df)}
