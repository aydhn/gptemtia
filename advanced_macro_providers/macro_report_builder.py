
import pandas as pd

def build_macro_provider_disclaimer() -> str:
    return "Bu çıktı Phase 109 Macro Data Provider Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, yönlü makro kesinlik iddiası, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek macro provider API çağrısı zorunluluğu veya official approval değildir."

def _wrap_disclaimer(content: str) -> str:
    return content + "\n\n" + build_macro_provider_disclaimer()

def build_macro_provider_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Provider Profile Registry")
def build_macro_provider_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Provider Domain Registry")
def build_macro_indicator_universe_markdown_report(summary: dict, indicator_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Indicator Universe")
def build_macro_region_metadata_markdown_report(summary: dict, region_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Region Metadata")
def build_macro_symbol_normalization_markdown_report(summary: dict, symbol_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Symbol Normalization")
def build_macro_timeseries_schema_markdown_report(summary: dict, schema_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Timeseries Schema")
def build_macro_release_metadata_markdown_report(summary: dict, release_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Release Metadata")
def build_macro_revision_policy_markdown_report(summary: dict, revision_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Revision Policy")
def build_macro_provider_capability_markdown_report(summary: dict, capability_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Provider Capabilities")
def build_macro_provider_registry_markdown_report(summary: dict, registry_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Provider Registry")
def build_macro_contract_markdown_report(summary: dict, contract_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Contract")
def build_macro_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Dry Run")
def build_macro_safety_markdown_report(summary: dict, safety_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Safety")
def build_macro_health_markdown_report(summary: dict, health_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Health")
def build_macro_quality_markdown_report(summary: dict, quality: dict | None = None) -> str: return _wrap_disclaimer("# Macro Quality")
def build_macro_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str: return _wrap_disclaimer("# Macro Status")
def build_phase_110_handoff_markdown_report(summary: dict, handoff_text: str | None = None) -> str: return _wrap_disclaimer("# Phase 110 Handoff")
