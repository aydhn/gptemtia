import pandas as pd

def build_runtime_disclaimer() -> str:
    return "> Bu çıktı Phase 102 advanced runtime consolidation raporudur. Canlı emir, broker talimatı, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı veya official approval değildir."

def _wrap(title, content):
    return f"# {title}\n\n{build_runtime_disclaimer()}\n\n{content}"

def build_runtime_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame | None = None) -> str:
    return _wrap("Runtime Profile Registry", profile_df.to_csv(index=False) if profile_df is not None else str(summary))
def build_unified_runtime_context_markdown_report(summary: dict, context_text: str | None = None) -> str:
    return _wrap("Unified Runtime Context", context_text if context_text else str(summary))
def build_runtime_capability_markdown_report(summary: dict, capability_df: pd.DataFrame | None = None) -> str:
    return _wrap("Runtime Capabilities", capability_df.to_csv(index=False) if capability_df is not None else str(summary))
def build_runtime_module_registry_markdown_report(summary: dict, module_df: pd.DataFrame | None = None) -> str:
    return _wrap("Runtime Modules", module_df.to_csv(index=False) if module_df is not None else str(summary))
def build_runtime_contracts_markdown_report(summary: dict, contract_df: pd.DataFrame | None = None) -> str:
    return _wrap("Runtime Contracts", contract_df.to_csv(index=False) if contract_df is not None else str(summary))
def build_runtime_health_markdown_report(summary: dict, health_df: pd.DataFrame | None = None) -> str:
    return _wrap("Runtime Health", health_df.to_csv(index=False) if health_df is not None else str(summary))
def build_runtime_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return _wrap("Runtime Quality", str(quality))
def build_runtime_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return _wrap("Runtime Status", status_df.to_csv(index=False) if status_df is not None else str(summary))
