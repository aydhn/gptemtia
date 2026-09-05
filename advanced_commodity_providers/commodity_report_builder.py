
import pandas as pd

def build_commodity_provider_disclaimer() -> str:
    return "Bu çıktı Phase 108 Commodities Data Provider Layer raporudur. Canlı emir, broker/futures broker talimatı, kesin AL/SAT, yatırım tavsiyesi, vadeli işlem tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek commodities provider API çağrısı zorunluluğu veya official approval değildir."

def build_commodity_provider_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame | None = None) -> str:
    return f"# Profile Registry\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_provider_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Domain Registry\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_universe_markdown_report(summary: dict, universe_df: pd.DataFrame | None = None) -> str:
    return f"# Commodity Universe\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_symbol_normalization_markdown_report(summary: dict, symbol_df: pd.DataFrame | None = None) -> str:
    return f"# Symbol Normalization\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_futures_contract_markdown_report(summary: dict, futures_df: pd.DataFrame | None = None) -> str:
    return f"# Futures Contract Metadata\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_roll_adjustment_markdown_report(summary: dict, roll_df: pd.DataFrame | None = None) -> str:
    return f"# Roll Adjustment\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_provider_capability_markdown_report(summary: dict, capability_df: pd.DataFrame | None = None) -> str:
    return f"# Capabilities\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_provider_registry_markdown_report(summary: dict, registry_df: pd.DataFrame | None = None) -> str:
    return f"# Provider Registry\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_contract_markdown_report(summary: dict, contract_df: pd.DataFrame | None = None) -> str:
    return f"# Adapter Contracts\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame | None = None) -> str:
    return f"# Dry-Run Fixture\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_safety_markdown_report(summary: dict, safety_df: pd.DataFrame | None = None) -> str:
    return f"# Safety Boundary\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_health_markdown_report(summary: dict, health_df: pd.DataFrame | None = None) -> str:
    return f"# Health Check\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Quality Report\n\n{build_commodity_provider_disclaimer()}\n"
def build_commodity_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Status Report\n\n{build_commodity_provider_disclaimer()}\n"
def build_phase_109_handoff_markdown_report(summary: dict, handoff_text: str | None = None) -> str:
    return f"# Phase 109 Handoff\n\n{build_commodity_provider_disclaimer()}\n"
