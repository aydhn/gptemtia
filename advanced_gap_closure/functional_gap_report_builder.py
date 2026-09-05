import pandas as pd

def build_gap_closure_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame | None = None) -> str: return "# Profile Registry\n" + build_functional_gap_disclaimer()
def build_readiness_reconciliation_markdown_report(summary: dict, reconciliation_df: pd.DataFrame | None = None) -> str: return "# Readiness\n"
def build_mvp_to_v2_closure_matrix_markdown_report(summary: dict, closure_df: pd.DataFrame | None = None) -> str: return "# Closure Matrix\n"
def build_foundation_audit_markdown_report(summary: dict, audit_df: pd.DataFrame | None = None) -> str: return "# Audit\n"
def build_missing_functionality_markdown_report(summary: dict, missing_df: pd.DataFrame | None = None) -> str: return "# Missing\n"
def build_phase_106_handoff_markdown_report(summary: dict, handoff_text: str | None = None) -> str: return "# Handoff\n"
def build_data_provider_requirements_markdown_report(summary: dict, requirements_df: pd.DataFrame | None = None) -> str: return "# Requirements\n"
def build_no_scraping_boundary_markdown_report(summary: dict, boundary_df: pd.DataFrame | None = None) -> str: return "# Boundary\n"
def build_functional_gap_quality_markdown_report(summary: dict, quality: dict | None = None) -> str: return "# Quality\n"
def build_functional_gap_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str: return "# Status\n"

def build_functional_gap_disclaimer() -> str:
    return "Bu çıktı Phase 105 Functional Gap Closure Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı veya official approval değildir."
