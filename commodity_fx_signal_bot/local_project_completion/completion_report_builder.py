import pandas as pd

def build_completion_disclaimer() -> str:
    return "Bu çıktı offline/local system closure rehearsal ve project completion dossier raporudur. Gerçek project closure, official completion approval, production approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"

def build_completion_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return build_completion_disclaimer() + "# Completion Domain Registry\n\nOffline/local system closure rehearsal.\n"

def build_system_closure_dossier_markdown_report(summary: dict, dossier_text: str | None = None) -> str:
    return build_completion_disclaimer() + (dossier_text or "")

def build_terminal_handoff_pack_markdown_report(summary: dict, handoff_text: str | None = None) -> str:
    return build_completion_disclaimer() + (handoff_text or "")

def build_knowledge_freeze_markdown_report(summary: dict, freeze_df: pd.DataFrame | None = None) -> str:
    return build_completion_disclaimer() + "# Knowledge Freeze Rehearsal\n"

def build_last_mile_audit_markdown_report(summary: dict, audit_text: str | None = None) -> str:
    return build_completion_disclaimer() + (audit_text or "")

def build_project_completion_readiness_markdown_report(summary: dict, readiness_text: str | None = None) -> str:
    return build_completion_disclaimer() + (readiness_text or "")

def build_completion_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return build_completion_disclaimer() + "# Completion Quality\n"

def build_completion_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return build_completion_disclaimer() + "# Completion Status\n"
