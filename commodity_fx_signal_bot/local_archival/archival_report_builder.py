"""
Archival Report Builder.
"""
import pandas as pd

def build_archival_disclaimer() -> str:
    return "Bu rapor offline/local archival seal rehearsal ve provenance documentation çıktısıdır; gerçek immutable archive, cloud archive, blockchain notarization, legal hold, compliance sertifikası, canlı sinyal, broker talimatı, model deployment, production release veya yatırım tavsiyesi değildir."

def build_archival_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Archival Domain Registry\n\n{build_archival_disclaimer()}\n"

def build_final_archival_seal_rehearsal_markdown_report(summary: dict, manifest: dict | None = None) -> str:
    return f"# Final Archival Seal Rehearsal\n\n{build_archival_disclaimer()}\n"

def build_provenance_lockfile_markdown_report(summary: dict, lockfile: dict | None = None) -> str:
    return f"# Provenance Lockfile\n\n{build_archival_disclaimer()}\n"

def build_hash_catalogs_markdown_report(summary: dict, hash_df: pd.DataFrame | None = None) -> str:
    return f"# Hash Catalogs\n\n{build_archival_disclaimer()}\n"

def build_custody_rehearsal_markdown_report(summary: dict, guide_text: str | None = None) -> str:
    return f"# Custody Rehearsal\n\n{build_archival_disclaimer()}\n"

def build_archival_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Archival Quality\n\n{build_archival_disclaimer()}\n"

def build_archival_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Archival Status\n\n{build_archival_disclaimer()}\n"
