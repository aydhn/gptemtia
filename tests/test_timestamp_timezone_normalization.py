import pandas as pd
from advanced_data_normalization.timestamp_timezone_normalization import (
    normalize_timestamp_to_utc_iso,
    normalize_timestamp_dataframe,
    build_timestamp_timezone_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_timestamp_to_utc():
    ts = normalize_timestamp_to_utc_iso("2026-03-01 10:00:00")
    assert "2026-03-01T10:00:00" in ts or "Z" in ts
    bad_ts = normalize_timestamp_to_utc_iso("invalid_time_string")
    assert bad_ts in ["invalid_time_string", "INVALID_TIMESTAMP"]


def test_normalize_timestamp_dataframe():
    raw_df = pd.DataFrame([{"timestamp": "2026-03-01 10:00:00"}, {"timestamp": "invalid_date"}])
    norm_df, findings = normalize_timestamp_dataframe(raw_df, timestamp_field="timestamp")

    # Source timestamp preserved
    assert "timestamp" in norm_df.columns
    assert "normalized_timestamp" in norm_df.columns
    manual_findings = [f for f in findings if f.manual_review_required]
    assert len(manual_findings) == 1
    assert manual_findings[0].manual_review_required is True


def test_timestamp_timezone_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_timestamp_timezone_normalization_registry(prof)
    assert not df.empty
    assert summary["canonical_timezone"] == "UTC"
