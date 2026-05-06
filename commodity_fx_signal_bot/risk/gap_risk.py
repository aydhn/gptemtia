from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_gap_percent_risk(value: Optional[float]) -> float:
    if value is None:
        return 0.3
    if value > 0.03:
        return 0.9
    if value > 0.015:
        return 0.6
    if value > 0.005:
        return 0.3
    return 0.1


def score_asset_gap_profile_risk(context_snapshot: dict) -> float:
    risk = 0.2
    if context_snapshot.get("asset_high_gap_risk_warning"):
        risk += 0.4
    if context_snapshot.get("asset_gap_risk_score"):
        risk = max(risk, context_snapshot["asset_gap_risk_score"])
    return min(1.0, risk)


def detect_gap_warning_context(context_snapshot: dict) -> dict:
    reasons = []
    warnings = []
    if "abs_gap_pct" not in context_snapshot:
        warnings.append("Missing gap percent context")
    if context_snapshot.get("event_large_gap"):
        reasons.append("Large gap event detected")
    return {"reasons": reasons, "warnings": warnings}


def calculate_gap_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_gap_risk if profile else 0.75
    gap_pct = context_snapshot.get("abs_gap_pct")
    if gap_pct is None and "gap_pct" in context_snapshot:
        gap_pct = abs(context_snapshot["gap_pct"])
    gap_risk = score_gap_percent_risk(gap_pct)
    asset_risk = score_asset_gap_profile_risk(context_snapshot)
    total_score = (gap_risk * 0.7) + (asset_risk * 0.3)
    detect = detect_gap_warning_context(context_snapshot)
    if detect["reasons"]:
        total_score = max(total_score, 0.8)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "gap",
        total_score,
        severity_from_score(total_score),
        passed,
        detect["reasons"] if not passed else [],
        detect["warnings"],
    )
