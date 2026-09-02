from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_phase_evolution_table(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    phases = [
        ("Phases 1-10", "Core foundation and data lake"),
        ("Phases 11-20", "Model training and backtesting pipelines"),
        ("Phases 21-30", "Governance, evidence, and security"),
        ("Phases 31-40", "Knowledge graph, timeline, readiness"),
        ("Phases 41-50", "Maintenance, archive, DR"),
        ("Phases 51-60", "ML enhancements, observability"),
        ("Phases 61-70", "Advanced training, scenario regression, synthesis"),
        ("Phases 71-74", "Training kits, Briefing, Communication")
    ]
    df = pd.DataFrame(phases, columns=["phase_group", "description"])
    return df, {"total_phases": len(df)}

def build_phase_evolution_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_phase_evolution_table(project_root, profile)
    text = "# Phase Evolution Narrative\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    for _, row in df.iterrows():
        text += f"- **{row['phase_group']}**: {row['description']}\n"
    
    text += "\n*Not: Bu evrim canli sistem tamamlandi iddiasi tasimaz.*"
    return text, summary

def summarize_phase_evolution_narrative(text: str, phase_df: pd.DataFrame) -> dict:
    if phase_df is None or phase_df.empty:
        return {"total_phases": 0}
    return {"total_phases": len(phase_df)}
