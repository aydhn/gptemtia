import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def build_non_use_policy_examples(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "Trading", "policy": "No live trading"},
        {"scenario": "Deployment", "policy": "No deployment"}
    ])

def build_safe_vs_unsafe_prompt_examples(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"type": "Güvenli", "prompt": "raporu özetle"},
        {"type": "Güvenli", "prompt": "status çıktısını yorumla"},
        {"type": "Güvenli", "prompt": "gaps listesi çıkar"},
        {"type": "Güvensiz", "prompt": "şimdi al/sat"},
        {"type": "Güvensiz", "prompt": "broker ile emir gönder"},
        {"type": "Güvensiz", "prompt": "canlı trade aç"},
        {"type": "Güvensiz", "prompt": "API key bas"},
        {"type": "Güvenli düzeltme", "prompt": "bunu yatırım tavsiyesi olmadan risk/sınırlılık formatında açıkla"}
    ])

def build_non_use_policy_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    df = build_safe_vs_unsafe_prompt_examples(profile)
    text = "### Prompts\n" + df.to_string()
    text += "\n\n> UYARI: Safe/unsafe örnekleri yatırım tavsiyesi üretmemeli. Canlı işlem yönlendirmesi yok. Eğitim materyali policy explanation’dır."
    return text, summarize_non_use_policy_training(text)

def summarize_non_use_policy_training(text: str) -> dict:
    return {"length": len(text)}
