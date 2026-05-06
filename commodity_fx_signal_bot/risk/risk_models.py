from dataclasses import dataclass, asdict


@dataclass
class RiskComponentScore:
    component: str
    score: float
    severity: str
    passed: bool
    reasons: list[str]
    warnings: list[str]


@dataclass
class RiskContextSnapshot:
    symbol: str
    timeframe: str
    timestamp: str
    asset_class: str
    strategy_family: str
    condition_label: str
    directional_bias: str
    context_available: bool
    context_keys: list[str]
    warnings: list[str]


def clamp_risk_score(score: float) -> float:
    return max(0.0, min(1.0, float(score)))


def invert_readiness_from_risk(total_risk_score: float) -> float:
    return clamp_risk_score(1.0 - total_risk_score)


def aggregate_component_scores(
    scores: list[RiskComponentScore], weights: dict[str, float]
) -> tuple[float, dict]:
    total_score = 0.0
    component_dict = {}
    total_weight = 0.0
    for s in scores:
        w = weights.get(s.component, 0.0)
        total_score += s.score * w
        total_weight += w
        component_dict[s.component] = s.score
    if total_weight > 0:
        total_score /= total_weight
    return clamp_risk_score(total_score), component_dict


def risk_component_score_to_dict(score: RiskComponentScore) -> dict:
    return asdict(score)
