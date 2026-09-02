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
    
    text = "# Executive Summary Pack\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    
    for s in sections[:profile.max_sections]:
        text += f"## {s['title']}\n{s['content']}\n\n"
        
    summary = summarize_executive_summary_pack(text)
    return text, summary

def summarize_executive_summary_pack(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI:" in text,
        "is_investment_advice": False
    }
