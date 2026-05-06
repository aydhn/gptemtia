from typing import Optional
from risk.risk_models import RiskComponentScore
from risk.risk_config import RiskPrecheckProfile
from risk.risk_labels import severity_from_score


def score_quality_grade_risk(grade: Optional[str]) -> float:
    if not grade:
        return 0.6
    grade = grade.upper()
    if grade == "A":
        return 0.05
    if grade == "B":
        return 0.20
    if grade == "C":
        return 0.50
    if grade == "D":
        return 0.80
    if grade == "F":
        return 1.00
    return 0.6


def score_nan_ratio_risk(value: Optional[float]) -> float:
    if value is None:
        return 0.5
    if value > 0.1:
        return 0.9
    if value > 0.05:
        return 0.7
    if value > 0.01:
        return 0.4
    return 0.1


def score_missing_context_risk(
    missing_context_count: int, expected_context_count: int
) -> float:
    if expected_context_count == 0:
        return 0.0
    ratio = missing_context_count / expected_context_count
    if ratio > 0.5:
        return 0.9
    if ratio > 0.3:
        return 0.6
    if ratio > 0.1:
        return 0.3
    return 0.0


def detect_invalid_data_quality_context(context_snapshot: dict) -> dict:
    reasons = []
    warnings = []
    grade = context_snapshot.get("data_quality_grade", "")
    if grade in ["D", "F"]:
        reasons.append(f"Data quality grade is {grade}")
    if context_snapshot.get("nan_ratio", 0) > 0.1:
        reasons.append("High NaN ratio in features")
    if not context_snapshot.get("context_available", True):
        warnings.append("Context frames are partially or completely missing")
    return {"reasons": reasons, "warnings": warnings}


def calculate_data_quality_risk_score(
    context_snapshot: dict, profile: Optional[RiskPrecheckProfile] = None
) -> RiskComponentScore:
    max_risk = profile.max_data_quality_risk if profile else 0.60
    grade_risk = score_quality_grade_risk(context_snapshot.get("data_quality_grade"))
    nan_risk = score_nan_ratio_risk(context_snapshot.get("nan_ratio"))
    expected = len(context_snapshot.get("context_keys", []))
    missing = expected - sum(
        1
        for k in context_snapshot.get("context_keys", [])
        if context_snapshot.get(k) is not None
    )
    context_risk = score_missing_context_risk(missing, expected)
    total_score = (grade_risk * 0.5) + (nan_risk * 0.3) + (context_risk * 0.2)
    detect = detect_invalid_data_quality_context(context_snapshot)
    if profile and profile.block_on_invalid_data_quality and detect["reasons"]:
        total_score = max(total_score, 0.9)
    passed = total_score <= max_risk
    return RiskComponentScore(
        "data_quality",
        total_score,
        severity_from_score(total_score),
        passed,
        detect["reasons"] if not passed else [],
        detect["warnings"],
    )
