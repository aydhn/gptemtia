from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_milestone_table(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    milestones = [
        ("core research platform", "offline_ready"),
        ("reporting and DataLake", "offline_ready"),
        ("safety and governance", "offline_ready"),
        ("metadata/evidence", "offline_ready"),
        ("graph/timeline/consistency", "offline_ready"),
        ("readiness/maintenance/archive/DR", "offline_ready"),
        ("training/briefing", "offline_ready")
    ]
    df = pd.DataFrame(milestones, columns=["milestone_group", "status"])
    return df, summarize_milestone_narrative("", df)

def build_milestone_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_milestone_table(project_root, profile)
    text = "# Milestone Narrative\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    for _, row in df.iterrows():
        text += f"- **{row['milestone_group']}**: {row['status']} (Manual review required)\n"
    return text, summary

def summarize_milestone_narrative(text: str, milestone_df: pd.DataFrame) -> dict:
    if milestone_df is None or milestone_df.empty:
        return {"total_milestones": 0}
    return {"total_milestones": len(milestone_df)}
