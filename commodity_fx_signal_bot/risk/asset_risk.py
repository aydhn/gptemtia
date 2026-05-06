from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_asset_behavior_risk(context_snapshot: dict) -> float:
    val = context_snapshot.get("asset_behavior_score")
    if val is None:
        return 0.5
    if val < 0.3:
        return 0.8
    if val < 0.6:
        return 0.5
    return 0.1


def score_asset_group_risk(context_snapshot: dict) -> float:
    val = context_snapshot.get("asset_risk_context_score")
    if val is not None:
        return val
    return 0.4


def score_relative_strength_risk(context_snapshot: dict) -> float:
    rs = context_snapshot.get("asset_relative_strength_regime_label", "").lower()
    bias = context_snapshot.get("directional_bias", "").lower()
    if not rs or not bias:
        return 0.4
    if "weak" in rs and "long" in bias:
        return 0.7
    if "strong" in rs and "short" in bias:
        return 0.7
    return 0.2


def score_dispersion_correlation_risk(context_snapshot: dict) -> float:
    if context_snapshot.get("event_asset_high_dispersion_context"):
        return 0.6
    return 0.2


def detect_asset_profile_risk_context(context_snapshot: dict) -> dict:
    reasons = []
    warnings = []
    if "asset_profile_label" not in context_snapshot:
        warnings.append("Missing asset profile context")
    if context_snapshot.get("event_asset_low_volume_confidence_warning"):
        reasons.append("Asset volume confidence warning")
    if context_snapshot.get("event_asset_high_gap_risk_warning"):
        reasons.append("Asset high gap risk warning")
    return {"reasons": reasons, "warnings": warnings}


def calculate_asset_profile_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_total_pretrade_risk if profile else 0.70
    beh_risk = score_asset_behavior_risk(context_snapshot)
    grp_risk = score_asset_group_risk(context_snapshot)
    rs_risk = score_relative_strength_risk(context_snapshot)
    disp_risk = score_dispersion_correlation_risk(context_snapshot)
    total_score = (
        (beh_risk * 0.3) + (grp_risk * 0.3) + (rs_risk * 0.3) + (disp_risk * 0.1)
    )
    detect = detect_asset_profile_risk_context(context_snapshot)
    if detect["reasons"]:
        total_score = max(total_score, 0.75)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "asset_profile",
        total_score,
        severity_from_score(total_score),
        passed,
        detect["reasons"] if not passed else [],
        detect["warnings"],
    )
