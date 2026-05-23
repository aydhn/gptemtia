
import pandas as pd


def build_quality_adjusted_ranking(
    consensus_df: pd.DataFrame,
    ensemble_df: pd.DataFrame,
    adjustment_df: pd.DataFrame
) -> pd.DataFrame:

    if consensus_df.empty or ensemble_df.empty or adjustment_df.empty:
        return pd.DataFrame()

    merged = pd.merge(
        consensus_df,
        ensemble_df[["symbol", "ensemble_score"]],
        on="symbol",
        how="left"
    )

    merged = pd.merge(
        merged,
        adjustment_df[["symbol", "quality_adjusted_score"]],
        on="symbol",
        how="left"
    )

    merged = merged.sort_values(by="quality_adjusted_score", ascending=False).reset_index(drop=True)
    merged["rank"] = merged.index + 1

    merged = assign_meta_rank_labels(merged)

    if "asset_class" not in merged:
        merged["asset_class"] = "unknown"
    if "uncertainty_score" not in merged:
        merged["uncertainty_score"] = 0.5
    if "missing_source_count" not in merged:
        merged["missing_source_count"] = 0

    return merged

def assign_meta_rank_labels(ranking_df: pd.DataFrame) -> pd.DataFrame:
    if "quality_adjusted_score" not in ranking_df:
        return ranking_df

    def _label(score):
        if pd.isna(score):
            return "insufficient_data_alignment"
        if score >= 0.70:
            return "high_research_alignment"
        elif score >= 0.60:
            return "moderate_research_alignment"
        elif score <= 0.30:
            return "weak_research_alignment"
        elif score <= 0.40:
            return "mixed_research_alignment"
        else:
            return "neutral_research_alignment"

    ranking_df["meta_rank_label"] = ranking_df["quality_adjusted_score"].apply(_label)
    return ranking_df

def summarize_meta_ranking(ranking_df: pd.DataFrame) -> dict:
    if ranking_df.empty:
        return {"ranked_symbols": 0, "high_alignment_count": 0, "weak_alignment_count": 0}

    high_alignment = (ranking_df["meta_rank_label"] == "high_research_alignment").sum()
    weak_alignment = (ranking_df["meta_rank_label"] == "weak_research_alignment").sum()

    return {
        "ranked_symbols": len(ranking_df),
        "high_alignment_count": int(high_alignment),
        "weak_alignment_count": int(weak_alignment)
    }
