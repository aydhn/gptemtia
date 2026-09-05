from typing import Tuple, Dict, Any
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_scoring import build_provider_benchmark_score_report


def build_provider_ranking_research_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    scores_df, _ = build_provider_benchmark_score_report(profile)
    if scores_df.empty:
        df = pd.DataFrame(
            columns=[
                "research_rank",
                "provider_name",
                "provider_domain",
                "total_score",
                "status_label",
                "research_tier",
                "official_approval",
                "disclaimer",
            ]
        )
        return df, summarize_provider_ranking_research(df)

    ranked_df = scores_df.sort_values(by="total_score", ascending=False).reset_index(drop=True)
    ranked_df["research_rank"] = ranked_df.index + 1

    def assign_tier(score: float) -> str:
        if score >= 0.90:
            return "tier_1_high_suitability"
        elif score >= 0.75:
            return "tier_2_moderate_suitability"
        else:
            return "tier_3_conditional_suitability"

    ranked_df["research_tier"] = ranked_df["total_score"].apply(assign_tier)
    ranked_df["official_approval"] = False
    ranked_df["disclaimer"] = "Research ranking only; not an official approval, endorsement, or trading recommendation"

    cols = [
        "research_rank",
        "provider_name",
        "provider_domain",
        "total_score",
        "research_tier",
        "status_label",
        "coverage_score",
        "capability_score",
        "quality_score",
        "normalization_score",
        "traceability_score",
        "compliance_score",
        "official_approval",
        "disclaimer",
    ]
    df = ranked_df[[c for c in cols if c in ranked_df.columns]]
    summary = summarize_provider_ranking_research(df)
    return df, summary


def summarize_provider_ranking_research(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_providers_ranked": len(df),
        "top_ranked_provider": str(df.iloc[0]["provider_name"]) if not df.empty and "provider_name" in df.columns else "none",
        "top_score": float(df.iloc[0]["total_score"]) if not df.empty and "total_score" in df.columns else 0.0,
        "official_approval_guarantee": False,
        "production_ready_guarantee": False,
        "broker_ready_guarantee": False,
        "disclaimer": "Provider ranking is for offline architectural evaluation only. It does NOT constitute an official recommendation or trading signal.",
        "current_phase": 115,
        "target_final_phase": 160,
    }
