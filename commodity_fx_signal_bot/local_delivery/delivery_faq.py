import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def build_default_delivery_faq(profile: LocalDeliveryProfile) -> pd.DataFrame:
    faqs = [
        {"q": "Bu gerçek teslim mi?", "a": "Hayır, bu bir provadır."},
        {"q": "Paket zip olarak üretildi mi?", "a": "Hayır, üretilmedi."},
        {"q": "Cloud'a yüklendi mi?", "a": "Hayır, yüklenmedi."},
        {"q": "Canlı trade yapılabilir mi?", "a": "Hayır, yapılamaz."},
        {"q": "Broker bağlantısı var mı?", "a": "Hayır, yoktur."},
        {"q": "Raporlar yatırım tavsiyesi mi?", "a": "Hayır, değildir."}
    ]
    return pd.DataFrame(faqs)

def build_delivery_recipient_faq(profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_delivery_faq(profile)
    return df, summarize_delivery_faq(df)

def summarize_delivery_faq(faq_df: pd.DataFrame) -> dict:
    return {"total_faqs": len(faq_df)}
