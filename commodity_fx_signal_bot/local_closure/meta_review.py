
from pathlib import Path
from local_closure.closure_config import LocalClosureProfile

def build_meta_review_sections(project_root: Path, profile: LocalClosureProfile) -> list[dict]:
    return [
        {"title": "Proje Amacı", "content": "Offline Emtia-Döviz sinyal platformunun 1-79 fazlık yolculuğu."},
        {"title": "Faz Aileleri Özeti", "content": "Veri gölü, ML, raporlama, denetim, güvenlik ve teslimat fazları tamamlandı."},
        {"title": "Mimari Evrim", "content": "Monolitik scriptlerden event-driven, modüler bir feature-store mimarisine geçiş."},
        {"title": "Safety/Non-use Evrimi", "content": "Sıkı no-go kuralları, dry-run standartları eklendi."},
        {"title": "DataLake/Reporting Evrimi", "content": "Bağımsız depolama ve raporlama katmanları oturtuldu."},
        {"title": "Evidence/Metadata/Graph/Timeline Evrimi", "content": "Her adımın kanıtlanabilir olması sağlandı."},
        {"title": "Readiness/Maintenance/Archive/DR Evrimi", "content": "Sürdürülebilirlik katmanları oluşturuldu."},
        {"title": "Training/Briefing/Synthesis/Hardening/Acceptance/Delivery/Archival Evrimi", "content": "Teslimat ve kabul provaları yapıldı."},
        {"title": "Güçlü Yönler", "content": "Modüler, test edilebilir, şeffaf."},
        {"title": "Bilinçli Sınırlamalar", "content": "Canlı trade yok, yatırım tavsiyesi yok."},
        {"title": "Teknik Borç Adayları", "content": "Test coverage artırılabilir, bellek optimizasyonu yapılabilir."},
        {"title": "Manuel Review Alanları", "content": "Gelecek faz geçişleri öncesi inceleme gereklidir."},
        {"title": "Gelecek Yol Haritası İçin Gözlemler", "content": "Offline araştırma yetenekleri genişletilebilir."}
    ]

def build_final_project_meta_review_report(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    sections = build_meta_review_sections(project_root, profile)
    text = "# Final Project Meta-Review Report\n\n"
    text += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    summary = summarize_meta_review_report(text)
    return text, summary

def summarize_meta_review_report(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("## "),
        "has_warning": "UYARI" in text
    }
