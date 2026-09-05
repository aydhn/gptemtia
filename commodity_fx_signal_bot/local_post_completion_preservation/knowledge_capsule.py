import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_knowledge_capsule_sections(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> list[dict]:
    return [
        {"title": "Proje nedir?", "content": "Knowledge Capsule."},
        {"title": "Proje ne degildir?", "content": "Official knowledge freeze degildir."},
        {"title": "Ana modul aileleri", "content": "Modules"},
        {"title": "Ana script aileleri", "content": "Scripts"},
        {"title": "Ana rapor aileleri", "content": "Reports"},
        {"title": "DataLake aileleri", "content": "DataLake"},
        {"title": "Guvenlik sinirlari", "content": "Boundaries"},
        {"title": "Governance/redteam/incident/release/longterm/completion ozeti", "content": "Summary"},
        {"title": "Nasil baslanir?", "content": "Quickstart"},
        {"title": "Hangi komutlar yalnizca rapor uretir?", "content": "Read-only"},
        {"title": "Hangi seyler kesinlikle yapilmaz?", "content": "No-go"},
        {"title": "Sonraki bakim okuma sirasi", "content": "Order"}
    ]

def build_final_knowledge_capsule(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    sections = build_knowledge_capsule_sections(project_root, profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_final_knowledge_capsule(text)

def build_knowledge_capsule_index(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "capsule"}])
    return df, summarize_knowledge_capsule_index(df)

def summarize_final_knowledge_capsule(text: str) -> dict:
    return {"length": len(text)}

def summarize_knowledge_capsule_index(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
