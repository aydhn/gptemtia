from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile
from .briefing_models import DeckSlideSource, build_deck_slide_id

def build_default_deck_slides(profile: LocalBriefingProfile) -> list[DeckSlideSource]:
    slides = [
        ("Proje Ozeti", ["Offline arastirma platformu", "Makro ve emtia sinyalleri", "Lokal calisma prensibi"], "Sadece arastirma icindir."),
        ("Neden local/offline?", ["Veri guvenligi", "Risk izolasyonu", "Bagimsiz test ortami"], "Harici API/LLM veri gonderimi kapalidir."),
        ("Sistem ne yapar?", ["Veri toplama", "Feature muhendisligi", "Backtest/Paper trading loglama"], "Model egitimi localdir."),
        ("Sistem ne yapmaz?", ["Canli emir gondermez", "Broker'a baglanmaz", "Yatirim tavsiyesi vermez"], "Kesinlikle production degildir."),
        ("Ana modul aileleri", ["DataLake", "FeatureStore", "Core AI", "Reports"], "Moduller izoledir."),
        ("Raporlama ve DataLake", ["Her cikti kayit altinda", "Offline graph ve timeline"], "Local klasorler kullanilir."),
        ("Guvenlik sinirlari", ["Kod silme/degistirme yok", "Harici cloud upload yok"], "Read-only analiz odagi."),
        ("Evidence/metadata/graph/timeline", ["Metadata tracking", "Knowledge graph", "Event timeline"], "Karar destek surecleri."),
        ("Consistency/readiness/maintenance/archive/DR/training", ["Otomatize bakim testleri", "DR rehearsal", "Arsivleme"], "Sistemin devamliligi."),
        ("Karar baglami", ["Manuel review gerekir", "Ciktilar bilgi amacli"], "Otomatik yatirim karari alinmaz."),
        ("Sinirliliklar", ["Tarihsel veri gecikmesi", "Sentetik test limitleri"], "Gercek piyasa sartlarindan sapabilir."),
        ("Guvenli sonraki adimlar", ["Local loglari incele", "Model metriklerini gozden gecir"], "Hicbir canli baglanti kurma.")
    ]
    
    out = []
    for i, (title, bullets, notes) in enumerate(slides, 1):
        out.append(DeckSlideSource(
            slide_id=build_deck_slide_id(i, title),
            slide_number=i,
            title=title,
            audience_label="nontechnical_audience",
            bullets=bullets,
            speaker_notes=notes,
            safety_notes=["Yatirim tavsiyesi icermez."]
        ))
    return out

def build_non_technical_briefing_deck_source(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    slides = build_default_deck_slides(profile)
    if len(slides) > profile.max_slide_items:
        slides = slides[:profile.max_slide_items]
    df = pd.DataFrame([vars(s) for s in slides])
    summary = summarize_deck_source(df)
    return df, summary

def export_deck_source_to_markdown(slide_df: pd.DataFrame) -> str:
    text = "# Non-Technical Briefing Deck Source\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    for _, row in slide_df.iterrows():
        text += f"## Slide {row['slide_number']}: {row['title']}\n"
        for b in row['bullets']:
            text += f"- {b}\n"
        text += f"**Speaker Notes:** {row['speaker_notes']}\n\n"
    return text

def export_deck_source_to_json(slide_df: pd.DataFrame) -> dict:
    return slide_df.to_dict(orient="records")

def summarize_deck_source(slide_df: pd.DataFrame) -> dict:
    if slide_df is None or slide_df.empty:
        return {"total_slides": 0}
    return {"total_slides": len(slide_df)}
