from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_macro_conflict_risk(context_snapshot: dict) -> float:
    if context_snapshot.get("event_macro_conflicting"):
        return 0.8
    conf = context_snapshot.get("macro_confidence")
    if conf is not None and conf < 0.3:
        return 0.6
    return 0.2


def score_fx_pressure_risk(context_snapshot: dict) -> float:
    risk = 0.2
    if context_snapshot.get("event_macro_try_depreciation_pressure"):
        risk += 0.4
    if context_snapshot.get("usdtry_depreciation_pressure", 0) > 0.7:
        risk += 0.3
    return min(1.0, risk)


def score_inflation_uncertainty_risk(context_snapshot: dict) -> float:
    if context_snapshot.get("event_macro_high_local_inflation_fx_pressure"):
        return 0.7
    return 0.2


def detect_macro_risk_context(context_snapshot: dict) -> dict:
    reasons = []
    warnings = []
    if "macro_primary_label" not in context_snapshot:
        warnings.append("Missing macro context")
    return {"reasons": reasons, "warnings": warnings}


def calculate_macro_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_macro_risk if profile else 0.80
    conflict_risk = score_macro_conflict_risk(context_snapshot)
    fx_risk = score_fx_pressure_risk(context_snapshot)
    inf_risk = score_inflation_uncertainty_risk(context_snapshot)
    total_score = (conflict_risk * 0.4) + (fx_risk * 0.3) + (inf_risk * 0.3)
    detect = detect_macro_risk_context(context_snapshot)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "macro",
        total_score,
        severity_from_score(total_score),
        passed,
        detect["reasons"] if not passed else [],
        detect["warnings"],
    )
