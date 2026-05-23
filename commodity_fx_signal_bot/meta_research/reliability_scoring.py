from typing import Dict, List

import pandas as pd

from meta_research.meta_models import ResearchEvidence
from meta_research.source_registry import EvidenceSourceDefinition


def calculate_source_reliability(evidence: ResearchEvidence, prior: float = 0.50) -> float:
    if evidence.evidence_direction == "missing_evidence":
        return 0.0

    reliability = prior

    if evidence.quality_score is not None:
        quality_adj = (evidence.quality_score - 0.5) * 0.2
        reliability += quality_adj

    if evidence.confidence_score is not None:
        confidence_adj = (evidence.confidence_score - 0.5) * 0.2
        reliability += confidence_adj

    if evidence.uncertainty_score is not None:
        reliability -= (evidence.uncertainty_score * 0.3)

    if evidence.warnings and len(evidence.warnings) > 0:
        reliability -= 0.1 * min(len(evidence.warnings), 3)

    return max(0.0, min(1.0, reliability))

def calculate_evidence_effective_weight(evidence: ResearchEvidence, source_weight: float, source_reliability: float) -> float:
    if evidence.evidence_direction == "missing_evidence" or evidence.normalized_score is None:
        return 0.0
    return source_weight * source_reliability

def build_source_reliability_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    sources: List[EvidenceSourceDefinition]
) -> pd.DataFrame:
    rows = []

    source_priors = {s.source_label: s.reliability_prior for s in sources}
    source_weights = {s.source_label: s.default_weight for s in sources}

    for symbol, ev_list in evidence_map.items():
        for ev in ev_list:
            prior = source_priors.get(ev.source_label, 0.50)
            weight = source_weights.get(ev.source_label, 0.0)

            rel = calculate_source_reliability(ev, prior)
            eff_weight = calculate_evidence_effective_weight(ev, weight, rel)

            rows.append({
                "symbol": symbol,
                "timeframe": ev.timeframe,
                "source_label": ev.source_label,
                "prior_reliability": prior,
                "calculated_reliability": rel,
                "base_weight": weight,
                "effective_weight": eff_weight,
                "missing": ev.evidence_direction == "missing_evidence"
            })

    if not rows:
        return pd.DataFrame()

    return pd.DataFrame(rows)

def summarize_source_reliability(reliability_df: pd.DataFrame) -> dict:
    if reliability_df.empty:
        return {"avg_reliability": 0.0, "sources": 0}

    avg_rel = reliability_df["calculated_reliability"].mean()
    zero_rel = (reliability_df["calculated_reliability"] == 0.0).sum()

    return {
        "avg_reliability": float(avg_rel),
        "zero_reliability_count": int(zero_rel),
        "total_evidence_rows": len(reliability_df)
    }
