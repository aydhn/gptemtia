import pandas as pd
from advanced_regime_matrix.regime_state_dataset_schema import (
    MINIMUM_STATE_DATASET_COLUMNS,
    REGIME_STATE_STANDARD_FIELDS,
    build_regime_state_dataset_schema,
    validate_regime_state_dataset_schema,
)


def test_build_regime_state_dataset_schema():
    df, s = build_regime_state_dataset_schema()
    assert len(df) == 11
    assert s["total_schema_fields"] == 11
    assert s["all_non_signal"] is True
    assert "entity_id" in df["field_name"].values
    assert "timestamp_utc" in df["field_name"].values
    assert "regime_state_candidate_context" in df["field_name"].values


def test_validate_regime_state_dataset_schema():
    valid_data = {col: [1] for col in MINIMUM_STATE_DATASET_COLUMNS}
    valid_df = pd.DataFrame(valid_data)
    res = validate_regime_state_dataset_schema(valid_df)
    assert res["is_valid"] is True

    # DataFrame containing forbidden label term
    dirty_data = dict(valid_data)
    dirty_data["target_regime_label"] = [1]
    dirty_df = pd.DataFrame(dirty_data)
    res_dirty = validate_regime_state_dataset_schema(dirty_df)
    assert res_dirty["is_valid"] is False
    assert len(res_dirty["forbidden_fields_found"]) > 0
