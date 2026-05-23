from typing import Dict, List

import pandas as pd

from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import ResearchEvidence, clamp_meta_score
from meta_research.source_registry import EvidenceSourceDefinition
from meta_research.uncertainty_aggregation import (
    apply_uncertainty_penalty,
    calculate_aggregate_uncertainty,
)


def calculate_quality_penalty(evidence_list: List[ResearchEvidence]) -> float:
    if not evidence_list:
        return 0.5

    qual_scores = [e.quality_score for e in evidence_list if e.quality_score is not None]
    if not qual_scores:
        return 0.3

    avg_qual = sum(qual_scores) / len(qual_scores)
    if avg_qual < 0.6:
        return (0.6 - avg_qual) * 0.8
    return 0.0

def calculate_missing_source_penalty(
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> float:
    missing = sum(1 for e in evidence_list if e.evidence_direction == "missing_evidence")
    expected = sum(1 for s in sources if s.enabled)

    if expected == 0:
        return 0.0

    missing_ratio = missing / expected
    return min(0.4, missing_ratio * 0.5)

def apply_quality_adjustments(
    ensemble_score: float | None,
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> dict:

    if ensemble_score is None:
        return {
            "base_score": None,
            "uncertainty_penalty": 0.0,
            "quality_penalty": 0.0,
            "missing_source_penalty": 0.0,
            "conflict_penalty": 0.0,
            "quality_adjusted_score": None
        }

    unc = calculate_aggregate_uncertainty(evidence_list)

    adj_score_unc = apply_uncertainty_penalty(
        ensemble_score, unc, profile.uncertainty_penalty_enabled
    )
    if adj_score_unc is None:
        adj_score_unc = ensemble_score
    unc_penalty = abs(ensemble_score - adj_score_unc)

    qual_penalty = 0.0
    if profile.quality_penalty_enabled:
        qual_penalty = calculate_quality_penalty(evidence_list)

    missing_penalty = 0.0
    if profile.missing_source_penalty_enabled:
        missing_penalty = calculate_missing_source_penalty(evidence_list, sources, profile)

    current_dist = adj_score_unc - 0.5
    total_penalty_ratio = min(1.0, qual_penalty + missing_penalty)

    final_dist = current_dist * (1.0 - total_penalty_ratio)
    quality_adjusted_score = clamp_meta_score(0.5 + final_dist)

    return {
        "base_score": ensemble_score,
        "uncertainty_penalty": unc_penalty,
        "quality_penalty": qual_penalty,
        "missing_source_penalty": missing_penalty,
        "conflict_penalty": 0.0,
        "quality_adjusted_score": quality_adjusted_score
    }

def build_quality_adjustment_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> pd.DataFrame:
    from meta_research.consensus_engine import calculate_weighted_consensus_score

    rows = []
    for symbol, ev_list in evidence_map.items():
        metrics = calculate_weighted_consensus_score(ev_list, sources)
        adj = apply_quality_adjustments(metrics["consensus_score"], ev_list, sources, profile)
        adj["symbol"] = symbol
        rows.append(adj)

    return pd.DataFrame(rows) if rows else pd.DataFrame()
