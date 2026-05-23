from typing import List

import pandas as pd

from config.symbols import SymbolSpec
from meta_research.meta_models import (
    ConsensusResult,
    MetaResearchSnapshot,
    ResearchEvidence,
    clamp_meta_score,
)


def build_meta_research_snapshot(
    spec: SymbolSpec,
    timeframe: str,
    evidence_list: List[ResearchEvidence],
    consensus: ConsensusResult,
    ensemble_score: float | None,
    quality_adjusted_score: float | None
) -> MetaResearchSnapshot:

    if quality_adjusted_score is None:
        final_label = "unknown"
    elif quality_adjusted_score >= 0.70:
        final_label = "high_research_alignment"
    elif quality_adjusted_score >= 0.60:
        final_label = "moderate_research_alignment"
    elif quality_adjusted_score <= 0.30:
        final_label = "weak_research_alignment"
    elif quality_adjusted_score <= 0.40:
        final_label = "mixed_research_alignment"
    else:
        final_label = "neutral_research_alignment"

    return MetaResearchSnapshot(
        symbol=spec.symbol,
        timeframe=timeframe,
        asset_class=spec.asset_class,
        consensus=consensus,
        evidence=evidence_list,
        ensemble_score=clamp_meta_score(ensemble_score),
        quality_adjusted_score=clamp_meta_score(quality_adjusted_score),
        final_research_label=final_label,
        warnings=consensus.warnings.copy()
    )

def build_symbol_snapshot_table(snapshots: List[MetaResearchSnapshot]) -> pd.DataFrame:
    rows = []
    for s in snapshots:
        rows.append({
            "symbol": s.symbol,
            "timeframe": s.timeframe,
            "asset_class": s.asset_class,
            "consensus_score": s.consensus.consensus_score,
            "ensemble_score": s.ensemble_score,
            "quality_adjusted_score": s.quality_adjusted_score,
            "final_research_label": s.final_research_label
        })
    return pd.DataFrame(rows) if rows else pd.DataFrame()

def summarize_symbol_snapshot(snapshot: MetaResearchSnapshot) -> dict:
    return {
        "symbol": snapshot.symbol,
        "timeframe": snapshot.timeframe,
        "evidence_count": snapshot.consensus.evidence_count,
        "available_sources": snapshot.consensus.available_source_count,
        "final_label": snapshot.final_research_label
    }

def build_snapshot_narrative(snapshot: MetaResearchSnapshot) -> str:
    supportive = [e.source_label for e in snapshot.evidence if e.evidence_direction == "supportive_evidence"]
    conflicting = [e.source_label for e in snapshot.evidence if e.evidence_direction == "conflicting_evidence"]
    missing = [e.source_label for e in snapshot.evidence if e.evidence_direction == "missing_evidence"]

    lines = []
    lines.append(f"Meta Research Snapshot for {snapshot.symbol} ({snapshot.timeframe})")
    lines.append("-" * 50)
    lines.append(f"Consensus Score: {snapshot.consensus.consensus_score}")
    lines.append(f"Quality Adjusted Score: {snapshot.quality_adjusted_score}")
    lines.append(f"Research Alignment: {snapshot.final_research_label}")
    lines.append(f"Total Evaluated Sources: {snapshot.consensus.available_source_count}")
    lines.append("")
    lines.append("Key Supportive Sources:")
    lines.append(", ".join(supportive) if supportive else "None")
    lines.append("")
    lines.append("Key Conflicting Sources:")
    lines.append(", ".join(conflicting) if conflicting else "None")
    lines.append("")
    lines.append("Missing Sources:")
    lines.append(", ".join(missing) if missing else "None")
    lines.append("")
    if snapshot.warnings:
        lines.append("Warnings:")
        for w in snapshot.warnings:
            lines.append(f"- {w}")
    lines.append("")
    lines.append("DISCLAIMER: This narrative is a summary of offline meta-research. "
                 "It is not a live trading signal, order instruction, or investment advice.")

    return "\n".join(lines)
