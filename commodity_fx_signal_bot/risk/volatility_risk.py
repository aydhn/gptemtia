from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_atr_percent_risk(value: Optional[float]) -> float:
    if value is None:
        return 0.5
    if value > 0.05:
        return 0.9
    if value > 0.03:
        return 0.7
    if value > 0.015:
        return 0.4
    if value < 0.002:
        return 0.3
    return 0.1


def score_volatility_percentile_risk(value: Optional[float]) -> float:
    if value is None:
        return 0.5
    if value > 95:
        return 0.8
    if value > 80:
        return 0.6
    if value < 10:
        return 0.4
    return 0.2


def score_volatility_event_risk(context_snapshot: dict) -> float:
    risk = 0.2
    if context_snapshot.get("event_volatility_expansion_bb20"):
        risk += 0.3
    if context_snapshot.get("event_atr_pct_high"):
        risk += 0.2
    if context_snapshot.get("event_range_shock_high"):
        risk += 0.4
    if context_snapshot.get("event_high_volatility_regime"):
        risk += 0.3
    return min(1.0, risk)


def detect_extreme_volatility_context(context_snapshot: dict) -> dict:
    reasons = []
    warnings = []
    if context_snapshot.get("atr_pct_14", 0) > 0.06:
        reasons.append("ATR percentage > 6%")
    if context_snapshot.get("event_range_shock_high"):
        reasons.append("High range shock event")
    if "atr_pct_14" not in context_snapshot:
        warnings.append("Missing ATR context")
    return {"reasons": reasons, "warnings": warnings}


def calculate_volatility_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_volatility_risk if profile else 0.75
    atr_risk = score_atr_percent_risk(context_snapshot.get("atr_pct_14"))
    perc_risk = score_volatility_percentile_risk(
        context_snapshot.get("percentile_atr_pct_14_120")
    )
    event_risk = score_volatility_event_risk(context_snapshot)
    total_score = (atr_risk * 0.4) + (perc_risk * 0.3) + (event_risk * 0.3)
    extreme = detect_extreme_volatility_context(context_snapshot)
    if extreme["reasons"]:
        total_score = max(total_score, 0.85)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "volatility",
        total_score,
        severity_from_score(total_score),
        passed,
        extreme["reasons"] if not passed else [],
        extreme["warnings"],
    )
