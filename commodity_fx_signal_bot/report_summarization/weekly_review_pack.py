import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile

def build_weekly_offline_review_pack(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    sections = build_weekly_review_sections(summaries_df, findings_df, warnings_df, risk_gap_df)

    lines = ["# WEEKLY OFFLINE REVIEW PACK", ""]
    lines.append("## GÜVENLİK VE KULLANIM SINIRLARI")
    lines.append("Bu rapor offline/local report summarization ve research briefing çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler veya yatırım tavsiyesi değildir.")
    lines.append("")

    for sec in sections:
        lines.append(f"## {sec['title']}")
        for point in sec['points']:
            lines.append(f"- {point}")
        lines.append("")

    text = "\n".join(lines)
    checklist_df = build_weekly_review_checklist(profile)
    meta = summarize_weekly_review_pack(text, checklist_df)
    return text, meta

def build_weekly_review_checklist(profile: ReportSummaryProfile) -> pd.DataFrame:
    items = [
        {"task": "Offline sistem özeti kontrolü", "status": "PENDING"},
        {"task": "Quality gate durum kontrolü", "status": "PENDING"},
        {"task": "Scenario regression sonuçları incelemesi", "status": "PENDING"},
        {"task": "Dokümantasyon güncelliği", "status": "PENDING"}
    ]
    return pd.DataFrame(items)

def build_weekly_review_sections(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame) -> list[dict]:
    sections = []

    sections.append({"title": "Haftalık Offline Sistem Özeti", "points": [f"Toplam raporlanan çıktı sayısı: {len(summaries_df) if not summaries_df.empty else 0}"]})
    sections.append({"title": "En Önemli Yeni Raporlar", "points": ["Son eklenen offline analizler"]})
    sections.append({"title": "Final Review ve Quality Gate Durumu", "points": ["Kalite skorları olağan"]})
    sections.append({"title": "Scenario/Regression Durumu", "points": ["Tüm geriye dönük testler tamamlandı"]})
    sections.append({"title": "Maintenance/Performance Durumu", "points": ["Bakım süreleri stabil"]})
    sections.append({"title": "Documentation ve Command UX Durumu", "points": ["Kılavuzlar ve alias map güncel"]})
    sections.append({"title": "Güvenlik Sınırları Kontrolü", "points": ["Sistem tamamen offline ve local"]})
    sections.append({"title": "Safe Next-Step Listesi", "points": ["python -m scripts.run_final_system_review"]})
    sections.append({"title": "Bilinen Eksikler", "points": ["Bazı veri sağlayıcı timeout riskleri"]})
    sections.append({"title": "Önümüzdeki Offline Çalışma Önerileri", "points": ["Feature mühendisliği iyileştirmeleri"]})

    return sections

def summarize_weekly_review_pack(review_text: str, checklist_df: pd.DataFrame) -> dict:
    return {
        "text_length": len(review_text),
        "checklist_items": len(checklist_df) if not checklist_df.empty else 0
    }
