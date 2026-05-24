import pandas as pd
from research_planning.planning_models import ResearchSignal

def calculate_research_opportunity_score(signal: ResearchSignal) -> float:
    # A mix of high opportunity and low uncertainty means good opportunity
    return min(1.0, (signal.opportunity_score * 0.7) + ((1.0 - signal.uncertainty_score) * 0.3))

def identify_research_opportunities(signals: list[ResearchSignal], backlog_df: pd.DataFrame) -> pd.DataFrame:
    opp_rows = []

    for sig in signals:
        opp_score = calculate_research_opportunity_score(sig)
        if opp_score > 0.5:
            opp_rows.append({
                "signal_id": sig.signal_id,
                "source_module": sig.source_module,
                "title": sig.title,
                "opportunity_score": opp_score,
                "classification": classify_research_opportunity(opp_score)
            })

    return pd.DataFrame(opp_rows)

def classify_research_opportunity(score: float) -> str:
    if score > 0.8:
        return "high_opportunity"
    elif score > 0.6:
        return "medium_opportunity"
    return "low_opportunity"

def summarize_research_opportunities(opportunity_df: pd.DataFrame) -> dict:
    if opportunity_df.empty:
        return {"total_opportunities": 0}

    return {
        "total_opportunities": len(opportunity_df),
        "classifications": opportunity_df["classification"].value_counts().to_dict() if "classification" in opportunity_df.columns else {}
    }
