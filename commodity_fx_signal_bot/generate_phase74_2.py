import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

write_file('local_briefing/executive_summary.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_executive_summary_sections(project_root: Path, profile: LocalBriefingProfile) -> list[dict]:
    return [
        {"title": "Proje Amaci", "content": "Offline/local makro-emtia sinyal arastirma platformu saglamak."},
        {"title": "Offline/local Kapsam", "content": "Sadece local calisir, cloud/broker baglantisi yoktur."},
        {"title": "Ana Yetenekler", "content": "Veri toplama, feature engineering, backtest, evidence yonetimi."},
        {"title": "Ne Yapmaz?", "content": "Canli emir gondermez, gercek pozisyon acmaz, yatirim tavsiyesi uretmez."},
        {"title": "Faz Gelisimi", "content": "Phase 1-73 arasi arastirma, validation, maintenance, dr katmanlari insa edildi."},
        {"title": "Guvenlik Sinirlari", "content": "Harici API/LLM ile veri/sifre paylasilmaz. Canli execution engellidir."},
        {"title": "Raporlama ve DataLake Yapisi", "content": "Tum ciktilar DataLake ve reports/ klasorunde lokal olarak tutulur."},
        {"title": "Cross-layer Denetim Katmanlari", "content": "Consistency, readiness, governance ile sonuclarin tutarliligi dogrulanir."},
        {"title": "Egitim, Bakim, Arsiv ve DR Katmanlari", "content": "Sistem uzun vadeli kendi kendine bakim ve disaster recovery destekler."},
        {"title": "Sinirliliklar", "content": "Backtest verisi gecikmeli olabilir, model uretim onayi degildir."},
        {"title": "Manuel Review Gerektiren Alanlar", "content": "Yeni model egitimi, gercek karar alma, parametre degisimi."},
        {"title": "Guvenli Sonraki Adimlar", "content": "Raporlari okuma, offline paper trading incelemesi."}
    ]

def build_executive_summary_pack(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    sections = build_executive_summary_sections(project_root, profile)
    
    text = "# Executive Summary Pack\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    
    for s in sections[:profile.max_sections]:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
        
    summary = summarize_executive_summary_pack(text)
    return text, summary

def summarize_executive_summary_pack(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI:" in text,
        "is_investment_advice": False
    }
''')

write_file('local_briefing/project_one_pager.py', '''
from pathlib import Path
from .briefing_config import LocalBriefingProfile

def build_one_pager_sections(profile: LocalBriefingProfile) -> list[dict]:
    return [
        {"title": "Amac", "content": "Makro ekonomik ve emtia verileriyle offline arastirma yapmak."},
        {"title": "Ana Yetenekler", "content": "1. Backtest 2. Model Training 3. Reporting 4. Evidence Governance 5. Readiness."},
        {"title": "Net Sinirlar", "content": "1. Canli emir yok 2. Broker yok 3. Yatirim tavsiyesi yok 4. Cloud yok 5. Oto-deploy yok."},
        {"title": "Kimler Kullanir?", "content": "Quant arastirmacilari, veri bilimciler, risk analistleri, uyum denetcileri."},
        {"title": "Nerede Cikti Uretir?", "content": "Lokal DataLake (data/lake) ve reports klasorleri."},
        {"title": "En Guvenli Ilk Okuma Sirasi", "content": "One pager -> Executive Summary -> Non-technical deck -> Reports."},
        {"title": "Sonraki Manuel Adimlar", "content": "Ciktilari offline incelemek, model basarimini manual dogrulamak."}
    ]

def build_project_one_pager(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    sections = build_one_pager_sections(profile)
    
    text = "# Project One-Pager\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    
    for s in sections:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
        
    summary = summarize_project_one_pager(text)
    return text, summary

def summarize_project_one_pager(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI:" in text,
        "is_investment_advice": False
    }
''')

write_file('local_briefing/deck_source.py', '''
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
    text = "# Non-Technical Briefing Deck Source\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    for _, row in slide_df.iterrows():
        text += f"## Slide {row['slide_number']}: {row['title']}\\n"
        for b in row['bullets']:
            text += f"- {b}\\n"
        text += f"**Speaker Notes:** {row['speaker_notes']}\\n\\n"
    return text

def export_deck_source_to_json(slide_df: pd.DataFrame) -> dict:
    return slide_df.to_dict(orient="records")

def summarize_deck_source(slide_df: pd.DataFrame) -> dict:
    if slide_df is None or slide_df.empty:
        return {"total_slides": 0}
    return {"total_slides": len(slide_df)}
''')

write_file('local_briefing/project_narrative.py', '''
from pathlib import Path
from .briefing_config import LocalBriefingProfile

def build_project_narrative_sections(project_root: Path, profile: LocalBriefingProfile) -> list[dict]:
    return [
        {"title": "Baslangic Problemi", "content": "Veri odemeli olmayan, guvenli ve kapali bir offline arastirma platformu ihtiyaci."},
        {"title": "Offline Research Platform Yaklasimi", "content": "Butun operasyon lokal bilgisayarda calisir."},
        {"title": "Fazlarla Genisleyen Mimari", "content": "1-73 fazda adim adim gelisen veri, model, guvenlik ve yonetisim katmanlari."},
        {"title": "Guvenli Kullanim Sinirlari", "content": "API baglantilari ve canli islem engellidir."},
        {"title": "Arastirma/rapor/metadata/graph/timeline Tutarliligi", "content": "Uretilen veriler lokal consistency aracliyla dogrulanir."},
        {"title": "Teslim, Bakim, Arsiv, DR ve Egitim Katmanlari", "content": "Sistemin operasyonel yasami lokal olarak garanti altina alinmistir."},
        {"title": "Mevcut Olgunluk", "content": "Arastirma icin olgun, ancak canli uretim icin degil."},
        {"title": "Bilincli Sinirlamalar", "content": "Gercek zamanli veri akisi yerine batch isleme ve sentetik testler tercih edilmistir."},
        {"title": "Manuel Review Kulturu", "content": "Hicbir model sonucu insan onayi olmadan dikkate alinmaz."}
    ]

def build_project_narrative_report(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    sections = build_project_narrative_sections(project_root, profile)
    
    text = "# Project Narrative Report\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    
    for s in sections[:profile.max_sections]:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
        
    summary = summarize_project_narrative(text)
    return text, summary

def summarize_project_narrative(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI:" in text,
        "is_investment_advice": False
    }
''')
