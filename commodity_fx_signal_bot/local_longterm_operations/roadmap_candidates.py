"""Roadmap candidates."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile
from .longterm_models import RoadmapCandidate, build_roadmap_candidate_id, roadmap_candidate_to_dict

def build_default_v1x_roadmap_candidates(profile: LocalLongTermOperationsProfile) -> list[RoadmapCandidate]:
    return [
        RoadmapCandidate(
            roadmap_id=build_roadmap_candidate_id("feature_x", "core"),
            roadmap_name="feature_x",
            roadmap_area="core",
            priority_hint="low",
            expected_benefit="none",
            risk_note="low",
            manual_review_required=True,
            warnings=["Implementation commitment değildir."]
        )
    ]

def build_v1x_roadmap_candidate_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_v1x_roadmap_candidates(profile)
    df = pd.DataFrame([roadmap_candidate_to_dict(i) for i in items])
    return df, summarize_v1x_roadmap_candidates(df)

def summarize_v1x_roadmap_candidates(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
