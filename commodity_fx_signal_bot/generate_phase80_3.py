import os

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

meta_review = """
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
    text = "# Final Project Meta-Review Report\\n\\n"
    text += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
    for s in sections:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
    summary = summarize_meta_review_report(text)
    return text, summary

def summarize_meta_review_report(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("## "),
        "has_warning": "UYARI" in text
    }
"""
write_file("local_closure/meta_review.py", meta_review)

lessons_learned = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile
from local_closure.closure_models import LessonLearnedItem, build_lesson_learned_id, lesson_learned_item_to_dict

def build_default_lessons_learned(profile: LocalClosureProfile) -> list[LessonLearnedItem]:
    return [
        LessonLearnedItem(
            lesson_id=build_lesson_learned_id("Data Lake Ayrımı"),
            lesson_title="Data Lake Ayrımı",
            category="architecture",
            observation="Veri depolama ile raporlama ayrılmalı.",
            implication="Daha kolay test edilebilirlik.",
            recommendation="Klasör yapısını strict tut.",
            warnings=[]
        ),
        LessonLearnedItem(
            lesson_id=build_lesson_learned_id("Safety First"),
            lesson_title="Safety First",
            category="safety",
            observation="Canlı işlem kazalarına karşı önlem şart.",
            implication="Her faza non-use eklenmeli.",
            recommendation="Dry-run default olmalı.",
            warnings=[]
        )
    ]

def build_lessons_learned_compendium(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    lessons = build_default_lessons_learned(profile)
    df = pd.DataFrame([lesson_learned_item_to_dict(l) for l in lessons])
    summary = summarize_lessons_learned(df)
    return df, summary

def summarize_lessons_learned(lesson_df: pd.DataFrame) -> dict:
    return {
        "total_lessons": len(lesson_df),
        "categories": lesson_df["category"].nunique() if not lesson_df.empty else 0
    }

def export_lessons_learned_markdown(lesson_df: pd.DataFrame, summary: dict) -> str:
    md = "# Lessons Learned Compendium\\n\\n"
    md += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
    if lesson_df.empty:
        md += "No lessons found.\\n"
        return md
    for _, row in lesson_df.iterrows():
        md += f"## {row['lesson_title']}\\n"
        md += f"- **Category**: {row['category']}\\n"
        md += f"- **Observation**: {row['observation']}\\n"
        md += f"- **Implication**: {row['implication']}\\n"
        md += f"- **Recommendation**: {row['recommendation']}\\n\\n"
    return md
"""
write_file("local_closure/lessons_learned.py", lessons_learned)

roadmap_backlog = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile
from local_closure.closure_models import RoadmapItem, build_roadmap_item_id, roadmap_item_to_dict
from local_closure.closure_labels import list_roadmap_status_labels

def build_default_roadmap_items(profile: LocalClosureProfile) -> list[RoadmapItem]:
    return [
        RoadmapItem(
            roadmap_id=build_roadmap_item_id("Offline Model Training"),
            title="Offline Model Training",
            category="model research offline",
            status="roadmap_candidate",
            rationale="Gelecekte farklı algoritmalar test edilebilir.",
            prerequisites=["Feature Store update"],
            safety_boundaries=["Strict local execution", "No live connection"],
            warnings=[]
        ),
        RoadmapItem(
            roadmap_id=build_roadmap_item_id("Live Trading Connection"),
            title="Live Trading Connection",
            category="governance extensions",
            status="roadmap_blocked_by_safety",
            rationale="Canlı trade projenin offline sınırlarını ihlal eder.",
            prerequisites=[],
            safety_boundaries=["Blocked by policy"],
            warnings=["Blocked by safety restrictions"]
        )
    ]

def classify_roadmap_item_safety(item: RoadmapItem, profile: LocalClosureProfile) -> dict:
    if "live" in item.title.lower() or "broker" in item.title.lower() or "deploy" in item.title.lower():
        item.status = "roadmap_blocked_by_safety"
        item.warnings.append("Blocked by safety restrictions")
    return roadmap_item_to_dict(item)

def build_future_roadmap_backlog(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_roadmap_items(profile)
    processed = [classify_roadmap_item_safety(item, profile) for item in items]
    df = pd.DataFrame(processed)
    summary = summarize_roadmap_backlog(df)
    return df, summary

def summarize_roadmap_backlog(roadmap_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(roadmap_df),
        "blocked_items": len(roadmap_df[roadmap_df["status"] == "roadmap_blocked_by_safety"]) if not roadmap_df.empty else 0
    }

def export_roadmap_backlog_markdown(roadmap_df: pd.DataFrame, summary: dict) -> str:
    md = "# Future Roadmap Backlog\\n\\n"
    md += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
    if roadmap_df.empty:
        md += "No items found.\\n"
        return md
    for _, row in roadmap_df.iterrows():
        md += f"## {row['title']}\\n"
        md += f"- **Status**: {row['status']}\\n"
        md += f"- **Category**: {row['category']}\\n"
        md += f"- **Rationale**: {row['rationale']}\\n\\n"
    return md
"""
write_file("local_closure/roadmap_backlog.py", roadmap_backlog)

future_phase_candidates = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_candidate_phase_from_roadmap_row(row: pd.Series, phase_number_hint: int, profile: LocalClosureProfile) -> dict:
    return {
        "candidate_phase": f"Phase {phase_number_hint}",
        "title": row["title"],
        "status": row["status"] if row["status"] != "roadmap_blocked_by_safety" else "manual_review_required",
        "description": row["rationale"]
    }

def build_future_phase_candidate_registry(roadmap_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    candidates = []
    if not roadmap_df.empty:
        valid_items = roadmap_df[roadmap_df["status"] != "roadmap_blocked_by_safety"]
        for idx, row in valid_items.iterrows():
            candidates.append(build_candidate_phase_from_roadmap_row(row, 81 + idx, profile))
    df = pd.DataFrame(candidates)
    summary = summarize_future_phase_candidates(df)
    return df, summary

def summarize_future_phase_candidates(candidate_df: pd.DataFrame) -> dict:
    return {
        "total_candidates": len(candidate_df)
    }
"""
write_file("local_closure/future_phase_candidates.py", future_phase_candidates)

governance_rehearsal = """
from pathlib import Path
from local_closure.closure_config import LocalClosureProfile

def build_governance_rehearsal_sections(profile: LocalClosureProfile) -> list[dict]:
    return [
        {"title": "Local-only Governance Prensibi", "content": "Herhangi bir cloud veya live değişiklik yasaktır."},
        {"title": "Manual Review Ritmi", "content": "Değişiklikler manuel onaydan geçmelidir."},
        {"title": "Change Request Intake", "content": "Offline araştırma odaklı CR'lar kabul edilir."},
        {"title": "Future Phase Approval Rehearsal", "content": "Fazlar mock-approval alır."},
        {"title": "Safety Boundary Review", "content": "Kuralların ihlal edilmediği test edilir."},
        {"title": "Documentation Review", "content": "Dokümantasyon güncelliği sağlanır."},
        {"title": "Evidence Review", "content": "Kanıtların tamlığı incelenir."},
        {"title": "Roadmap Triage", "content": "Önceliklendirme yapılır."},
        {"title": "No-go Escalation", "content": "Live trade varsa reddedilir."},
        {"title": "Aftercare Communication", "content": "Bakım planı mock olarak işletilir."},
        {"title": "Neyi Yapmamalı?", "content": "Canlı ortama kod atılmamalı."}
    ]

def build_post_project_governance_rehearsal_guide(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    sections = build_governance_rehearsal_sections(profile)
    text = "# Post-Project Governance Rehearsal Guide\\n\\n"
    text += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
    for s in sections:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
    summary = summarize_governance_rehearsal_guide(text)
    return text, summary

def summarize_governance_rehearsal_guide(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI" in text
    }
"""
write_file("local_closure/governance_rehearsal.py", governance_rehearsal)
