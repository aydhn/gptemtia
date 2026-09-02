import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def build_safe_usage_rules(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"rule": "Sadece read-only komutlar çalıştır", "level": "mandatory"},
        {"rule": "Canlı emir kesinlikle yasaktır", "level": "critical"}
    ])

def build_forbidden_action_training(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"action": "canlı emir", "reason": "Sistem offline"},
        {"action": "broker API", "reason": "Desteklenmiyor"},
        {"action": "gerçek pozisyon", "reason": "Desteklenmiyor"},
        {"action": "yatırım tavsiyesi", "reason": "Yasak"},
        {"action": "model deployment", "reason": "Yasak"},
        {"action": "production scheduler", "reason": "Yasak"},
        {"action": "background daemon", "reason": "Yasak"},
        {"action": "cloud upload", "reason": "Yasak"},
        {"action": "external LLM/API", "reason": "Yasak"},
        {"action": "scraping", "reason": "Yasak"},
        {"action": "file delete/move/overwrite", "reason": "Yasak"},
        {"action": "auto restore/backup/recovery", "reason": "Yasak"}
    ])

def build_safe_usage_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    rules_df = build_safe_usage_rules(profile)
    text = "### Safe Usage Rules\n" + rules_df.to_string()
    text += "\n\n> UYARI: Safe usage training net ve tekrar edilebilir olmalı. Sertifika dili yok."
    return text, summarize_safe_usage_training(text, rules_df)

def summarize_safe_usage_training(text: str, rules_df: pd.DataFrame) -> dict:
    return {"rules_count": len(rules_df)}
