import pandas as pd

def build_fx_provider_disclaimer() -> str:
    return "Bu çıktı Phase 107 FX Data Provider Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek FX provider API çağrısı zorunluluğu veya official approval değildir."

def build_fx_provider_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame = None) -> str: return f"# Profile Registry\n\n{build_fx_provider_disclaimer()}"
def build_fx_provider_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame = None) -> str: return f"# Domain Registry\n\n{build_fx_provider_disclaimer()}"
def build_fx_pair_universe_markdown_report(summary: dict, pair_df: pd.DataFrame = None) -> str: return f"# Pair Universe\n\n{build_fx_provider_disclaimer()}"
def build_fx_symbol_normalization_markdown_report(summary: dict, symbol_df: pd.DataFrame = None) -> str: return f"# Symbol Normalization\n\n{build_fx_provider_disclaimer()}"
def build_fx_provider_capability_markdown_report(summary: dict, capability_df: pd.DataFrame = None) -> str: return f"# Capabilities\n\n{build_fx_provider_disclaimer()}"
def build_fx_provider_registry_markdown_report(summary: dict, registry_df: pd.DataFrame = None) -> str: return f"# Provider Registry\n\n{build_fx_provider_disclaimer()}"
def build_fx_contract_markdown_report(summary: dict, contract_df: pd.DataFrame = None) -> str: return f"# Contracts\n\n{build_fx_provider_disclaimer()}"
def build_fx_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame = None) -> str: return f"# Dry Run\n\n{build_fx_provider_disclaimer()}"
def build_fx_safety_markdown_report(summary: dict, safety_df: pd.DataFrame = None) -> str: return f"# Safety Boundary\n\n{build_fx_provider_disclaimer()}"
def build_fx_health_markdown_report(summary: dict, health_df: pd.DataFrame = None) -> str: return f"# Health Check\n\n{build_fx_provider_disclaimer()}"
def build_fx_quality_markdown_report(summary: dict, quality: dict = None) -> str: return f"# Quality Report\n\n{build_fx_provider_disclaimer()}"
def build_fx_status_markdown_report(summary: dict, status_df: pd.DataFrame = None) -> str: return f"# Status\n\n{build_fx_provider_disclaimer()}"
def build_phase_108_handoff_markdown_report(summary: dict, handoff_text: str = None) -> str: return f"# Phase 108 Handoff\n\n{build_fx_provider_disclaimer()}"
