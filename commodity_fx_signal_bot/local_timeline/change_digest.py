"""
Change history digest module.
"""

import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def build_recent_change_summary(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> pd.DataFrame:
    if event_df.empty:
        return pd.DataFrame()

    # Sort by event_time_utc desc
    if 'event_time_utc' in event_df:
        recent = event_df.sort_values(by='event_time_utc', ascending=False).head(50)
        return recent
    return event_df.head(50)

def build_phase_change_digest(phase_df: pd.DataFrame, event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[str, dict]:
    if phase_df.empty:
        return "No phase events found.", {}

    lines = ["### Phase Based Activity"]
    for _, row in phase_df.iterrows():
        lines.append(f"- **{row.get('phase_title', 'Unknown Phase')}**: {row.get('event_count', 0)} events. Last seen: {row.get('last_seen_utc', 'N/A')}")

    return "\n".join(lines), {"lines": len(lines)}

def build_change_digest_sections(event_df: pd.DataFrame, evolution_df: pd.DataFrame, gap_df: pd.DataFrame) -> list[dict]:
    sections = []
    sections.append({
        "title": "General Project Timeline",
        "content": f"Total recorded events: {len(event_df)}"
    })

    if not gap_df.empty:
        sections.append({
            "title": "Stale or Missing Timeline Areas",
            "content": f"Found {len(gap_df)} gaps or stale artifacts requiring attention."
        })

    return sections

def build_change_history_digest(event_df: pd.DataFrame, evolution_df: pd.DataFrame, gap_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[str, dict]:
    lines = ["# Change History Digest\n"]
    lines.append("> **UYARI / YASAL BİLDİRİM**")
    lines.append("> Bu çıktı offline/local project timeline ve artifact evolution raporudur.")
    lines.append("> Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, ")
    lines.append("> otomatik trade onayı veya yatırım tavsiyesi değildir.\n")

    sections = build_change_digest_sections(event_df, evolution_df, gap_df)
    for sec in sections:
        lines.append(f"## {sec['title']}")
        lines.append(sec['content'])
        lines.append("")

    recent_df = build_recent_change_summary(event_df, profile)
    if not recent_df.empty:
        lines.append("## Most Recent Changes")
        for _, row in recent_df.head(10).iterrows():
            lines.append(f"- [{row.get('event_time_utc', 'N/A')}] {row.get('event_type', 'N/A')} on {row.get('relative_path', 'N/A')}")

    text = "\n".join(lines)
    summary = summarize_change_digest(text, recent_df)
    return text, summary

def summarize_change_digest(digest_text: str, recent_df: pd.DataFrame) -> dict:
    return {
        "text_length": len(digest_text),
        "recent_changes_count": len(recent_df)
    }
