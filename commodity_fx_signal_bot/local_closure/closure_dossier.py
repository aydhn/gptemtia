
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_closure_dossier_sections(
    meta_review_text: str,
    lessons_df: pd.DataFrame,
    roadmap_df: pd.DataFrame,
    recap_texts: dict[str, str],
) -> list[dict]:
    return [
        {"title": "Amaç ve Kapsam", "content": "Offline platformun final durumunun belgelenmesi."},
        {"title": "v1.0 Local Closure Ne Demektir?", "content": "Geliştirme döngüsünün offline provasıdır."},
        {"title": "v1.0 Local Closure Ne Değildir?", "content": "Gerçek release veya yatırım tavsiyesi değildir."},
        {"title": "Faz 1-80 Genel Özet", "content": "Altyapı ve dokümantasyon tamamlandı."},
        {"title": "Ana Modül Aileleri", "content": "Storage, ML, Reports, Local Closure vs."},
        {"title": "Safety/Non-use Özeti", "content": "Sıkı önlemler alındı."},
        {"title": "Evidence/Provenance Özeti", "content": "İzlenebilirlik sağlandı."},
        {"title": "Delivery/Acceptance Özeti", "content": "Local teslimat kriterleri test edildi."},
        {"title": "Lessons Learned", "content": f"{len(lessons_df) if lessons_df is not None else 0} ders çıkarıldı."},
        {"title": "Roadmap Backlog Özeti", "content": f"{len(roadmap_df) if roadmap_df is not None else 0} aday özellik var."},
        {"title": "Unresolved Items", "content": "Listede tutulmaktadır."},
        {"title": "No-go/Safe-go", "content": "Safety criteria apply."},
        {"title": "Handoff-Aftercare", "content": "Maintenance log aktiftir."},
        {"title": "Final Limitation Statement", "content": "Sistem kapalı devredir."},
        {"title": "Manual Review Requirements", "content": "Her yeni özellik için şarttır."}
    ]

def build_v1_local_closure_dossier(
    meta_review_text: str,
    lessons_df: pd.DataFrame,
    roadmap_df: pd.DataFrame,
    recap_texts: dict[str, str],
    profile: LocalClosureProfile,
) -> tuple[str, dict]:
    sections = build_closure_dossier_sections(meta_review_text, lessons_df, roadmap_df, recap_texts)
    text = "# V1.0 Local Closure Dossier\n\n"
    text += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    summary = summarize_closure_dossier(text)
    return text, summary

def save_v1_local_closure_dossier(text: str, output_path: Path) -> Path:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_closure_dossier(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("## "),
        "has_warning": "UYARI" in text
    }
