from typing import Dict, List

import pandas as pd

from meta_research.meta_models import ResearchEvidence, clamp_meta_score


def calculate_evidence_uncertainty(evidence: ResearchEvidence) -> float:
    base_unc = evidence.uncertainty_score if evidence.uncertainty_score is not None else 0.5

    if evidence.quality_score is not None and evidence.quality_score < 0.4:
        base_unc += 0.2

    if evidence.evidence_direction == "missing_evidence":
        base_unc = 1.0

    return clamp_meta_score(base_unc)

def calculate_aggregate_uncertainty(evidence_list: List[ResearchEvidence]) -> float:
    if not evidence_list:
        return 1.0

    unc_scores = [calculate_evidence_uncertainty(e) for e in evidence_list]
    avg_unc = sum(unc_scores) / len(unc_scores)

    missing = sum(1 for e in evidence_list if e.evidence_direction == "missing_evidence")
    missing_ratio = missing / len(evidence_list)

    final_unc = avg_unc + (missing_ratio * 0.5)

    return clamp_meta_score(final_unc)

def apply_uncertainty_penalty(score: float | None, uncertainty: float | None, enabled: bool = True) -> float | None:
    if score is None:
        return None
    if not enabled or uncertainty is None or uncertainty <= 0.2:
        return score

    dist_to_neutral = score - 0.5
    penalty_factor = 1.0 - (uncertainty * 0.5)

    adjusted = 0.5 + (dist_to_neutral * penalty_factor)
    return clamp_meta_score(adjusted)

def build_uncertainty_penalty_table(evidence_map: Dict[str, List[ResearchEvidence]]) -> pd.DataFrame:
    rows = []
    for symbol, ev_list in evidence_map.items():
        unc = calculate_aggregate_uncertainty(ev_list)
        missing_count = sum(1 for e in ev_list if e.evidence_direction == "missing_evidence")

        rows.append({
            "symbol": symbol,
            "aggregate_uncertainty": unc,
            "missing_source_count": missing_count,
            "high_uncertainty": unc > 0.6
        })

    return pd.DataFrame(rows) if rows else pd.DataFrame()

def summarize_uncertainty(uncertainty_df: pd.DataFrame) -> dict:
    if uncertainty_df.empty:
        return {"avg_uncertainty": 0.0, "high_uncertainty_symbols": 0}

    return {
        "avg_uncertainty": float(uncertainty_df["aggregate_uncertainty"].mean()),
        "high_uncertainty_symbols": int(uncertainty_df["high_uncertainty"].sum())
    }
