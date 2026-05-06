from risk.risk_models import (
    clamp_risk_score,
    invert_readiness_from_risk,
    aggregate_component_scores,
    RiskComponentScore,
    risk_component_score_to_dict,
)


def test_clamp_risk_score():
    assert clamp_risk_score(-1.0) == 0.0
    assert clamp_risk_score(2.0) == 1.0
    assert clamp_risk_score(0.5) == 0.5


def test_invert_readiness_from_risk():
    assert invert_readiness_from_risk(0.2) == 0.8


def test_aggregate_component_scores():
    scores = [
        RiskComponentScore("volatility", 1.0, "extreme", False, [], []),
        RiskComponentScore("gap", 0.0, "low", True, [], []),
    ]
    weights = {"volatility": 0.8, "gap": 0.2}
    total, d = aggregate_component_scores(scores, weights)
    assert total == 0.8
    assert d["volatility"] == 1.0
    assert d["gap"] == 0.0


def test_risk_component_score_to_dict():
    score = RiskComponentScore("volatility", 1.0, "extreme", False, ["reason"], [])
    d = risk_component_score_to_dict(score)
    assert d["component"] == "volatility"
    assert d["reasons"] == ["reason"]
