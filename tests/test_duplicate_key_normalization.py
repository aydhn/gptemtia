import pandas as pd
from advanced_data_normalization.duplicate_key_normalization import (
    build_canonical_duplicate_key,
    add_duplicate_key_column,
    build_duplicate_key_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_build_canonical_duplicate_key():
    row = {"pair": "EUR/USD", "timestamp": "2026-03-01 10:00:00"}
    k = build_canonical_duplicate_key(row, ["pair", "timestamp"])
    assert k == "eur/usd::2026-03-01 10:00:00"


def test_add_duplicate_key_column_preserves_records():
    raw_df = pd.DataFrame([
        {"id": 1, "pair": "EUR/USD", "time": "2026-01-01"},
        {"id": 2, "pair": "EUR/USD", "time": "2026-01-01"},  # duplicate
        {"id": 3, "pair": "USD/TRY", "time": "2026-01-01"},
    ])
    norm_df, findings = add_duplicate_key_column(raw_df, ["pair", "time"])

    # Verify no records deleted! Length must remain 3
    assert len(norm_df) == 3
    assert "canonical_duplicate_key" in norm_df.columns
    assert len(findings) == 1
    assert findings[0].manual_review_required is True


def test_duplicate_key_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_duplicate_key_normalization_registry(prof)
    assert not df.empty
    assert summary["records_deleted"] == 0
    assert summary["destructive_action_allowed"] is False
