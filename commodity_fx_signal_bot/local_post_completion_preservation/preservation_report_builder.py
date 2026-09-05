import pandas as pd

def build_preservation_disclaimer() -> str:
    return "Bu cikti offline/local archive seal rehearsal ve post-completion preservation raporudur. Gercek immutable archive, official archive seal, production approval, canli emir, broker talimati, model deployment veya yatirim tavsiyesi degildir."

def build_preservation_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return "# Domain Registry\n" + build_preservation_disclaimer()
def build_archive_seal_rehearsal_markdown_report(summary: dict, packet_text: str | None = None) -> str:
    return "# Archive Seal\n" + build_preservation_disclaimer()
def build_immutable_readme_markdown_report(summary: dict, readme_text: str | None = None) -> str:
    return "# Immutable README\n" + build_preservation_disclaimer()
def build_evidence_vault_markdown_report(summary: dict, evidence_df: pd.DataFrame | None = None) -> str:
    return "# Evidence Vault\n" + build_preservation_disclaimer()
def build_knowledge_capsule_markdown_report(summary: dict, capsule_text: str | None = None) -> str:
    return "# Knowledge Capsule\n" + build_preservation_disclaimer()
def build_preservation_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    return "# Preservation Binder\n" + build_preservation_disclaimer()
def build_preservation_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return "# Preservation Quality\n" + build_preservation_disclaimer()
def build_preservation_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return "# Preservation Status\n" + build_preservation_disclaimer()
