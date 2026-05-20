from research_reports.research_config import ResearchReportProfile

def summarize_trend_context(inputs: dict) -> dict:
    return {"trend_label": "neutral_context"}

def summarize_momentum_context(inputs: dict) -> dict:
    return {"momentum_label": "neutral_context"}

def summarize_volatility_context(inputs: dict) -> dict:
    return {"volatility_label": "neutral_context"}

def summarize_regime_context(inputs: dict) -> dict:
    return {"regime_label": "unknown_context"}

def summarize_signal_candidates(inputs: dict) -> dict:
    candidates = inputs.get('signal_candidates', [])
    count = len(candidates) if isinstance(candidates, list) else 0
    return {
        "signal_candidate_count": count,
        "strongest_signal_context": "neutral_context" if count == 0 else "supportive_context",
        "conflict_count": 0,
        "uncertainty_count": 0
    }

def build_technical_summary(inputs: dict, profile: ResearchReportProfile) -> dict:
    trend = summarize_trend_context(inputs)
    momentum = summarize_momentum_context(inputs)
    volatility = summarize_volatility_context(inputs)
    regime = summarize_regime_context(inputs)
    signals = summarize_signal_candidates(inputs)

    return {
        **trend,
        **momentum,
        **volatility,
        **regime,
        **signals,
        "warnings": []
    }
