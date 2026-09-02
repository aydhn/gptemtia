import pandas as pd
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
