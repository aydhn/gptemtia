from pathlib import Path
from .usability_config import LocalUsabilityProfile

def build_usability_review_sections(project_root: Path, profile: LocalUsabilityProfile) -> list[dict]:
    return [
        {"title": "Amaç ve Kapsam", "content": "Bu rapor offline/local usability review ve operator ergonomics rehearsal çıktısıdır; gerçek kullanıcı testi, telemetry, production usability approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "Operatörün İlk Karşılaşacağı Yapı", "content": "Sistem architecture docs üzerinden incelenmelidir."},
        {"title": "Komut Keşfi", "content": "Tüm komutlar scripts/ altındadır."},
        {"title": "Doküman Keşfi", "content": "Dokümanlar docs/ altındadır."},
        {"title": "Çıktı Okuma Akışı", "content": "Raporlar reports/output/ altından okunur."},
        {"title": "Manuel Review Noktaları", "content": "Usability kalite kontrolleri."},
        {"title": "En Çok Kafa Karıştırabilecek Alanlar", "content": "Çok fazla script ve doküman bulunması."},
        {"title": "İlk Saat / İlk Gün / Haftalık Kullanım", "content": "Operator paths incelenmelidir."},
        {"title": "Ne Çalıştırılmalı?", "content": "Status scriptleri."},
        {"title": "Ne Çalıştırılmamalı?", "content": "Yıkıcı ve canlı komutlar."},
        {"title": "Sınırlar ve Uyarılar", "content": "Gerçek kullanıcı testi ve yatırım tavsiyesi değildir."}
    ]

def build_final_local_usability_review(project_root: Path, profile: LocalUsabilityProfile) -> tuple[str, dict]:
    sections = build_usability_review_sections(project_root, profile)
    text = "\n\n".join(f"## {s['title']}\n{s['content']}" for s in sections)
    return text, {"section_count": len(sections)}

def summarize_usability_review(text: str) -> dict:
    return {"length": len(text)}

def save_usability_review(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
