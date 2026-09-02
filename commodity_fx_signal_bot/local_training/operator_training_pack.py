from pathlib import Path
from .training_config import LocalTrainingProfile

def build_operator_training_sections(project_root: Path, profile: LocalTrainingProfile) -> list[dict]:
    return [
        {"title": "Projenin amacı", "content": "Offline araştırma ve analiz."},
        {"title": "Ne yapar/ne yapmaz?", "content": "Sinyal üretir ama canlı trade yapmaz."},
        {"title": "Güvenli ilk kullanım", "content": "Sadece okuma ve analiz yapın."},
        {"title": "Status komutlarını okuma", "content": "Status komutları raporları gösterir."},
        {"title": "Rapor klasörlerini okuma", "content": "reports/ altındaki verileri inceleyin."},
        {"title": "DataLake outputs", "content": "DataLake lake içindeki verilerdir."},
        {"title": "Final review/quality gates", "content": "Quality checks pass edilmelidir."},
        {"title": "Known gaps/manual review", "content": "Manuel inceleme gerektirir."},
        {"title": "Local DR, archive, maintenance outputs", "content": "Local recovery raporlarıdır."},
        {"title": "Yasaklar", "content": "Canlı emir, deployment, broker kullanımı yasaktır."}
    ]

def build_operator_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    sections = build_operator_training_sections(project_root, profile)
    text = "\n\n".join([f"### {s['title']}\n{s['content']}" for s in sections])
    text += "\n\n> UYARI: Eğitim pack canlı işlem yetkisi vermez. Safe commands çalıştırılmaz. Yatırım tavsiyesi yok."
    return text, summarize_operator_training_pack(text)

def summarize_operator_training_pack(text: str) -> dict:
    return {"length": len(text), "sections": text.count("### ")}
