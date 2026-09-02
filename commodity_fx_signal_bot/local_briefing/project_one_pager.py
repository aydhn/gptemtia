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
    
    text = "# Project One-Pager\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
        
    summary = summarize_project_one_pager(text)
    return text, summary

def summarize_project_one_pager(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI:" in text,
        "is_investment_advice": False
    }
