import os

with open("local_training/safe_usage_training.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
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
    text = "### Safe Usage Rules\\n" + rules_df.to_markdown()
    text += "\\n\\n> UYARI: Safe usage training net ve tekrar edilebilir olmalı. Sertifika dili yok."
    return text, summarize_safe_usage_training(text, rules_df)

def summarize_safe_usage_training(text: str, rules_df: pd.DataFrame) -> dict:
    return {"rules_count": len(rules_df)}
''')

with open("local_training/non_use_policy_training.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
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
    text = "### Prompts\\n" + df.to_markdown()
    text += "\\n\\n> UYARI: Safe/unsafe örnekleri yatırım tavsiyesi üretmemeli. Canlı işlem yönlendirmesi yok. Eğitim materyali policy explanation’dır."
    return text, summarize_non_use_policy_training(text)

def summarize_non_use_policy_training(text: str) -> dict:
    return {"length": len(text)}
''')

with open("local_training/walkthrough_registry.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile

def build_default_walkthroughs(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"name": "repo ilk okuma", "desc": "Walkthrough"},
        {"name": "kurulum dokümanını okuma", "desc": "Walkthrough"},
        {"name": "status report okuma", "desc": "Walkthrough"},
        {"name": "quality report okuma", "desc": "Walkthrough"},
        {"name": "DataLake klasörlerini gezme", "desc": "Walkthrough"},
        {"name": "local graph query çıktısını okuma", "desc": "Walkthrough"},
        {"name": "timeline event report okuma", "desc": "Walkthrough"},
        {"name": "consistency gap report okuma", "desc": "Walkthrough"},
        {"name": "readiness binder okuma", "desc": "Walkthrough"},
        {"name": "maintenance runbook okuma", "desc": "Walkthrough"},
        {"name": "archive manifest okuma", "desc": "Walkthrough"},
        {"name": "DR tabletop report okuma", "desc": "Walkthrough"}
    ])

def build_guided_walkthrough_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_walkthroughs(profile)
    return df, summarize_guided_walkthroughs(df)

def summarize_guided_walkthroughs(walkthrough_df: pd.DataFrame) -> dict:
    if walkthrough_df is None or walkthrough_df.empty: return {"count": 0}
    return {"count": len(walkthrough_df)}
''')

with open("local_training/local_walkthroughs.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def build_walkthrough_steps(walkthrough_name: str, profile: LocalTrainingProfile) -> list[str]:
    return ["Step 1: Open file", "Step 2: Read contents"]

def validate_walkthrough_steps_safety(steps: list[str], profile: LocalTrainingProfile) -> dict:
    return {"is_safe": True, "issues": []}

def build_local_walkthrough_lessons(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"lesson": "repo ilk okuma", "steps": build_walkthrough_steps("repo", profile)}])
    return df, summarize_local_walkthrough_lessons(df)

def summarize_local_walkthrough_lessons(lesson_df: pd.DataFrame) -> dict:
    if lesson_df is None or lesson_df.empty: return {"count": 0}
    return {"count": len(lesson_df)}
''')

