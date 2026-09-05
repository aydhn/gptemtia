import pandas as pd
from advanced_regime_matrix.regime_matrix_asof_join_policies import (
    build_regime_matrix_asof_join_policy_registry,
    build_regime_matrix_asof_join_policies,
    safe_regime_matrix_asof_join_backward,
    summarize_regime_matrix_asof_join_policies,
)


def test_build_regime_matrix_asof_join_policies():
    df, s = build_regime_matrix_asof_join_policy_registry()
    assert len(df) == 5
    assert s["total_policies"] == 5
    assert s["mandatory_direction"] == "backward"
    assert s["all_enforced"] is True


def test_safe_regime_matrix_asof_join_backward():
    base_df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-01-02", "2026-01-04"]),
        "entity_id": ["BRENT", "BRENT"],
        "price": [75.0, 76.0],
    })
    ctx_df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-01-01", "2026-01-03"]),
        "entity_id": ["BRENT", "BRENT"],
        "context_val": [10.0, 20.0],
    })

    joined = safe_regime_matrix_asof_join_backward(
        left_df=base_df,
        right_df=ctx_df,
        left_on="timestamp",
        right_on="timestamp",
        by="entity_id",
    )
    assert len(joined) == 2
    assert "context_val" in joined.columns
    assert joined.iloc[0]["context_val"] == 10.0
    assert joined.iloc[1]["context_val"] == 20.0

    # Ensure source was not mutated
    assert "context_val" not in base_df.columns
