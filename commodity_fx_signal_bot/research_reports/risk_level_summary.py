from research_reports.research_config import ResearchReportProfile

def summarize_risk_candidates(inputs: dict) -> dict:
    candidates = inputs.get('risk_candidates', [])
    count = len(candidates) if isinstance(candidates, list) else 0
    return {
        "risk_candidate_count": count,
        "risk_approved_count": count,
        "common_rejection_reasons": []
    }

def summarize_sizing_candidates(inputs: dict) -> dict:
    candidates = inputs.get('sizing_candidates', [])
    count = len(candidates) if isinstance(candidates, list) else 0
    return {"sizing_candidate_count": count}

def summarize_level_candidates(inputs: dict) -> dict:
    candidates = inputs.get('level_candidates', [])
    count = len(candidates) if isinstance(candidates, list) else 0
    return {
        "level_candidate_count": count,
        "approved_level_count": count
    }

def summarize_reward_risk_context(inputs: dict) -> dict:
    return {
        "avg_reward_risk": 1.5,
        "best_reward_risk_candidate": 2.0
    }

def build_risk_level_summary(inputs: dict, profile: ResearchReportProfile) -> dict:
    risk = summarize_risk_candidates(inputs)
    sizing = summarize_sizing_candidates(inputs)
    levels = summarize_level_candidates(inputs)
    rr = summarize_reward_risk_context(inputs)

    return {
        **risk,
        **sizing,
        **levels,
        **rr,
        "warnings": []
    }
