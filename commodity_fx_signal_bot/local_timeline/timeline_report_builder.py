"""
Markdown report builder for local timeline.
"""

import pandas as pd

def build_timeline_disclaimer() -> str:
    return (
        "> **UYARI / YASAL BİLDİRİM**\n"
        "> Bu çıktı offline/local project timeline ve artifact evolution raporudur.\n"
        "> Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler,\n"
        "> cloud event service, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
    )

def build_project_event_registry_markdown_report(summary: dict, event_df: pd.DataFrame | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Project Event Registry\n\n"
    txt += f"Total Events: {summary.get('total_events', 0)}\n\n"
    if event_df is not None and not event_df.empty:
        txt += event_df.head(20).to_markdown() + "\n"
    return txt

def build_phase_chronology_markdown_report(summary: dict, phase_df: pd.DataFrame | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Phase Chronology Report\n\n"
    txt += f"Total Phases: {summary.get('total_phases', 0)}\n\n"
    if phase_df is not None and not phase_df.empty:
        txt += phase_df.to_markdown() + "\n"
    return txt

def build_artifact_evolution_markdown_report(summary: dict, evolution_df: pd.DataFrame | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Artifact Evolution Report\n\n"
    txt += f"Total Artifacts: {summary.get('total_artifacts', 0)}\n\n"
    if evolution_df is not None and not evolution_df.empty:
        txt += evolution_df.head(20).to_markdown() + "\n"
    return txt

def build_change_history_digest_markdown_report(summary: dict, digest_text: str | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Change History Digest\n\n"
    if digest_text:
        txt += digest_text + "\n"
    return txt

def build_timeline_query_markdown_report(summary: dict, results_df: pd.DataFrame | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Timeline Query Results\n\n"
    txt += f"Total Results: {summary.get('total_results', 0)}\n\n"
    if results_df is not None and not results_df.empty:
        txt += results_df.to_markdown() + "\n"
    return txt

def build_timeline_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Timeline Quality Report\n\n"
    if quality:
        for k, v in quality.items():
            txt += f"- **{k}**: {v}\n"
    return txt

def build_timeline_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    txt = build_timeline_disclaimer()
    txt += "# Timeline Status Report\n\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_markdown() + "\n"
    return txt
