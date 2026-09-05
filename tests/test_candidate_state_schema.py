import pandas as pd
from advanced_regime_rule_free.candidate_state_schema import (
    build_candidate_state_schema_registry,
    validate_candidate_state_schema,
    CANDIDATE_STATE_COLUMNS,
)


def test_build_candidate_state_schema_registry():
    df, summary = build_candidate_state_schema_registry()
    assert len(df) == len(CANDIDATE_STATE_COLUMNS)
    assert summary["all_non_signal"] is True
    assert summary["all_not_target_or_prediction"] is True
    assert summary["schema_status"] == "VALID"

    cols = df["column_name"].tolist()
    assert "candidate_state_key" in cols
    assert "entity_type" in cols
    assert "entity_id" in cols
    assert "timestamp_utc" in cols
    assert "candidate_state_family" in cols
    assert "candidate_state_context" in cols
    assert "source_matrix_ref" in cols
    assert "assignment_policy_ref" in cols
    assert "validation_status_ref" in cols
    assert "quality_status_ref" in cols
    assert "manual_review_required" in cols
    assert "non_signal" in cols


def test_validate_candidate_state_schema_valid_dataframe():
    valid_df = pd.DataFrame(columns=[c.column_name for c in CANDIDATE_STATE_COLUMNS])
    res = validate_candidate_state_schema(valid_df)
    assert res["is_valid"] is True
    assert len(res["missing_columns"]) == 0
    assert len(res["forbidden_columns_detected"]) == 0


def test_validate_candidate_state_schema_detects_forbidden_columns():
    invalid_df = pd.DataFrame(columns=["candidate_state_key", "target", "buy_signal", "future_return"])
    res = validate_candidate_state_schema(invalid_df)
    assert res["is_valid"] is False
    assert len(res["forbidden_columns_detected"]) >= 2
