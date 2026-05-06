from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_strategy_regime_mismatch(context_snapshot: dict) -> float:
    strat = context_snapshot.get("strategy_family", "").lower()
    regime = context_snapshot.get("regime_primary_label", "").lower()
    if not strat or not regime:
        return 0.5
    if "trend" in strat:
        if "range" in regime or "conflict" in regime:
            return 0.8
        if "strong_trend" in regime:
            return 0.1
    if "mean_reversion" in strat or "range" in strat:
        if "strong_trend" in regime:
            return 0.9
        if "range" in regime:
            return 0.1
    if "breakout" in strat:
        if "low_volatility" in regime or "compression" in regime:
            return 0.3
    return 0.4


def score_regime_confidence_risk(context_snapshot: dict) -> float:
    conf = context_snapshot.get("regime_confidence")
    if conf is None:
        return 0.5
    if conf < 0.3:
        return 0.8
    if conf < 0.6:
        return 0.5
    return 0.1


def detect_regime_risk_context(context_snapshot: dict) -> dict:
    reasons = []
    warnings = []
    if "regime_primary_label" not in context_snapshot:
        warnings.append("Missing primary regime context")
    if context_snapshot.get("event_conflicting_regime"):
        reasons.append("Conflicting regime event detected")
    if (
        context_snapshot.get("event_high_volatility_regime")
        and "mean_reversion" in context_snapshot.get("strategy_family", "").lower()
    ):
        reasons.append("Mean reversion in high volatility regime")
    return {"reasons": reasons, "warnings": warnings}


def calculate_regime_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_regime_risk if profile else 0.70
    mismatch_risk = score_strategy_regime_mismatch(context_snapshot)
    conf_risk = score_regime_confidence_risk(context_snapshot)
    total_score = (mismatch_risk * 0.7) + (conf_risk * 0.3)
    detect = detect_regime_risk_context(context_snapshot)
    if detect["reasons"]:
        total_score = max(total_score, 0.75)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "regime",
        total_score,
        severity_from_score(total_score),
        passed,
        detect["reasons"] if not passed else [],
        detect["warnings"],
    )
