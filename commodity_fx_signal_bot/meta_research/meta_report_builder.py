from typing import Dict

import pandas as pd

from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import MetaResearchSnapshot
from meta_research.meta_snapshot import build_snapshot_narrative


def build_meta_disclaimer() -> str:
    return (
        "*** DISCLAIMER ***\n"
        "Bu çıktı offline meta-research/kanıt ağırlıklandırma raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, otomatik trade onayı veya "
        "yatırım tavsiyesi değildir. Yalnızca offline araştırma kanıtlarını birleştirir."
    )

def _build_generic_markdown(title: str, summary: dict, df: pd.DataFrame | None, profile: MetaResearchProfile) -> str:
    lines = [
        f"# {title}",
        "",
        "## Configuration",
        f"- Profile: {profile.name}",
        f"- Timeframe: {summary.get('timeframe', 'Unknown')}",
        ""
    ]

    lines.append("## Summary")
    for k, v in summary.items():
        if k != "timeframe":
            lines.append(f"- {k}: {v}")
    lines.append("")

    if df is not None and not df.empty:
        lines.append("## Data Table")
        if len(df) > 50:
            lines.append("*(Showing top 50 rows)*")
            lines.append(df.head(50).to_markdown(index=False))
        else:
            lines.append(df.to_markdown(index=False))
        lines.append("")

    lines.append(build_meta_disclaimer())
    return "\n".join(lines)

def build_meta_research_markdown_report(summary: dict, tables: Dict[str, pd.DataFrame], profile: MetaResearchProfile) -> str:
    df = tables.get("consensus", None)
    return _build_generic_markdown("Meta Research Report", summary, df, profile)

def build_meta_consensus_markdown_report(summary: dict, consensus_df: pd.DataFrame, profile: MetaResearchProfile) -> str:
    return _build_generic_markdown("Meta Consensus Report", summary, consensus_df, profile)

def build_evidence_conflict_markdown_report(summary: dict, conflict_df: pd.DataFrame, profile: MetaResearchProfile) -> str:
    return _build_generic_markdown("Evidence Conflict Report", summary, conflict_df, profile)

def build_quality_adjusted_ranking_markdown_report(summary: dict, ranking_df: pd.DataFrame, profile: MetaResearchProfile) -> str:
    return _build_generic_markdown("Quality Adjusted Ranking Report", summary, ranking_df, profile)

def build_meta_symbol_snapshot_markdown(snapshot: MetaResearchSnapshot, profile: MetaResearchProfile) -> str:
    narrative = build_snapshot_narrative(snapshot)

    lines = [
        f"# Meta Research Snapshot: {snapshot.symbol}",
        f"**Timeframe**: {snapshot.timeframe}",
        f"**Profile**: {profile.name}",
        "",
        "## Narrative Summary",
        narrative,
        "",
        build_meta_disclaimer()
    ]
    return "\n".join(lines)
