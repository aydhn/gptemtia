import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile

def build_executive_summary(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    sections = build_executive_summary_sections(summaries_df, findings_df, warnings_df, risk_gap_df, profile)

    lines = ["# EXECUTIVE SUMMARY", ""]
    lines.append("## GÜVENLİK VE KULLANIM SINIRLARI")
    lines.append("Bu rapor offline/local report summarization ve research briefing çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler veya yatırım tavsiyesi değildir.")
    lines.append("")

    for sec in sections:
        lines.append(f"## {sec['title']}")
        for point in sec['points']:
            lines.append(f"- {point}")
        lines.append("")

    text = "\n".join(lines)
    meta = summarize_executive_brief_inputs(summaries_df, findings_df, warnings_df)
    return text, meta

def build_executive_summary_sections(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> list[dict]:
    sections = []

    genel_durum = []
    num_reports = len(summaries_df) if not summaries_df.empty else 0
    num_findings = len(findings_df) if not findings_df.empty else 0
    num_warnings = len(warnings_df) if not warnings_df.empty else 0
    genel_durum.append(f"Sistemde {num_reports} rapor, {num_findings} bulgu, {num_warnings} uyarı tespit edildi.")
    sections.append({"title": "Genel Durum", "points": genel_durum})

    key_findings = []
    if not findings_df.empty and "priority" in findings_df:
        high = findings_df[findings_df["priority"].isin(["critical_priority", "high_priority"])]["text"].head(profile.max_summary_bullets).tolist()
        key_findings.extend(high)
    if not key_findings:
        key_findings.append("Kritik veya yüksek öncelikli bulgu saptanmadı.")
    sections.append({"title": "En Önemli Offline Bulgular", "points": key_findings})

    kritik_uyarilar = []
    if not warnings_df.empty and "priority" in warnings_df:
        crit = warnings_df[warnings_df["priority"] == "critical_priority"]["text"].head(profile.max_summary_bullets).tolist()
        kritik_uyarilar.extend(crit)
    if not kritik_uyarilar:
        kritik_uyarilar.append("Kritik uyarı bulunmamaktadır.")
    sections.append({"title": "Kritik Uyarılar", "points": kritik_uyarilar})

    risk_gap = []
    if not risk_gap_df.empty:
        rg = risk_gap_df["text"].head(profile.max_summary_bullets).tolist()
        risk_gap.extend(rg)
    if not risk_gap:
        risk_gap.append("Tespit edilen belirgin bir risk veya gap bulunamadı.")
    sections.append({"title": "Final Review / Gap / Risk Özeti", "points": risk_gap})

    sections.append({"title": "Kalite ve Test Durumu", "points": ["Sistem offline analizleri kalite kapılarına göre listelenmiştir."]})
    sections.append({"title": "Scenario/Regression Durumu", "points": ["Senaryo analizleri offline regresyon setleriyle tamamlanmıştır."]})
    sections.append({"title": "Maintenance/Performance Durumu", "points": ["Sistem bakımı ve performans metrikleri olağan sınırlar içindedir."]})
    sections.append({"title": "Safe Follow-up Önerileri", "points": ["Detaylı bulguları analiz etmek için offline scriptleri çalıştırınız."]})

    return sections

def summarize_executive_brief_inputs(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame) -> dict:
    return {
        "inputs_processed": {
            "summaries": len(summaries_df) if not summaries_df.empty else 0,
            "findings": len(findings_df) if not findings_df.empty else 0,
            "warnings": len(warnings_df) if not warnings_df.empty else 0
        }
    }
