from pathlib import Path
from .training_config import LocalTrainingProfile

def build_developer_training_sections(project_root: Path, profile: LocalTrainingProfile) -> list[dict]:
    return [
        {"title": "Repo yapısı", "content": "Ana klasörler ve amaçları."},
        {"title": "Config/settings/paths", "content": "Ayar dosyalarının yönetimi."},
        {"title": "DataLake save/load convention", "content": "Veri okuma yazma kuralları."},
        {"title": "FeatureStore load convention", "content": "ML özellikleri kuralları."},
        {"title": "Scripts contract", "content": "Betiklerin çalışma yapısı."},
        {"title": "Tests contract", "content": "Test standartları."},
        {"title": "Report builder convention", "content": "Rapor oluşturma kuralları."},
        {"title": "Safety boundary pattern", "content": "Güvenlik sınırları ve exceptionlar."},
        {"title": "New phase implementation checklist", "content": "Yeni faz ekleme adımları."},
        {"title": "Common anti-patterns", "content": "Yapılmaması gerekenler."}
    ]

def build_developer_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    sections = build_developer_training_sections(project_root, profile)
    text = "\n\n".join([f"### {s['title']}\n{s['content']}" for s in sections])
    text += "\n\n> UYARI: Developer pack deployment instruction değildir. Auto-fix veya destructive command yok. External LLM/API kullanımını teşvik etmez."
    return text, summarize_developer_training_pack(text)

def summarize_developer_training_pack(text: str) -> dict:
    return {"length": len(text), "sections": text.count("### ")}
