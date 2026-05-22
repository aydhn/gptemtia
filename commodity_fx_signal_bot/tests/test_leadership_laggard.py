import pandas as pd
from synthetic_indices.leadership_laggard import (
    identify_cross_asset_leaders,
    identify_cross_asset_laggards,
    build_leadership_laggard_table,
    summarize_leadership_laggard
)

def test_leadership_laggard():
    rs_df = pd.DataFrame({
        "symbol": ["A", "B", "C"],
        "relative_rank": [1, 2, 3],
        "relative_strength_label": ["leader", "neutral", "laggard"]
    })

    mom_df = pd.DataFrame({
        "symbol": ["A", "B", "C"],
        "momentum_rank": [1, 3, 2],
        "momentum_label": ["strong", "weak", "neutral"]
    })

    leaders = identify_cross_asset_leaders(rs_df, mom_df, top_n=1)
    assert len(leaders) == 1
    assert leaders["symbol"].iloc[0] == "A"

    laggards = identify_cross_asset_laggards(rs_df, mom_df, bottom_n=1)
    assert len(laggards) == 1

    table = build_leadership_laggard_table(rs_df, mom_df)



    summary = summarize_leadership_laggard(table)
    assert summary["total_symbols"] == 3
    assert summary["leaders"] >= 0
