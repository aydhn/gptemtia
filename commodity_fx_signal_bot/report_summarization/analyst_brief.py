import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.module_summaries import rank_modules_by_attention_need

def build_analyst_brief(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    sections = build_analyst_brief_sections(summaries_df, findings_df, warnings_df, risk_gap_df, profile)

    lines = ["# ANALYST BRIEF", ""]
    lines.append("## GÜVENLİK VE KULLANIM SINIRLARI")
    lines.append("Bu rapor offline/local report summarization ve research briefing çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler veya yatırım tavsiyesi değildir.")
    lines.append("")

    for sec in sections:
        lines.append(f"## {sec['title']}")
        for point in sec['points']:
            lines.append(f"- {point}")
        lines.append("")

    text = "\n".join(lines)
    focus_df = build_focus_area_table(findings_df, warnings_df, risk_gap_df)
    meta = summarize_analyst_brief(text, focus_df)
    return text, meta

def build_analyst_brief_sections(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> list[dict]:
    sections = []

    sections.append({"title": "Bugün / Son Çıktı Setinde Ne Değişti?", "points": ["Offline veri seti analizlerinde güncellemeler tespit edildi."]})

    attention_df = rank_modules_by_attention_need(findings_df, warnings_df)
    attn_points = []
    if not attention_df.empty:
        for idx, row in attention_df.head(5).iterrows():
            attn_points.append(f"{row['module_name']} (Skor: {row['attention_score']})")
    if not attn_points:
        attn_points.append("Özel dikkat isteyen modül bulunamadı.")
    sections.append({"title": "Hangi Modüller Dikkat İstiyor?", "points": attn_points})

    sections.append({"title": "Hangi Raporlar Okunmalı?", "points": ["executive_summary_report.md", "research_digest_report.md"]})

    sections.append({"title": "Hangi Safe Komutlar Öneriliyor?", "points": ["python -m scripts.run_safety_audit", "python -m scripts.run_final_system_review"]})

    gap_points = []
    if not risk_gap_df.empty and "text" in risk_gap_df:
        gap_points.extend(risk_gap_df["text"].head(5).tolist())
    if not gap_points:
        gap_points.append("Kritik bir gap saptanmadı.")
    sections.append({"title": "Hangi Regression/Final Review Gap'leri Var?", "points": gap_points})

    sections.append({"title": "Hangi Dokümantasyon veya Bakım Aksiyonları Var?", "points": ["Maintenance review follow-up işlemleri tavsiye edilir."]})
    sections.append({"title": "Hangi Bilgiler Yetersiz?", "points": ["Data pipeline kapsamındaki bazı kaynaklar eksik olabilir."]})

    return sections

def build_focus_area_table(findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame) -> pd.DataFrame:
    df = rank_modules_by_attention_need(findings_df, warnings_df)
    return df

def summarize_analyst_brief(brief_text: str, focus_df: pd.DataFrame) -> dict:
    return {
        "text_length": len(brief_text),
        "top_focus_modules": focus_df["module_name"].head(3).tolist() if not focus_df.empty else []
    }
