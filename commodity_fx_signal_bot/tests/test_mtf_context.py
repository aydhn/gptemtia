import pytest
import pandas as pd
from mtf.mtf_context import add_mtf_context_columns, summarize_mtf_context


def test_add_mtf_context_columns():
    df = pd.DataFrame({"tf_1d_trend_score": [1.0, -1.0]})
    res, summ = add_mtf_context_columns(df)

    assert "mtf_trend_alignment_score" in res.columns
    assert "mtf_stale_context_ratio" in res.columns


def test_summarize_mtf_context():
    df = pd.DataFrame(
        {"mtf_trend_alignment_score": [1.0, 1.0], "mtf_stale_context_ratio": [0.0, 0.0]}
    )

    summ = summarize_mtf_context("TEST", "1d", ("1wk",), df)

    assert summ.symbol == "TEST"
    assert summ.trend_alignment_score == 1.0
    assert summ.stale_context_ratio == 0.0
