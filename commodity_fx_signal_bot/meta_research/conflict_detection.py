from typing import Dict, List, Tuple

import pandas as pd

from meta_research.meta_config import MetaResearchProfile
from meta_research.meta_models import ResearchEvidence


def calculate_pairwise_evidence_disagreement(evidence_list: List[ResearchEvidence]) -> pd.DataFrame:
    rows = []
    valid_ev = [e for e in evidence_list if e.normalized_score is not None]

    for i, e1 in enumerate(valid_ev):
        for j, e2 in enumerate(valid_ev):
            if i < j:
                diff = abs(e1.normalized_score - e2.normalized_score)
                rows.append({
                    "source_1": e1.source_label,
                    "score_1": e1.normalized_score,
                    "source_2": e2.source_label,
                    "score_2": e2.normalized_score,
                    "disagreement": diff
                })

    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)

def calculate_conflict_score(evidence_list: List[ResearchEvidence]) -> float:
    df = calculate_pairwise_evidence_disagreement(evidence_list)
    if df.empty:
        return 0.0
    avg_diff = df["disagreement"].mean()
    return float(min(1.0, avg_diff * 1.5))

def identify_major_conflicts(evidence_list: List[ResearchEvidence], threshold: float = 0.35) -> List[dict]:
    df = calculate_pairwise_evidence_disagreement(evidence_list)
    conflicts = []
    if df.empty:
        return conflicts

    major = df[df["disagreement"] > threshold]
    for _, row in major.iterrows():
        conflicts.append({
            "source_1": row["source_1"],
            "source_2": row["source_2"],
            "disagreement": float(row["disagreement"])
        })
    return conflicts

def build_agreement_matrix(evidence_map: Dict[str, List[ResearchEvidence]]) -> pd.DataFrame:
    all_rows = []
    for symbol, ev_list in evidence_map.items():
        df = calculate_pairwise_evidence_disagreement(ev_list)
        if not df.empty:
            df["symbol"] = symbol
            all_rows.append(df)

    if not all_rows:
        return pd.DataFrame()

    combined = pd.concat(all_rows, ignore_index=True)
    matrix = combined.groupby(["source_1", "source_2"])["disagreement"].mean().reset_index()
    pivot = matrix.pivot(index="source_1", columns="source_2", values="disagreement")
    return pivot

def build_conflict_detection_report(
    evidence_map: Dict[str, List[ResearchEvidence]],
    profile: MetaResearchProfile
) -> Tuple[pd.DataFrame, dict]:

    rows = []
    total_conflicts = 0

    for symbol, ev_list in evidence_map.items():
        score = calculate_conflict_score(ev_list)
        major = identify_major_conflicts(ev_list, profile.conflict_threshold)

        total_conflicts += len(major)

        rows.append({
            "symbol": symbol,
            "conflict_score": score,
            "major_conflict_count": len(major),
            "has_critical_conflict": score > profile.conflict_threshold,
            "conflict_details": str([f"{c['source_1']} vs {c['source_2']}" for c in major]) if major else ""
        })

    df = pd.DataFrame(rows) if rows else pd.DataFrame()

    summary = {
        "symbols_analyzed": len(evidence_map),
        "total_major_conflicts": total_conflicts,
        "avg_conflict_score": float(df["conflict_score"].mean()) if not df.empty else 0.0
    }

    return df, summary
