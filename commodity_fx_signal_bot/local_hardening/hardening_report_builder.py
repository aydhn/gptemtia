
import pandas as pd

def build_hardening_disclaimer() -> str:
    return "Bu cikti offline/local final hardening ve release-candidate dry-run freeze raporudur. Production release, gercek release candidate, package publish, canli emir, broker talimati, model deployment, resmi compliance onayi veya yatirim tavsiyesi degildir."

def build_hardening_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str: return build_hardening_disclaimer() + "\n\n# Domains"
def build_dead_code_review_markdown_report(summary: dict, candidate_df: pd.DataFrame | None = None) -> str: return build_hardening_disclaimer() + "\n\n# Dead Code"
def build_contract_freeze_markdown_report(summary: dict, contract_df: pd.DataFrame | None = None) -> str: return build_hardening_disclaimer() + "\n\n# Contracts"
def build_documentation_freeze_markdown_report(summary: dict, doc_df: pd.DataFrame | None = None) -> str: return build_hardening_disclaimer() + "\n\n# Docs Freeze"
def build_rc_dry_run_freeze_markdown_report(summary: dict, manifest: dict | None = None) -> str: return build_hardening_disclaimer() + "\n\n# RC Freeze"
def build_freeze_quality_markdown_report(summary: dict, quality: dict | None = None) -> str: return build_hardening_disclaimer() + "\n\n# Quality"
def build_freeze_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str: return build_hardening_disclaimer() + "\n\n# Status"
