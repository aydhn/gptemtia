from typing import Dict, List

import pandas as pd

from meta_research.consensus_engine import calculate_weighted_consensus_score
from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import ResearchEvidence
from meta_research.source_registry import EvidenceSourceDefinition


def calculate_model_factor_strategy_ensemble(
    evidence_list: List[ResearchEvidence],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> dict:

    scores = {
        "technical_score": None,
        "strategy_score": None,
        "risk_level_score": None,
        "backtest_score": None,
        "validation_score": None,
        "ml_score": None,
        "paper_score": None,
        "factor_score": None,
        "synthetic_index_score": None,
        "portfolio_score": None,
        "regime_score": None,
        "quality_score": None
    }

    for ev in evidence_list:
        if ev.normalized_score is not None:
            key = ev.source_label.replace("_evidence", "_score")
            if key in scores:
                scores[key] = ev.normalized_score

    metrics = calculate_weighted_consensus_score(evidence_list, sources)

    scores["ensemble_score"] = metrics["consensus_score"]
    return scores

def build_ensemble_score_table(
    evidence_map: Dict[str, List[ResearchEvidence]],
    sources: List[EvidenceSourceDefinition],
    profile: MetaResearchProfile
) -> pd.DataFrame:

    rows = []
    for symbol, ev_list in evidence_map.items():
        res = calculate_model_factor_strategy_ensemble(ev_list, sources, profile)
        res["symbol"] = symbol
        rows.append(res)

    return pd.DataFrame(rows) if rows else pd.DataFrame()

def summarize_ensemble_scores(ensemble_df: pd.DataFrame) -> dict:
    if ensemble_df.empty:
        return {"avg_ensemble_score": 0.0, "high_ensemble_count": 0}

    high_count = (ensemble_df["ensemble_score"] > 0.7).sum() if "ensemble_score" in ensemble_df else 0

    return {
        "avg_ensemble_score": float(ensemble_df["ensemble_score"].mean()) if "ensemble_score" in ensemble_df else 0.0,
        "high_ensemble_count": int(high_count)
    }
