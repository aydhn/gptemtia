import pytest
import pandas as pd
from paper.paper_signal_adapter import filter_paper_eligible_level_candidates, merge_level_sizing_risk_candidates, infer_virtual_order_side, build_virtual_order_candidates
from paper.paper_config import get_default_paper_trading_profile

def test_filter_eligible_levels():
    profile = get_default_paper_trading_profile()
    df = pd.DataFrame({
        'level_label': ['level_approved_candidate', 'watchlist_candidate', 'rejected'],
        'directional_bias': ['long_bias', 'short_bias', 'long_bias']
    })

    filtered = filter_paper_eligible_level_candidates(df, profile)
    assert len(filtered) == 1

def test_merge_candidates():
    level_df = pd.DataFrame({'a': [1, 2]}, index=[1, 2])
    sizing_df = pd.DataFrame({'b': [3, 4]}, index=[1, 2])
    risk_df = pd.DataFrame({'c': [5, 6]}, index=[1, 2])

    merged, w = merge_level_sizing_risk_candidates(level_df, sizing_df, risk_df)
    assert 'b' in merged.columns
    assert 'c' in merged.columns
    assert not w

def test_infer_side():
    row = pd.Series({'directional_bias': 'long_bias'})
    assert infer_virtual_order_side(row) == "virtual_long_bias"

def test_build_candidates():
    profile = get_default_paper_trading_profile()
    level_df = pd.DataFrame({
        'level_label': ['level_approved_candidate'],
        'directional_bias': ['long_bias'],
        'symbol': ['GC=F'],
        'close': [100.0]
    }, index=[pd.to_datetime('2024-01-01')])

    # Needs risk and sizing approved
    risk_df = pd.DataFrame({'risk_label': ['risk_approval_candidate']}, index=[pd.to_datetime('2024-01-01')])
    sizing_df = pd.DataFrame({'sizing_label': ['sizing_approved_candidate']}, index=[pd.to_datetime('2024-01-01')])

    orders, w = build_virtual_order_candidates(level_df, sizing_df, risk_df, profile)
    assert len(orders) == 1
    assert orders[0].order_side == "virtual_long_bias"
