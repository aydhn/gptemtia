from sizing.sizing_filters import (
    should_block_sizing,
    should_watchlist_sizing,
    infer_sizing_candidate_label,
    rank_sizing_candidates,
)
from sizing.sizing_config import get_default_sizing_profile
import pandas as pd


def test_should_block_sizing():
    profile = get_default_sizing_profile()

    risk_row = pd.Series(
        {"risk_label": "risk_rejected_candidate", "risk_readiness_score": 0.1}
    )
    eval_ctx = {
        "capped_theoretical_risk_amount": 100.0,
        "adjusted_theoretical_notional": 1000.0,
    }

    blocked, reasons = should_block_sizing(risk_row, eval_ctx, profile)
    assert blocked is True
    assert len(reasons) > 0


def test_should_watchlist_sizing():
    profile = get_default_sizing_profile()
    # Mock borderline
    risk_row = pd.Series(
        {
            "risk_label": "risk_approved_candidate",
            "risk_readiness_score": profile.min_risk_readiness_score + 0.05,
        }
    )
    eval_ctx = {
        "capped_theoretical_risk_amount": 100.0,
        "adjusted_theoretical_notional": 1000.0,
    }

    watchlist, reasons = should_watchlist_sizing(risk_row, eval_ctx, profile)
    assert watchlist is True


def test_infer_sizing_candidate_label():
    profile = get_default_sizing_profile()
    # Good candidate
    risk_row = pd.Series(
        {
            "risk_label": "risk_approved_candidate",
            "risk_readiness_score": 0.9,
            "total_pretrade_risk_score": 0.1,
        }
    )
    eval_ctx = {
        "capped_theoretical_risk_amount": 100.0,
        "adjusted_theoretical_notional": 1000.0,
        "exposure_eval": {
            "symbol_limit_passed": True,
            "asset_class_limit_passed": True,
        },
    }

    label = infer_sizing_candidate_label(risk_row, eval_ctx, profile)
    assert label == "sizing_approved_candidate"


def test_rank_sizing_candidates():
    df = pd.DataFrame(
        {"sizing_id": ["a", "b", "c"], "sizing_readiness_score": [0.5, 0.9, 0.2]}
    )
    ranked = rank_sizing_candidates(df)
    assert ranked.iloc[0]["sizing_id"] == "b"
