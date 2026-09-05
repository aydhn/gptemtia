import pandas as pd

DISCLAIMER = "Bu çıktı Phase 106 Multi-Provider Data Abstraction raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu veya official approval değildir."

def build_provider_disclaimer() -> str:
    return DISCLAIMER

def build_provider_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame | None = None) -> str: return f"# Profile Registry\n\n{DISCLAIMER}\n"
def build_provider_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str: return f"# Domain Registry\n\n{DISCLAIMER}\n"
def build_provider_type_registry_markdown_report(summary: dict, type_df: pd.DataFrame | None = None) -> str: return f"# Type Registry\n\n{DISCLAIMER}\n"
def build_provider_capability_markdown_report(summary: dict, capability_df: pd.DataFrame | None = None) -> str: return f"# Capability Registry\n\n{DISCLAIMER}\n"
def build_provider_registry_markdown_report(summary: dict, registry_df: pd.DataFrame | None = None) -> str: return f"# Provider Registry\n\n{DISCLAIMER}\n"
def build_provider_contract_markdown_report(summary: dict, contract_df: pd.DataFrame | None = None) -> str: return f"# Provider Contract\n\n{DISCLAIMER}\n"
def build_provider_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame | None = None) -> str: return f"# Dry Run Fixture\n\n{DISCLAIMER}\n"
def build_provider_safety_markdown_report(summary: dict, safety_df: pd.DataFrame | None = None) -> str: return f"# Safety Boundary\n\n{DISCLAIMER}\n"
def build_provider_health_markdown_report(summary: dict, health_df: pd.DataFrame | None = None) -> str: return f"# Health Check\n\n{DISCLAIMER}\n"
def build_provider_quality_markdown_report(summary: dict, quality: dict | None = None) -> str: return f"# Quality Report\n\n{DISCLAIMER}\n"
def build_provider_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str: return f"# Provider Status\n\n{DISCLAIMER}\n"
def build_phase_107_handoff_markdown_report(summary: dict, handoff_text: str | None = None) -> str: return f"# Phase 107 Handoff\n\n{DISCLAIMER}\n"
