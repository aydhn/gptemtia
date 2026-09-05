import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_immutable_readme_sections(profile: LocalPostCompletionPreservationProfile) -> list[dict]:
    return [
        {"title": "Bu README ne anlatir?", "content": "Immutable README rehearsal."},
        {"title": "Bu README ne degildir?", "content": "Gercek immutable lock degildir."},
        {"title": "Offline/local kullanim siniri", "content": "Offline only."},
        {"title": "Komutlarin calisma mantigi", "content": "Rehearsal mode."},
        {"title": "Canli trading/broker/deploy/advice yasaklari", "content": "Yasak."},
        {"title": "Archive seal rehearsal aciklamasi", "content": "Rehearsal."},
        {"title": "Evidence vault index aciklamasi", "content": "Rehearsal."},
        {"title": "Knowledge capsule aciklamasi", "content": "Rehearsal."},
        {"title": "Preservation binder aciklamasi", "content": "Rehearsal."},
        {"title": "Manual review zorunlulugu", "content": "Zorunlu."},
        {"title": "Final safety statement", "content": "Safe."}
    ]

def build_immutable_readme_rehearsal_document(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    sections = build_immutable_readme_sections(profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_immutable_readme(text)

def summarize_immutable_readme(text: str) -> dict:
    return {"length": len(text)}
