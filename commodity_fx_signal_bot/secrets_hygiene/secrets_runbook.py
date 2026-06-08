
from pathlib import Path
import pandas as pd
from typing import Tuple
from secrets_hygiene.secrets_config import SecretsHygieneProfile

def build_secret_incident_manual_review_section(findings_df: pd.DataFrame) -> str: return "### Incident Manual Review\nIf you find a real secret, manually rotate it at the provider and scrub from git history if pushed."

def build_secret_hygiene_runbook_sections(findings_df: pd.DataFrame, recommendations_df: pd.DataFrame) -> list[dict]:
    return [
        {"title": "Purpose and Scope", "content": "This runbook handles local secret hygiene."},
        {"title": "Secret Values Not Reported", "content": "Raw secret values are never printed."},
        {"title": ".env vs .env.example", "content": "Never commit .env. Always use placeholders in .env.example."},
        {"title": "Manual Action", "content": build_secret_incident_manual_review_section(findings_df)}
    ]

def build_secret_hygiene_runbook(findings_df: pd.DataFrame, recommendations_df: pd.DataFrame, profile: SecretsHygieneProfile) -> Tuple[str, dict]:
    sections = build_secret_hygiene_runbook_sections(findings_df, recommendations_df)
    text = "# Secrets Hygiene Runbook\n\n"
    for s in sections: text += f"## {s['title']}\n{s['content']}\n\n"
    return text, {"sections_generated": len(sections)}

def save_secret_hygiene_runbook(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f: f.write(text)
    return output_path
