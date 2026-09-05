import pandas as pd

def build_completion_disclaimer() -> str:
    return "Bu rapor offline/local closure synthesis ve completion governance rehearsal çıktısıdır; gerçek certification, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def build_completion_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Completion Domain Registry\n\n{build_completion_disclaimer()}"

def build_closure_synthesis_markdown_report(summary: dict, closure_text: str | None = None) -> str:
    return f"# Closure Synthesis\n\n{build_completion_disclaimer()}"

def build_end_state_certification_markdown_report(summary: dict, cert_text: str | None = None) -> str:
    return f"# End-State Certification\n\n{build_completion_disclaimer()}"

def build_project_freeze_markdown_report(summary: dict, freeze_text: str | None = None) -> str:
    return f"# Project Freeze\n\n{build_completion_disclaimer()}"

def build_acceptance_evidence_markdown_report(summary: dict, evidence_text: str | None = None) -> str:
    return f"# Acceptance Evidence\n\n{build_completion_disclaimer()}"

def build_completion_governance_markdown_report(summary: dict, governance_text: str | None = None) -> str:
    return f"# Completion Governance\n\n{build_completion_disclaimer()}"

def build_completion_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Completion Quality\n\n{build_completion_disclaimer()}"

def build_completion_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Completion Status\n\n{build_completion_disclaimer()}"\n