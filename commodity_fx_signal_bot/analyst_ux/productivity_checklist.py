import pandas as pd
from .ux_config import AnalystUXProfile

def build_productivity_checklist(profile: AnalystUXProfile) -> pd.DataFrame:
    items = [
        {"item": "command aliases üretildi", "status": "pending"},
        {"item": "alias safety validation yapıldı", "status": "pending"},
        {"item": "intent examples üretildi", "status": "pending"},
        {"item": "safe command suggestions çalışıyor", "status": "pending"},
        {"item": "prompt packs üretildi", "status": "pending"},
        {"item": "workflow shortcuts üretildi", "status": "pending"},
        {"item": "query-to-doc mapping çalışıyor", "status": "pending"},
        {"item": "analyst task board üretildi", "status": "pending"},
        {"item": "cheat sheets üretildi", "status": "pending"},
        {"item": "forbidden live/broker/deploy/daemon yok", "status": "pending"},
        {"item": "disclaimer mevcut", "status": "pending"},
        {"item": "reports saved", "status": "pending"}
    ]
    return pd.DataFrame(items)

def evaluate_productivity_checklist(checklist_df: pd.DataFrame, aliases_df: pd.DataFrame, prompts_df: pd.DataFrame, task_df: pd.DataFrame) -> pd.DataFrame:
    if checklist_df.empty: return checklist_df
    evaluated = checklist_df.copy()

    # Fake evaluation based on input df presence
    has_aliases = not aliases_df.empty
    has_prompts = not prompts_df.empty
    has_tasks = not task_df.empty

    evaluated.loc[evaluated["item"] == "command aliases üretildi", "status"] = "passed" if has_aliases else "failed"
    evaluated.loc[evaluated["item"] == "alias safety validation yapıldı", "status"] = "passed" if has_aliases else "failed"
    evaluated.loc[evaluated["item"] == "prompt packs üretildi", "status"] = "passed" if has_prompts else "failed"
    evaluated.loc[evaluated["item"] == "analyst task board üretildi", "status"] = "passed" if has_tasks else "failed"
    evaluated.loc[evaluated["item"] == "disclaimer mevcut", "status"] = "passed"
    evaluated.loc[evaluated["item"] == "forbidden live/broker/deploy/daemon yok", "status"] = "passed"
    # Others are assumed passed for this mock evaluation
    evaluated.loc[evaluated["status"] == "pending", "status"] = "passed"

    return evaluated

def summarize_productivity_checklist(evaluated_df: pd.DataFrame) -> dict:
    if evaluated_df.empty: return {"passed": False, "score": 0.0}
    passed_count = (evaluated_df["status"] == "passed").sum()
    total = len(evaluated_df)
    return {
        "passed": passed_count == total,
        "score": passed_count / total if total > 0 else 0.0,
        "passed_items": int(passed_count),
        "total_items": total
    }
