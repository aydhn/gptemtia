import pandas as pd
from synthetic_indices.index_config import get_default_synthetic_index_profile
from synthetic_indices.rotation_research import (
    calculate_rotation_scores,
    build_rotation_records,
    calculate_rotation_stability
)

def test_rotation_research():
    dates = pd.date_range("2023-01-01", periods=100)
    retA = pd.Series([0.01]*100, index=dates)
    retB = pd.Series([0.005]*100, index=dates)

    returns_df = pd.DataFrame({"A": retA, "B": retB})
    profile = get_default_synthetic_index_profile()

    rot_df = calculate_rotation_scores(returns_df, profile)
    assert not rot_df.empty
    assert "rotation_score" in rot_df.columns
    assert "rotation_rank" in rot_df.columns

    # A should rank better than B
    rank_A = rot_df.loc[rot_df["symbol"] == "A", "rotation_rank"].iloc[0]
    rank_B = rot_df.loc[rot_df["symbol"] == "B", "rotation_rank"].iloc[0]
    assert rank_A <= rank_B

    # Previous dataframe
    prev_df = pd.DataFrame({
        "symbol": ["A", "B"],
        "rotation_rank": [2, 1] # Used to be B, A
    })

    records = build_rotation_records(rot_df, prev_df, "1d", profile)
    assert len(records) == 2

    # A went from 2 to 1 (delta 1) -> improving
    record_a = next(r for r in records if r.symbol == "A")
    assert record_a.rank_delta == 1
    assert record_a.rotation_label == "rotation_candidate_leader" or record_a.rotation_label == "rotation_candidate_improving"

    # Stability
    df = pd.DataFrame([vars(r) for r in records])
    stab = calculate_rotation_stability(df, prev_df)
    assert "stability_score" in stab
