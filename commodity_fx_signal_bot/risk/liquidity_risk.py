from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_volume_usability_risk(context_snapshot: dict) -> float:
    if "volume_is_usable" in context_snapshot:
        if not context_snapshot["volume_is_usable"]:
            return 0.6
        return 0.1
    return 0.5


def score_relative_volume_risk(context_snapshot: dict) -> float:
    val = context_snapshot.get("relative_volume_20")
    if val is None:
        return 0.5
    if val < 0.5:
        return 0.7
    if val < 0.8:
        return 0.4
    if val > 3.0:
        return 0.6
    return 0.1


def score_asset_liquidity_profile_risk(context_snapshot: dict) -> float:
    score = context_snapshot.get("asset_volume_confidence_score")
    if score is not None:
        if score < 0.3:
            return 0.8
        if score < 0.6:
            return 0.5
        return 0.1
    return 0.3


def detect_liquidity_warning_context(context_snapshot: dict) -> dict:
    warnings = []
    reasons = []
    if "volume_is_usable" not in context_snapshot:
        warnings.append("Missing volume usability context")
    elif not context_snapshot["volume_is_usable"]:
        warnings.append("Volume data is unreliable/unusable")
    if context_snapshot.get("event_liquidity_thin"):
        reasons.append("Thin liquidity event detected")
    if (
        context_snapshot.get("event_volume_unusable")
        and "volume" in context_snapshot.get("strategy_family", "").lower()
    ):
        reasons.append("Volume strategy with unusable volume")
    return {"reasons": reasons, "warnings": warnings}


def calculate_liquidity_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_liquidity_risk if profile else 0.75
    usability_risk = score_volume_usability_risk(context_snapshot)
    rel_vol_risk = score_relative_volume_risk(context_snapshot)
    asset_risk = score_asset_liquidity_profile_risk(context_snapshot)
    total_score = (usability_risk * 0.4) + (rel_vol_risk * 0.4) + (asset_risk * 0.2)
    detect = detect_liquidity_warning_context(context_snapshot)
    if detect["reasons"]:
        total_score = max(total_score, 0.8)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "liquidity",
        total_score,
        severity_from_score(total_score),
        passed,
        detect["reasons"] if not passed else [],
        detect["warnings"],
    )
