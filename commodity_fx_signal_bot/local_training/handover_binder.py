import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def build_handover_binder_sections(domain_df, path_df, lesson_df, faq_df):
    return [
        {"title": "Amaç ve kapsam", "content": "Offline project handover"},
        {"title": "Kime yönelik?", "content": "Operators and analysts"},
        {"title": "Sistem ne yapar/ne yapmaz?", "content": "Sinyal üretir, canlı trade yapmaz"},
        {"title": "Role-based onboarding", "content": "Paths included"},
        {"title": "İlk hafta curriculum", "content": "Curriculum included"},
        {"title": "Safe commands", "content": "Only safe commands allowed"},
        {"title": "Rapor okuma", "content": "Reports logic"},
        {"title": "DataLake okuma", "content": "Lake structure"},
        {"title": "Cross-layer outputs", "content": "Cross-layer connections"},
        {"title": "Troubleshooting", "content": "Common issues"},
        {"title": "Glossary/FAQ", "content": "Definitions"},
        {"title": "Knowledge transfer checklist", "content": "Checklist items"},
        {"title": "Yasaklar", "content": "Live/broker bans"}
    ]

def build_handover_education_binder(domain_df, path_df, lesson_df, faq_df, profile):
    sections = build_handover_binder_sections(domain_df, path_df, lesson_df, faq_df)
    text = "\n\n".join([f"### {s['title']}\n{s['content']}" for s in sections])
    text += "\n\n> UYARI: Binder official certification değildir. Binder canlı operasyon yetkisi vermez. Raw secret yok."
    return text, summarize_handover_binder(text)

def save_handover_education_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_handover_binder(binder_text: str) -> dict:
    return {"length": len(binder_text), "sections": binder_text.count("### ")}
