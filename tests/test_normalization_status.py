from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.normalization_status import (
    build_normalization_status_registry,
    summarize_normalization_status,
)


def test_status_registry():
    prof = get_default_data_normalization_profile()
    df, summary = build_normalization_status_registry(prof)
    assert not df.empty
    assert "normalization_applied" in df["status_label"].tolist()
    assert summary["total_statuses"] >= 6
