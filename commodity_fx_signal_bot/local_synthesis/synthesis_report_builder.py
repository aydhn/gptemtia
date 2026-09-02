import pandas as pd
from typing import Dict, Optional

def build_synthesis_disclaimer() -> str:
    return "Bu rapor offline/local final synthesis ve end-state documentation çıktısıdır; yatırım tavsiyesi, canlı sinyal, broker talimatı, model deployment, production release, resmi compliance onayı veya resmi proje kapanış sertifikası değildir."

def build_synthesis_profile_markdown_report(summary: Dict, profile_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Synthesis Profile Report\n\n{build_synthesis_disclaimer()}"

def build_master_index_markdown_report(summary: Dict, index_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Master Index Report\n\n{build_synthesis_disclaimer()}"

def build_cross_phase_final_map_markdown_report(summary: Dict, map_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Cross Phase Final Map Report\n\n{build_synthesis_disclaimer()}"

def build_project_completion_dossier_markdown_report(summary: Dict, dossier_text: Optional[str] = None) -> str:
    return f"# Project Completion Dossier Report\n\n{build_synthesis_disclaimer()}"

def build_end_state_documentation_markdown_report(summary: Dict, catalog_df: Optional[pd.DataFrame] = None) -> str:
    return f"# End State Documentation Report\n\n{build_synthesis_disclaimer()}"

def build_synthesis_quality_markdown_report(summary: Dict, quality: Optional[Dict] = None) -> str:
    return f"# Synthesis Quality Report\n\n{build_synthesis_disclaimer()}"

def build_synthesis_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Synthesis Status Report\n\n{build_synthesis_disclaimer()}"
