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
    
    text = "# Project Narrative Report\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    
    for s in sections[:profile.max_sections]:
        text += f"## {s['title']}\n{s['content']}\n\n"
        
    summary = summarize_project_narrative(text)
    return text, summary

def summarize_project_narrative(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI:" in text,
        "is_investment_advice": False
    }
