import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quality_findings import create_quality_finding
from advanced_data_quality.provider_quality_scoring import (
    calculate_provider_quality_score,
    build_provider_quality_score_report,
    classify_provider_quality_score,
    summarize_provider_quality_scores,
)


def test_provider_quality_scoring():
    profile = get_default_data_quality_profile()
    # Clean provider score is 1.0
    clean_score = calculate_provider_quality_score(pd.DataFrame(), "test_prov", "dataset_fx_ohlcv", profile)
    assert clean_score == 1.0

    # Provider with critical finding gets penalty
    f = create_quality_finding("r_crit", "type_x", "dataset_fx_ohlcv", "bad_prov", severity_label="quality_critical")
    findings_df = pd.DataFrame([f.to_dict()])
    penalized = calculate_provider_quality_score(findings_df, "bad_prov", "dataset_fx_ohlcv", profile)
    assert penalized < 1.0
    assert 0.0 <= penalized <= 1.0

    # Report builder
    df_rep, sum_rep = build_provider_quality_score_report(findings_df, profile)
    assert len(df_rep) >= 5
    assert sum_rep["total_providers_scored"] >= 5
