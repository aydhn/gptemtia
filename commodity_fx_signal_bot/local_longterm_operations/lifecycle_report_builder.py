"""Lifecycle report builder."""
import pandas as pd

def build_lifecycle_disclaimer() -> str:
    return "Bu rapor offline/local long-term operations rehearsal ve lifecycle roadmap governance çıktısıdır; gerçek production operations plan, official lifecycle policy, release commitment, legal/compliance sign-off, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def _build_md(title: str, content: str) -> str:
    return f"# {title}\n\n{content}\n\n{build_lifecycle_disclaimer()}"

def build_longterm_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return _build_md("Long-term Domain Registry", str(summary))

def build_operations_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    return _build_md("Operations Binder", binder_text or str(summary))

def build_review_calendar_markdown_report(summary: dict, calendar_df: pd.DataFrame | None = None) -> str:
    return _build_md("Review Calendar", str(summary))

def build_lifecycle_workbook_markdown_report(summary: dict, workbook_df: pd.DataFrame | None = None) -> str:
    return _build_md("Lifecycle Workbook", str(summary))

def build_deprecation_rehearsal_markdown_report(summary: dict, deprecation_df: pd.DataFrame | None = None) -> str:
    return _build_md("Deprecation Rehearsal", str(summary))

def build_v1x_roadmap_governance_markdown_report(summary: dict, roadmap_text: str | None = None) -> str:
    return _build_md("Roadmap Governance", roadmap_text or str(summary))

def build_lifecycle_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return _build_md("Lifecycle Quality", str(quality or summary))

def build_lifecycle_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return _build_md("Lifecycle Status", str(summary))
