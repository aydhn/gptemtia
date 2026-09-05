import pandas as pd

def build_packaging_disclaimer() -> str:
    return "Bu rapor offline/local distribution bundle rehearsal ve packaging governance ciktisidir; gercek ZIP/archive, package publish, deployment, official handover, legal/compliance approval, production approval, canli sinyal, broker talimati, model deployment veya yatirim tavsiyesi degildir."

def build_packaging_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Packaging Domain Registry\n\n{build_packaging_disclaimer()}"

def build_distribution_bundle_markdown_report(summary: dict, bundle_text: str | None = None) -> str:
    return f"# Distribution Bundle\n\n{build_packaging_disclaimer()}\n\n{bundle_text or ''}"

def build_portable_docs_bundle_markdown_report(summary: dict, portable_text: str | None = None) -> str:
    return f"# Portable Docs Bundle\n\n{build_packaging_disclaimer()}\n\n{portable_text or ''}"

def build_release_folder_manifest_markdown_report(summary: dict, folder_text: str | None = None) -> str:
    return f"# Release Folder Manifest\n\n{build_packaging_disclaimer()}\n\n{folder_text or ''}"

def build_handover_zip_map_markdown_report(summary: dict, zip_text: str | None = None) -> str:
    return f"# Handover ZIP-Map\n\n{build_packaging_disclaimer()}\n\n{zip_text or ''}"

def build_packaging_governance_markdown_report(summary: dict, governance_text: str | None = None) -> str:
    return f"# Packaging Governance\n\n{build_packaging_disclaimer()}\n\n{governance_text or ''}"

def build_packaging_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Packaging Quality Report\n\n{build_packaging_disclaimer()}"

def build_packaging_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Packaging Status\n\n{build_packaging_disclaimer()}"
