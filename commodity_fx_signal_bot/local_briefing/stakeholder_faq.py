import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_default_stakeholder_faq(profile: LocalBriefingProfile) -> pd.DataFrame:
    faqs = [
        ("Bu sistem para kazandirir mi?", "Sistem sadece offline arastirma yapar, garantili getiri saglamaz."),
        ("Canli emir gonderiyor mu?", "Hayir, canli islem engellenmistir."),
        ("Yatirim tavsiyesi veriyor mu?", "Hayir, ciktilar tavsiye degil, analizdir."),
        ("Broker baglantisi var mi?", "Hayir, herhangi bir broker api key icermez."),
        ("Uretime hazir mi?", "Sadece offline test ortami icin hazirdir."),
        ("Neden local/offline?", "Veri guvenligi ve arastirma izolasyonu amaciyla."),
        ("Raporlari kim okumali?", "Analistler, risk yoneticileri ve proje yoneticileri."),
        ("Score'lar ne anlama gelir?", "Model ve veri kalitesini gosteren teknik metriklerdir."),
        ("Sinirliliklar neler?", "Canli islem, gercek para kullanimi ve anlik veri akisi yoktur."),
        ("Sonraki guvenli adim nedir?", "Lokal uretilen backtest sonuclarini incelemek.")
    ]
    return pd.DataFrame(faqs, columns=["question", "answer"])

def build_stakeholder_faq_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_stakeholder_faq(profile)
    return df, summarize_stakeholder_faq(df)

def summarize_stakeholder_faq(faq_df: pd.DataFrame) -> dict:
    if faq_df is None or faq_df.empty:
        return {"total_faq": 0}
    return {"total_faq": len(faq_df)}
