from pathlib import Path
from .training_config import LocalTrainingProfile

def build_analyst_training_sections(project_root: Path, profile: LocalTrainingProfile) -> list[dict]:
    return [
        {"title": "Araştırma raporlarını okuma", "content": "Raporlar analiz için üretilmiştir."},
        {"title": "Synthetic/demo/test verinin sınırları", "content": "Veriler sentetik olabilir."},
        {"title": "Backtest/paper outputlarını yorumlama sınırları", "content": "Geçmiş performans geleceği garanti etmez."},
        {"title": "Evidence ve metadata cards", "content": "Modeller hakkında bilgi verir."},
        {"title": "Scenario/regression reports", "content": "Test raporlarıdır."},
        {"title": "Graph/timeline/consistency outputs", "content": "Bağımlılık ve olay geçmişidir."},
        {"title": "“Yatırım tavsiyesi değildir” çerçevesi", "content": "Hiçbir rapor yatırım tavsiyesi değildir."},
        {"title": "Manual review notları", "content": "Analist incelemesi gerekir."}
    ]

def build_analyst_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    sections = build_analyst_training_sections(project_root, profile)
    text = "\n\n".join([f"### {s['title']}\n{s['content']}" for s in sections])
    text += "\n\n> UYARI: Analist eğitimi yatırım danışmanlığı değildir. Kesin AL/SAT yorumlama yok. Canlı sinyal yok."
    return text, summarize_analyst_training_pack(text)

def summarize_analyst_training_pack(text: str) -> dict:
    return {"length": len(text), "sections": text.count("### ")}
