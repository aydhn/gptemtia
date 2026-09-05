"""Tests for Pseudo State Sequence Schema."""

import pandas as pd
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.pseudo_state_sequence_schema import (
    build_pseudo_state_sequence_schema_registry,
    validate_pseudo_state_sequence_schema,
    PSEUDO_STATE_SEQUENCE_COLUMNS,
)


def test_build_pseudo_state_sequence_schema_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_pseudo_state_sequence_schema_registry(profile)

    assert not df.empty
    assert len(df) == 12
    assert "column_name" in df.columns
    assert summary["total_schema_columns"] == 12
    assert summary["non_signal_certified"] is True


def test_validate_pseudo_state_sequence_schema():
    cols = [col["column_name"] for col in PSEUDO_STATE_SEQUENCE_COLUMNS if col["is_required"]]
    sample_df = pd.DataFrame([{c: 1 for c in cols}])
    res = validate_pseudo_state_sequence_schema(sample_df)
    assert res["is_valid"] is True

    bad_df = pd.DataFrame([{"symbol": "USDTRY"}])
    res_bad = validate_pseudo_state_sequence_schema(bad_df)
    assert res_bad["is_valid"] is False

    forb_df = pd.DataFrame([{c: 1 for c in cols} | {"prediction": 0.5}])
    res_forb = validate_pseudo_state_sequence_schema(forb_df)
    assert res_forb["is_valid"] is False
