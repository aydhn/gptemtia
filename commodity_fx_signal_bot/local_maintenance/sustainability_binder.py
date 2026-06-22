import pandas as pd
from typing import Tuple, Dict, Any, List
from pathlib import Path
from datetime import datetime, timezone

from local_maintenance.maintenance_config import LocalMaintenanceProfile
from local_maintenance.sustainability_scoring import calculate_sustainability_score, classify_sustainability_score

def build_sustainability_binder_sections(
    domain_df: pd.DataFrame,
    task_df: pd.DataFrame,
    calendar_df: pd.DataFrame,
    score_df: pd.DataFrame,
    risk_df: pd.DataFrame
) -> List[Dict[str, str]]:

    score = score_df.iloc[0]["value"] if score_df is not None and not score_df.empty else 0.0
    classification = score_df.iloc[0]["classification"] if score_df is not None and not score_df.empty else "Unknown"

    sections = [
        {
            "title": "Binder Overview",
            "content": "This document outlines the long-term sustainability plan for the offline research project."
        },
        {
            "title": "Current Sustainability Score",
            "content": f"- Score: {score:.2f}\n- Status: {classification}"
        },
        {
            "title": "Maintenance Domains",
            "content": f"The project contains {len(domain_df) if domain_df is not None else 0} maintenance domains."
        },
        {
            "title": "Scheduled Tasks (Manual)",
            "content": f"There are {len(task_df) if task_df is not None else 0} tasks defined for periodic manual review."
        },
        {
            "title": "Identified Risks",
            "content": f"There are {len(risk_df) if risk_df is not None else 0} sustainability risks currently tracked."
        },
        {
            "title": "Disclaimers",
            "content": "This binder is a manual offline sustainability document. It is not a production SLA, official maintenance contract, or investment advice."
        }
    ]
    return sections

def build_long_term_sustainability_binder(
    domain_df: pd.DataFrame,
    task_df: pd.DataFrame,
    calendar_df: pd.DataFrame,
    score_df: pd.DataFrame,
    risk_df: pd.DataFrame,
    profile: LocalMaintenanceProfile
) -> Tuple[str, Dict[str, Any]]:

    sections = build_sustainability_binder_sections(domain_df, task_df, calendar_df, score_df, risk_df)

    lines = [f"# Long-Term Sustainability Binder (Profile: {profile.name})\n"]
    lines.append(f"*Generated: {datetime.now(timezone.utc).isoformat()}*\n")

    for sec in sections:
        lines.append(f"## {sec['title']}")
        lines.append(sec['content'])
        lines.append("")

    content = "\n".join(lines)
    summary = summarize_sustainability_binder(content)
    return content, summary

def summarize_sustainability_binder(binder_text: str) -> Dict[str, Any]:
    return {
        "text_length": len(binder_text),
        "disclaimer": "This binder is not an official maintenance contract."
    }

def save_sustainability_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
