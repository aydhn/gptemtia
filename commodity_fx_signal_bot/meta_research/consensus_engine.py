from typing import Dict, List

import pandas as pd

from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import ConsensusResult, ResearchEvidence, clamp_meta_score
from meta_research.reliability_scoring import (
    calculate_evidence_effective_weight,
    calculate_source_reliability,
)
from meta_research.source_registry import EvidenceSourceDefinition


def calculate_weighted_consensus_score(
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition]
) -> dict:

    source_priors = {s.source_label: s.reliability_prior for s in sources}
    source_weights = {s.source_label: s.default_weight for s in sources}

    total_effective_weight = 0.0
    weighted_score_sum = 0.0

    supportive = 0
    conflicting = 0
    neutral = 0
    missing = 0

    for ev in evidence_list:
        if ev.evidence_direction == "missing_evidence" or ev.normalized_score is None:
            missing += 1
            continue

        prior = source_priors.get(ev.source_label, 0.50)
        weight = source_weights.get(ev.source_label, 0.0)

        rel = calculate_source_reliability(ev, prior)
        eff_weight = calculate_evidence_effective_weight(ev, weight, rel)

        total_effective_weight += eff_weight
        weighted_score_sum += (ev.normalized_score * eff_weight)

        if ev.evidence_direction == "supportive_evidence":
            supportive += 1
        elif ev.evidence_direction == "conflicting_evidence":
            conflicting += 1
        else:
            neutral += 1

    if total_effective_weight > 0:
        consensus_score = weighted_score_sum / total_effective_weight
    else:
        consensus_score = None

    return {
        "consensus_score": clamp_meta_score(consensus_score),
        "total_effective_weight": total_effective_weight,
        "supportive_count": supportive,
        "conflicting_count": conflicting,
        "neutral_count": neutral,
        "missing_count": missing,
        "available_source_count": supportive + conflicting + neutral
    }

def infer_consensus_label(
    consensus_score: float | None,
    conflict_score: float | None,
    available_source_count: int,
    profile: MetaResearchProfile
) -> str:

    if consensus_score is None or available_source_count < profile.min_sources:
        return "insufficient_consensus_data"

    if conflict_score is not None and conflict_score > profile.conflict_threshold:
        return "mixed_consensus"

    if consensus_score >= profile.high_agreement_threshold:
        return "strong_positive_consensus"
    elif consensus_score >= 0.60:
        return "moderate_positive_consensus"
    elif consensus_score <= (1.0 - profile.high_agreement_threshold):
        return "strong_negative_consensus"
    elif consensus_score <= 0.40:
        return "moderate_negative_consensus"
    else:
        return "neutral_consensus"

def infer_confidence_label(confidence_score: float | None) -> str:
    if confidence_score is None:
        return "unknown_confidence"
    if confidence_score >= 0.70:
        return "high_confidence_research"
    elif confidence_score >= 0.40:
        return "medium_confidence_research"
    elif confidence_score >= 0.20:
        return "low_confidence_research"
    else:
        return "unreliable_research"

def build_consensus_result(
    symbol: str,
    timeframe: str,
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> ConsensusResult:

    metrics = calculate_weighted_consensus_score(evidence_list, sources)

    conf_scores = [e.confidence_score for e in evidence_list if e.confidence_score is not None]
    agg_conf = sum(conf_scores) / len(conf_scores) if conf_scores else None

    unc_scores = [e.uncertainty_score for e in evidence_list if e.uncertainty_score is not None]
    agg_unc = sum(unc_scores) / len(unc_scores) if unc_scores else None

    total_active = metrics["supportive_count"] + metrics["conflicting_count"]
    if total_active > 0:
        minority = min(metrics["supportive_count"], metrics["conflicting_count"])
        conflict_score = minority / total_active
    else:
        conflict_score = 0.0

    cons_label = infer_consensus_label(
        metrics["consensus_score"],
        conflict_score,
        metrics["available_source_count"],
        profile
    )

    conf_label = infer_confidence_label(agg_conf)

    warnings = []
    if metrics["available_source_count"] < profile.min_sources:
        warnings.append(f"Available sources ({metrics['available_source_count']}) below minimum ({profile.min_sources})")

    return ConsensusResult(
        symbol=symbol,
        timeframe=timeframe,
        evidence_count=len(evidence_list),
        available_source_count=metrics["available_source_count"],
        consensus_score=metrics["consensus_score"],
        confidence_score=clamp_meta_score(agg_conf),
        uncertainty_score=clamp_meta_score(agg_unc),
        conflict_score=clamp_meta_score(conflict_score),
        consensus_label=cons_label,
        confidence_label=conf_label,
        supportive_count=metrics["supportive_count"],
        conflicting_count=metrics["conflicting_count"],
        neutral_count=metrics["neutral_count"],
        missing_count=metrics["missing_count"],
        warnings=warnings
    )

def build_consensus_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    timeframe: str,
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> pd.DataFrame:

    rows = []
    for symbol, ev_list in evidence_map.items():
        res = build_consensus_result(symbol, timeframe, ev_list, sources, profile)
        rows.append({
            "symbol": res.symbol,
            "timeframe": res.timeframe,
            "consensus_score": res.consensus_score,
            "confidence_score": res.confidence_score,
            "conflict_score": res.conflict_score,
            "consensus_label": res.consensus_label,
            "confidence_label": res.confidence_label,
            "available_sources": res.available_source_count,
            "supportive": res.supportive_count,
            "conflicting": res.conflicting_count,
            "warning_count": len(res.warnings)
        })

    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)
