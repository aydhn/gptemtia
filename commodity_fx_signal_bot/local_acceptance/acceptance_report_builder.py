import pandas as pd

def build_acceptance_disclaimer() -> str:
    return "Bu rapor offline/local final acceptance simulation ve verification rehearsal çıktısıdır; resmi audit, resmi sign-off, production release, compliance sertifikası, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def build_acceptance_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Acceptance Domain Registry\n\n{build_acceptance_disclaimer()}\n\nTotal domains: {summary.get('total_domains', 0)}\n"

def build_final_acceptance_simulation_markdown_report(summary: dict, checklist_df: pd.DataFrame | None = None) -> str:
    return f"# Final Acceptance Simulation\n\n{build_acceptance_disclaimer()}\n\nTotal items: {summary.get('total_items', 0)}\n"

def build_independent_reviewer_pack_markdown_report(summary: dict, pack_text: str | None = None) -> str:
    return f"{pack_text if pack_text else '# Independent Reviewer Pack'}\n\n{build_acceptance_disclaimer()}\n"

def build_acceptance_evidence_trail_markdown_report(summary: dict, evidence_df: pd.DataFrame | None = None) -> str:
    return f"# Audit-Style Local Evidence Trail\n\n{build_acceptance_disclaimer()}\n\nTotal evidence: {summary.get('total_evidence_items', 0)}\n"

def build_signoff_rehearsal_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    return f"{binder_text if binder_text else '# Sign-off Rehearsal Binder'}\n\n{build_acceptance_disclaimer()}\n"

def build_acceptance_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Acceptance Quality Report\n\n{build_acceptance_disclaimer()}\n\nPassed: {quality.get('passed', False) if quality else False}\n"

def build_acceptance_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Acceptance Status\n\n{build_acceptance_disclaimer()}\n\nTotal reports: {len(status_df) if status_df is not None else 0}\n"
