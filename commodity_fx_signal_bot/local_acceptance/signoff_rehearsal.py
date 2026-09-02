import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_signoff_rehearsal_checklist(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        {"item": "Bu resmi sign-off değildir", "status": "checked"},
        {"item": "Production release değildir", "status": "checked"},
        {"item": "Compliance sertifikası değildir", "status": "checked"},
        {"item": "Yatırım tavsiyesi değildir", "status": "checked"},
        {"item": "Canlı emir/broker/deploy yoktur", "status": "checked"},
        {"item": "Manual review şartları listelendi", "status": "checked"},
        {"item": "No-go koşulları listelendi", "status": "checked"},
        {"item": "Safe-go koşulları sadece local/offline kullanım içindir", "status": "checked"}
    ]
    df = pd.DataFrame(items)
    return df, {"total_items": len(df)}

def build_signoff_rehearsal_sections(checklist_df: pd.DataFrame, no_go_df: pd.DataFrame, safe_go_df: pd.DataFrame) -> list[dict]:
    return [
        {"title": "Sign-off Rehearsal", "content": "Bu doküman sadece provadır, resmi imza üretmez."},
        {"title": "Checklist", "content": f"{len(checklist_df)} items checked."},
        {"title": "No-go conditions", "content": f"{len(no_go_df)} no-go items."},
        {"title": "Safe-go conditions", "content": f"{len(safe_go_df)} safe-go items."}
    ]

def build_signoff_rehearsal_binder(checklist_df: pd.DataFrame, no_go_df: pd.DataFrame, safe_go_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[str, dict]:
    sections = build_signoff_rehearsal_sections(checklist_df, no_go_df, safe_go_df)
    lines = ["# Sign-off Rehearsal Binder\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_signoff_rehearsal_binder(text)

def summarize_signoff_rehearsal_binder(text: str) -> dict:
    return {"length": len(text)}
