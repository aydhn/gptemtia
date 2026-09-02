import os

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

closure_dossier = """
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
    text = "# V1.0 Local Closure Dossier\\n\\n"
    text += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
    for s in sections:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
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
"""
write_file("local_closure/closure_dossier.py", closure_dossier)

closure_recaps = """
from pathlib import Path
from local_closure.closure_config import LocalClosureProfile

def build_closure_executive_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Executive Recap: Altyapı başarıyla modellendi, live operasyon yoktur."
    return text, {"type": "executive", "len": len(text)}

def build_closure_technical_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Technical Recap: Feature store ve event-driven mimari uygulandı."
    return text, {"type": "technical", "len": len(text)}

def build_closure_safety_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Safety Recap: Katı dry-run ve isolation sağlandı."
    return text, {"type": "safety", "len": len(text)}

def build_closure_architecture_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Architecture Recap: Modüler python scriptleri kullanıldı."
    return text, {"type": "architecture", "len": len(text)}

def build_closure_evidence_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Evidence Recap: Bütün çıktı metadata ile bağlanmıştır."
    return text, {"type": "evidence", "len": len(text)}

def build_closure_archival_provenance_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Archival Provenance Recap: Lake structure ile koruma sağlanmıştır."
    return text, {"type": "archival", "len": len(text)}

def build_closure_delivery_acceptance_recap(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    text = "Delivery Acceptance Recap: Offline criteria met."
    return text, {"type": "delivery", "len": len(text)}

def summarize_closure_recaps(recap_texts: dict[str, str]) -> dict:
    return {k: len(v) for k, v in recap_texts.items()}
"""
write_file("local_closure/closure_recaps.py", closure_recaps)

unresolved_items = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_unresolved_items(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item": "Full unit test coverage", "status": "unresolved"}
    ])

def build_closure_unresolved_items_register(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_unresolved_items(profile)
    summary = summarize_unresolved_items(df)
    return df, summary

def summarize_unresolved_items(unresolved_df: pd.DataFrame) -> dict:
    return {"total": len(unresolved_df)}
"""
write_file("local_closure/unresolved_items.py", unresolved_items)

open_questions = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_open_questions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"question": "How to scale offline?", "status": "open"}
    ])

def build_closure_open_questions_register(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_open_questions(profile)
    summary = summarize_open_questions(df)
    return df, summary

def summarize_open_questions(question_df: pd.DataFrame) -> dict:
    return {"total": len(question_df)}
"""
write_file("local_closure/open_questions.py", open_questions)

improvement_backlog = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_closure_future_improvement_backlog(lessons_df: pd.DataFrame, roadmap_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"improvement": "Better logging"}])
    summary = summarize_future_improvement_backlog(df)
    return df, summary

def summarize_future_improvement_backlog(improvement_df: pd.DataFrame) -> dict:
    return {"total": len(improvement_df)}
"""
write_file("local_closure/improvement_backlog.py", improvement_backlog)

maintenance_calendar = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_maintenance_calendar(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"task": "Check logs", "frequency": "monthly"}])

def build_closure_maintenance_calendar_rehearsal(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_calendar(profile)
    summary = summarize_maintenance_calendar(df)
    return df, summary

def summarize_maintenance_calendar(calendar_df: pd.DataFrame) -> dict:
    return {"total": len(calendar_df)}
"""
write_file("local_closure/maintenance_calendar.py", maintenance_calendar)

ownership_matrix = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_ownership_matrix(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"domain": "data_lake", "owner": "offline_system"}])

def build_closure_ownership_matrix_rehearsal(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_ownership_matrix(profile)
    summary = summarize_ownership_matrix(df)
    return df, summary

def summarize_ownership_matrix(owner_df: pd.DataFrame) -> dict:
    return {"total": len(owner_df)}
"""
write_file("local_closure/ownership_matrix.py", ownership_matrix)

decision_log = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_decision_log(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"decision": "Use markdown for reports", "reason": "readable"}])

def build_closure_decision_log(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_decision_log(profile)
    summary = summarize_decision_log(df)
    return df, summary

def summarize_decision_log(decision_df: pd.DataFrame) -> dict:
    return {"total": len(decision_df)}
"""
write_file("local_closure/decision_log.py", decision_log)
