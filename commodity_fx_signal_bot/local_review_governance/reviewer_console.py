from pathlib import Path
import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_reviewer_console_sections(profile: LocalReviewGovernanceProfile) -> list[dict]:
    return [
        {"title": "Console Warning", "content": "This is an offline reviewer console packet. No dashboard/GUI/TUI."},
        {"title": "Console Boards", "content": "Status, Warning, Manual Action boards available."},
        {"title": "Console Maps", "content": "Command map, output map available."}
    ]

def build_offline_reviewer_console_packet(project_root: Path, profile: LocalReviewGovernanceProfile) -> tuple[str, dict]:
    sections = build_reviewer_console_sections(profile)
    lines = ["# Offline Reviewer Console Packet\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_reviewer_console_packet(text)

def summarize_reviewer_console_packet(text: str) -> dict:
    return {"length": len(text)}

def build_offline_reviewer_console_index(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"index": 1, "item": "console_main"}])
    return df, summarize_reviewer_console_index(df)

def summarize_reviewer_console_index(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
