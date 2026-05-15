import pandas as pd
from risk.pretrade_risk import PreTradeRiskEvaluator
from risk.risk_config import get_default_risk_precheck_profile


def test_evaluate_rule_candidate():
    prof = get_default_risk_precheck_profile()
    evaluator = PreTradeRiskEvaluator(prof)
    row = pd.Series({"strategy_family": "trend", "timestamp": "2023-01-01"})
    ctx_frames = {
        "regime": pd.DataFrame(
            {"regime_primary_label": ["strong_trend"]}, index=["2023-01-01"]
        )
    }

    eval_dict, _ = evaluator.evaluate_rule_candidate("AAPL", "1d", row, ctx_frames)
    assert "total_pretrade_risk_score" in eval_dict
    assert 0 <= eval_dict["total_pretrade_risk_score"] <= 1.0
    assert 0 <= eval_dict["risk_readiness_score"] <= 1.0
    assert isinstance(eval_dict["passed_risk_precheck"], bool)
