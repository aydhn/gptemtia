import os

with open("local_training/glossary.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile

def build_default_glossary_terms(profile: LocalTrainingProfile) -> pd.DataFrame:
    terms = ["dry-run", "offline/local", "non-use policy", "DataLake", "FeatureStore", "evidence governance", "artifact metadata", "model card", "dataset card", "experiment card", "local knowledge graph", "timeline", "consistency", "readiness", "maintenance", "archive", "disaster-recovery tabletop", "restore drill simulation", "resilience score", "manual review", "no-go/safe-go"]
    data = [{"term": t, "definition": f"Definition of {t}", "warnings": "Finansal tavsiye sözlüğü değildir. Sınır açıklaması içerir."} for t in terms]
    return pd.DataFrame(data)

def build_glossary_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_glossary_terms(profile)
    return df, summarize_glossary(df)

def summarize_glossary(glossary_df: pd.DataFrame) -> dict:
    if glossary_df is None or glossary_df.empty: return {"count": 0}
    return {"count": len(glossary_df)}
''')

with open("local_training/concept_map.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile

def build_concept_relationships(profile: LocalTrainingProfile) -> pd.DataFrame:
    rels = [
        ("reports", "DataLake"), ("DataLake", "FeatureStore"), ("evidence", "controls"),
        ("metadata", "artifacts"), ("graph", "relationships"), ("timeline", "events"),
        ("consistency", "coherence"), ("readiness", "handoff"), ("maintenance", "sustainability"),
        ("archive", "preservation"), ("DR", "rehearsal"), ("training", "handover education")
    ]
    data = [{"source": r[0], "target": r[1], "warnings": "Concept map external graph DB değildir. Kesin nedensellik iddiası yok. Eğitim amaçlı local map’tir."} for r in rels]
    return pd.DataFrame(data)

def build_concept_map_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_concept_relationships(profile)
    return df, summarize_concept_map(df)

def summarize_concept_map(concept_df: pd.DataFrame) -> dict:
    if concept_df is None or concept_df.empty: return {"count": 0}
    return {"count": len(concept_df)}
''')

with open("local_training/faq_registry.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile
from .training_models import TrainingFAQ, build_training_faq_id

def build_default_faq_items(profile: LocalTrainingProfile) -> list[TrainingFAQ]:
    faqs = [
        ("Bu sistem canlı trade yapıyor mu?", "Hayır"),
        ("Broker entegrasyonu var mı?", "Hayır"),
        ("Raporlar yatırım tavsiyesi mi?", "Hayır"),
        ("Readiness score ne anlama gelir?", "Local readiness"),
        ("Resilience score ne anlama gelir?", "Local resilience"),
        ("DataLake nedir?", "Storage"),
        ("Hangi komutlar güvenli?", "Read-only olanlar"),
        ("Hangi komutlar yasak?", "Yazma ve canlı olanlar"),
        ("Raw secret görürsem ne yapmalıyım?", "Raporla ve sil"),
        ("Yeni faz eklerken nelere dikkat etmeliyim?", "Offline çalışmasına")
    ]
    return [
        TrainingFAQ(
            faq_id=build_training_faq_id(q),
            question=q,
            answer=a,
            domain_label="faq_training",
            warnings=["FAQ yatırım tavsiyesi vermez.", "Broker/live/deploy yönlendirme yok.", "Raw secret response güvenli olmalı."]
        ) for q, a in faqs
    ]

def build_faq_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_faq_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_faq(df)

def summarize_faq(faq_df: pd.DataFrame) -> dict:
    if faq_df is None or faq_df.empty: return {"count": 0}
    return {"count": len(faq_df)}
''')

with open("local_training/handover_binder.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
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
    text = "\\n\\n".join([f"### {s['title']}\\n{s['content']}" for s in sections])
    text += "\\n\\n> UYARI: Binder official certification değildir. Binder canlı operasyon yetkisi vermez. Raw secret yok."
    return text, summarize_handover_binder(text)

def save_handover_education_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_handover_binder(binder_text: str) -> dict:
    return {"length": len(binder_text), "sections": binder_text.count("### ")}
''')

with open("local_training/first_week_curriculum.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile

def build_daily_curriculum_items(day_number: int, profile: LocalTrainingProfile) -> list[dict]:
    plan = {
        1: "proje amacı, sınırlar, safe usage",
        2: "kurulum, config, docs",
        3: "reports/output ve DataLake okuma",
        4: "evidence, metadata, graph, timeline",
        5: "consistency, readiness, maintenance",
        6: "archive, DR, training materials",
        7: "assessment dry-run ve manual review"
    }
    return [{"day": day_number, "topic": plan.get(day_number, "Review")}]

def build_first_week_operator_curriculum(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    data = []
    for d in range(1, 8):
        data.extend(build_daily_curriculum_items(d, profile))
    df = pd.DataFrame(data)
    df["warnings"] = "Curriculum sertifika değildir. Assessment dry-run canlı operasyon yetkisi vermez. Yatırım tavsiyesi yok."
    return df, summarize_first_week_curriculum(df)

def summarize_first_week_curriculum(curriculum_df: pd.DataFrame) -> dict:
    if curriculum_df is None or curriculum_df.empty: return {"count": 0}
    return {"count": len(curriculum_df)}
''')

with open("local_training/knowledge_transfer_checklist.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile

def build_role_specific_transfer_checklist(role_label: str, profile: LocalTrainingProfile) -> pd.DataFrame:
    items = [
        "README okundu", "SAFE_USAGE_GUIDE okundu", "OPERATOR_MANUAL okundu", "Non-use policy anlaşıldı",
        "Safe commands listesi okundu", "Forbidden actions listesi okundu", "Rapor klasörleri gezildi",
        "DataLake klasörleri gezildi", "Quality/status raporları incelendi", "Manual review queue incelendi",
        "DR/Archive/Maintenance sınırları anlaşıldı"
    ]
    return pd.DataFrame([{"role": role_label, "item": i, "status": "pending"} for i in items])

def build_knowledge_transfer_checklist(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_role_specific_transfer_checklist("operator_role", profile)
    return df, summarize_knowledge_transfer_checklist(df)

def summarize_knowledge_transfer_checklist(checklist_df: pd.DataFrame) -> dict:
    if checklist_df is None or checklist_df.empty: return {"count": 0}
    return {"count": len(checklist_df)}
''')
