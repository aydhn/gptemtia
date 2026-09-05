"""Tests for Candidate State Sequence Schema."""

import pandas as pd
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.candidate_state_sequence_schema import (
    build_candidate_state_sequence_schema_registry,
    validate_candidate_state_sequence_schema,
    CANDIDATE_STATE_SEQUENCE_COLUMNS,
)


def test_build_candidate_state_sequence_schema_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_candidate_state_sequence_schema_registry(profile)

    assert not df.empty
    assert len(df) == 12
    assert "column_name" in df.columns
    assert "is_required" in df.columns
    assert summary["total_schema_columns"] == 12
    assert summary["non_signal_certified"] is True


def test_validate_candidate_state_sequence_schema():
    # Valid dataframe
    cols = [col["column_name"] for col in CANDIDATE_STATE_SEQUENCE_COLUMNS if col["is_required"]]
    sample_df = pd.DataFrame([{c: 1 for c in cols}])
    res = validate_candidate_state_sequence_schema(sample_df)
    assert res["is_valid"] is True

    # Missing columns
    bad_df = pd.DataFrame([{"symbol": "GOLD"}])
    res_bad = validate_candidate_state_sequence_schema(bad_df)
    assert res_bad["is_valid"] is False
    assert len(res_bad["missing_columns"]) > 0

    # Forbidden column
    forbidden_df = pd.DataFrame([{c: 1 for c in cols} | {"buy_signal": 1}])
    res_forb = validate_candidate_state_sequence_schema(forbidden_df)
    assert res_forb["is_valid"] is False
    assert len(res_forb["forbidden_columns"]) > 0
