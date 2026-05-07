import pytest
import pandas as pd
from levels.level_quality import (
    build_level_quality_report,
    check_for_forbidden_trade_terms_in_levels,
)


def test_forbidden_terms():
    df = pd.DataFrame({"notes": ["This is a BUY signal"]})
    res = check_for_forbidden_trade_terms_in_levels(df)
    assert res["forbidden_trade_terms_found"] is True
    assert "BUY" in res["terms"]


def test_quality_report():
    df = pd.DataFrame(
        {
            "level_id": ["1", "2"],
            "symbol": ["A", "B"],
            "timeframe": ["1d", "1d"],
            "level_label": ["x", "y"],
            "stop_target_readiness_score": [0.8, 1.5],  # invalid score
            "directional_bias": ["long_bias_candidate", "long_bias_candidate"],
            "latest_close": [100.0, 100.0],
            "theoretical_stop_level": [98.0, 102.0],  # invalid geometry
            "theoretical_target_level": [104.0, 104.0],
        }
    )
    rep = build_level_quality_report(df, {})
    assert rep["invalid_score_count"] == 1
    assert rep["invalid_geometry_count"] == 1
