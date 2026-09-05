"""Export report builder."""
import pandas as pd

def build_documentation_export_disclaimer() -> str:
    return "Bu çıktı offline/local documentation export rehearsal ve printable documentation pack raporudur. Gerçek static site deployment, web dashboard, PDF export, presentation deck, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def build_documentation_export_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Domain Registry\n{build_documentation_export_disclaimer()}\n"

def build_static_site_export_markdown_report(summary: dict, static_text: str | None = None) -> str:
    return f"# Static Site Export\n{build_documentation_export_disclaimer()}\n{static_text or ''}"

def build_offline_html_pack_markdown_report(summary: dict, html_text: str | None = None) -> str:
    return f"# Offline HTML Pack\n{build_documentation_export_disclaimer()}\n"

def build_printable_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    return f"# Printable Binder\n{build_documentation_export_disclaimer()}\n"

def build_pdf_ready_docs_markdown_report(summary: dict, pdf_ready_text: str | None = None) -> str:
    return f"# PDF-Ready Docs\n{build_documentation_export_disclaimer()}\n"

def build_presentation_freeze_markdown_report(summary: dict, freeze_text: str | None = None) -> str:
    return f"# Presentation Freeze\n{build_documentation_export_disclaimer()}\n"

def build_documentation_export_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Quality Report\n{build_documentation_export_disclaimer()}\n"

def build_documentation_export_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Status Report\n{build_documentation_export_disclaimer()}\n"
