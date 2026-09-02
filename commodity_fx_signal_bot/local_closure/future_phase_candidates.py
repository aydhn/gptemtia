
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_candidate_phase_from_roadmap_row(row: pd.Series, phase_number_hint: int, profile: LocalClosureProfile) -> dict:
    return {
        "candidate_phase": f"Phase {phase_number_hint}",
        "title": row["title"],
        "status": row["status"] if row["status"] != "roadmap_blocked_by_safety" else "manual_review_required",
        "description": row["rationale"]
    }

def build_future_phase_candidate_registry(roadmap_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    candidates = []
    if not roadmap_df.empty:
        valid_items = roadmap_df[roadmap_df["status"] != "roadmap_blocked_by_safety"]
        for idx, row in valid_items.iterrows():
            candidates.append(build_candidate_phase_from_roadmap_row(row, 81 + idx, profile))
    df = pd.DataFrame(candidates)
    summary = summarize_future_phase_candidates(df)
    return df, summary

def summarize_future_phase_candidates(candidate_df: pd.DataFrame) -> dict:
    return {
        "total_candidates": len(candidate_df)
    }
