from pathlib import Path
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_health import (
    build_data_normalization_health_check,
    summarize_data_normalization_health,
)


def test_data_normalization_health():
    root = Path(__file__).resolve().parent.parent
    prof = get_default_data_normalization_profile()
    df, summary = build_data_normalization_health_check(root, prof)
    assert not df.empty
    assert summary["total_checks"] >= 30
    assert summary["overall_status"] in ["PASS", "WARN"]
