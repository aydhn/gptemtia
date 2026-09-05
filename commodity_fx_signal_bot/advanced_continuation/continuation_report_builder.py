import pandas as pd

def build_advanced_continuation_disclaimer() -> str:
    return "Bu çıktı Phase 101 post-MVP advanced continuation raporudur. Canlı emir, broker talimatı, yatırım tavsiyesi, production deployment, model deployment, scraping veya official approval değildir."

def build_advanced_roadmap_markdown_report(summary: dict, roadmap_df: pd.DataFrame | None = None) -> str:
    return f"# Advanced Roadmap\n\n{build_advanced_continuation_disclaimer()}"
def build_phase_master_plan_markdown_report(summary: dict, plan_df: pd.DataFrame | None = None) -> str:
    return f"# Phase Master Plan\n\n{build_advanced_continuation_disclaimer()}"
def build_post_mvp_reopen_markdown_report(summary: dict, manifesto_text: str | None = None) -> str:
    return f"# Post MVP Reopen\n\n{manifesto_text}\n\n{build_advanced_continuation_disclaimer()}"
def build_phase_output_audit_markdown_report(summary: dict, audit_df: pd.DataFrame | None = None) -> str:
    return f"# Output Audit\n\n{build_advanced_continuation_disclaimer()}"
def build_mvp_gap_register_markdown_report(summary: dict, gap_df: pd.DataFrame | None = None) -> str:
    return f"# Gap Register\n\n{build_advanced_continuation_disclaimer()}"
def build_functional_continuation_markdown_report(summary: dict, continuation_df: pd.DataFrame | None = None) -> str:
    return f"# Functional Continuation\n\n{build_advanced_continuation_disclaimer()}"
def build_advanced_continuation_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Quality Report\n\n{build_advanced_continuation_disclaimer()}"
