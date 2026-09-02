from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_boundary_summary_table(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    boundaries = [
        ("canli emir yok", "Sistem broker'a veri gondermez"),
        ("broker entegrasyonu yok", "Broker API keyleri sisteme dahil edilmemistir"),
        ("gercek pozisyon yok", "Sadece kagit uzerinde islem yapilir"),
        ("yatirim tavsiyesi yok", "Uretilen raporlar analizdir, tavsiye degildir"),
        ("model deployment yok", "Modeller production sunucularina aktarilmaz"),
        ("production scheduler yok", "Canli operasyon tetikleyici scheduler yoktur"),
        ("background daemon yok", "Sonsuz dongude calisan trading botu yoktur"),
        ("cloud upload yok", "Veriler disariya gonderilmez"),
        ("external LLM/API yok", "Harici zeka servisi cagirisi yapilmaz"),
        ("web dashboard yok", "Lokal UI disinda web servisi yoktur"),
        ("auto-fix/destructive action yok", "Sistem kodlari otomatik degistirmez")
    ]
    df = pd.DataFrame(boundaries, columns=["boundary", "description"])
    return df, summarize_boundary_non_use("", df)

def build_boundary_non_use_summary(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_boundary_summary_table(profile)
    text = "# Boundary and Non-Use Summary\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    for _, row in df.iterrows():
        text += f"- **{row['boundary']}**: {row['description']}\n"
    return text, summary

def summarize_boundary_non_use(text: str, boundary_df: pd.DataFrame) -> dict:
    if boundary_df is None or boundary_df.empty:
        return {"total_boundaries": 0}
    return {"total_boundaries": len(boundary_df)}
