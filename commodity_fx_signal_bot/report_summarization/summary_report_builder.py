import pandas as pd

def build_summary_disclaimer() -> str:
    return "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"

def build_report_summary_registry_markdown_report(summary: dict, inventory_df: pd.DataFrame | None = None) -> str:
    md = "# REPORT SUMMARY REGISTRY\n\n"
    md += build_summary_disclaimer()
    md += f"Total Reports: {summary.get('total_reports', 0)}\n\n"
    return md

def build_executive_summary_markdown_report(summary: dict, executive_text: str) -> str:
    md = build_summary_disclaimer()
    md += executive_text
    return md

def build_analyst_brief_markdown_report(summary: dict, analyst_brief_text: str, focus_df: pd.DataFrame | None = None) -> str:
    md = build_summary_disclaimer()
    md += analyst_brief_text
    return md

def build_weekly_review_pack_markdown_report(summary: dict, review_text: str, checklist_df: pd.DataFrame | None = None) -> str:
    md = build_summary_disclaimer()
    md += review_text
    return md

def build_research_digest_markdown_report(summary: dict, cards_df: pd.DataFrame | None = None) -> str:
    md = "# RESEARCH DIGEST\n\n"
    md += build_summary_disclaimer()
    md += f"Total Cards: {summary.get('total_cards', 0)}\n"
    return md

def build_summary_quality_markdown_report(summary: dict, quality: dict) -> str:
    md = "# SUMMARY QUALITY REPORT\n\n"
    md += build_summary_disclaimer()
    md += f"Passed: {quality.get('passed', False)}\n"
    md += f"Warnings: {quality.get('warning_count', 0)}\n"
    if quality.get("forbidden_terms_found"):
        md += f"Forbidden terms found: {quality['forbidden_terms_found']}\n"
    return md

def build_briefing_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    md = "# BRIEFING STATUS\n\n"
    md += build_summary_disclaimer()
    return md
