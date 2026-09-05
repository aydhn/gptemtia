import pandas as pd

def build_review_disclaimer() -> str:
    return "\n\n> **UYARI:** Bu cikti offline/local human-review rehearsal ve terminal review governance raporudur. Gercek approval workflow, expert sign-off, legal/compliance approval, production approval, canli emir, broker talimati, model deployment veya yatirim tavsiyesi degildir.\n"

def build_review_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    md = "# Review Governance Domain Registry\n\n"
    if domain_df is not None:
        md += domain_df.to_markdown(index=False)
    md += build_review_disclaimer()
    return md

def build_human_review_cockpit_markdown_report(summary: dict, cockpit_text: str | None = None) -> str:
    md = cockpit_text if cockpit_text else "# Human Review Cockpit\n\n"
    md += build_review_disclaimer()
    return md

def build_manual_approval_ledger_markdown_report(summary: dict, ledger_text: str | None = None) -> str:
    md = ledger_text if ledger_text else "# Manual Approval Ledger\n\n"
    md += build_review_disclaimer()
    return md

def build_expert_review_workbook_markdown_report(summary: dict, expert_df: pd.DataFrame | None = None) -> str:
    md = "# Expert Review Workbook\n\n"
    if expert_df is not None:
        md += expert_df.to_markdown(index=False)
    md += build_review_disclaimer()
    return md

def build_reviewer_console_markdown_report(summary: dict, console_text: str | None = None) -> str:
    md = console_text if console_text else "# Offline Reviewer Console\n\n"
    md += build_review_disclaimer()
    return md

def build_review_governance_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    md = binder_text if binder_text else "# Terminal Review Governance Binder\n\n"
    md += build_review_disclaimer()
    return md

def build_review_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    md = "# Review Quality Report\n\n"
    md += build_review_disclaimer()
    return md

def build_review_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    md = "# Review Status Report\n\n"
    if status_df is not None:
        md += status_df.to_markdown(index=False)
    md += build_review_disclaimer()
    return md
