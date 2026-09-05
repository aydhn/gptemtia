import pandas as pd
from advanced_regime_rule_free.pseudo_state_schema import (
    build_pseudo_state_schema_registry,
    validate_pseudo_state_schema,
)


def test_build_pseudo_state_schema_registry():
    df, summary = build_pseudo_state_schema_registry()
    assert len(df) >= 8
    assert summary["all_non_signal"] is True
    assert summary["all_no_training"] is True
    assert summary["all_no_clustering"] is True
    assert summary["schema_status"] == "VALID"

    keys = df["pseudo_state_key"].tolist()
    assert "pseudo_state_volatility_high" in keys
    assert "pseudo_state_trend_persistent" in keys
    assert "pseudo_state_range_mean_reverting" in keys
    assert "pseudo_state_macro_shock_context" in keys


def test_validate_pseudo_state_schema():
    df, _ = build_pseudo_state_schema_registry()
    res = validate_pseudo_state_schema(df)
    assert res["is_valid"] is True
    assert res["training_executed"] is False
    assert res["clustering_executed"] is False
    assert res["all_non_signal"] is True
