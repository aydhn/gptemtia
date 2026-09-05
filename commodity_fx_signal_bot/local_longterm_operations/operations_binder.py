"""Operations binder."""
from pathlib import Path
from .longterm_config import LocalLongTermOperationsProfile

def build_longterm_operations_binder_sections(project_root: Path, profile: LocalLongTermOperationsProfile) -> list[dict]:
    return [
        {"title": "Amaç ve Kapsam", "content": "Offline/local long-term operations binder provası."},
        {"title": "Bu binder ne değildir?", "content": "Gerçek production operations plan değildir. Official lifecycle policy değildir. Roadmap commitment değildir. Yatırım tavsiyesi yoktur."},
        {"title": "Long-term operations overview", "content": "Sistem lokal olarak bakım altındadır."},
        {"title": "Yearly/quarterly/monthly/weekly review overview", "content": "Manuel inceleme takvimleri oluşturulmuştur."},
        {"title": "Lifecycle maintenance workbook recap", "content": "Bakım defteri hazırlandı."},
        {"title": "Retention/DataLake/generated docs review recap", "content": "Dosya saklama ve inceleme defteri."},
        {"title": "Quality/safety/incident/redteam/governance review recap", "content": "Kalite ve güvenlik değerlendirmeleri."},
        {"title": "Deprecation rehearsal recap", "content": "Offline deneme amaçlı deprecation provası."},
        {"title": "Migration readiness recap", "content": "Local migration deneme planı."},
        {"title": "v1.x roadmap governance recap", "content": "Local roadmap planlama defteri."},
        {"title": "Change-control rehearsal recap", "content": "Değişiklik kontrol provası."},
        {"title": "No-go/safe-go recap", "content": "Güvenlik sınırları."},
        {"title": "Final manual review requirements", "content": "Tüm adımlar manuel onay gerektirir."},
        {"title": "Final non-production boundary statement", "content": "Sistem kesinlikle canlı ortama çıkmaya hazır değildir."}
    ]

def build_final_local_longterm_operations_binder(project_root: Path, profile: LocalLongTermOperationsProfile) -> tuple[str, dict]:
    sections = build_longterm_operations_binder_sections(project_root, profile)
    text = "# Final Local Long-Term Operations Binder\n\n"
    for sec in sections:
        text += f"## {sec['title']}\n{sec['content']}\n\n"
    summary = summarize_longterm_operations_binder(text)
    return text, summary

def summarize_longterm_operations_binder(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("##")
    }

def save_longterm_operations_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return output_path
