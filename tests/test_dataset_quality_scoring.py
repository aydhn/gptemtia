import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quality_findings import create_quality_finding
from advanced_data_quality.dataset_quality_scoring import (
    calculate_dataset_quality_score,
    build_dataset_quality_score_report,
    classify_dataset_quality_score,
    summarize_dataset_quality_scores,
)


def test_dataset_quality_scoring():
    profile = get_default_data_quality_profile()
    clean_score = calculate_dataset_quality_score(pd.DataFrame(), "fx_clean", "dataset_fx_ohlcv", 100, 10, profile)
    assert clean_score == 1.0

    # Dataset with high finding
    f = create_quality_finding("r_high", "type_x", "dataset_fx_ohlcv", "test_p", severity_label="quality_high")
    findings_df = pd.DataFrame([f.to_dict()])
    score = calculate_dataset_quality_score(findings_df, "fx_clean", "dataset_fx_ohlcv", 100, 10, profile)
    assert score < 1.0
    assert 0.0 <= score <= 1.0

    df_rep, sum_rep = build_dataset_quality_score_report(findings_df, profile)
    assert len(df_rep) >= 5
    assert sum_rep["total_datasets_scored"] >= 5
