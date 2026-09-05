import pandas as pd
from advanced_data_normalization.normalization_scoring import (
    calculate_normalization_score,
    classify_normalization_score,
    build_normalization_score_report,
    summarize_normalization_scores,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalization_scoring():
    prof = get_default_data_normalization_profile()
    findings_df = pd.DataFrame([
        {
            "finding_id": "f1",
            "dataset_type": "dataset_fx_quote",
            "status_label": "normalization_manual_review_required",
            "severity_label": "normalization_high",
        }
    ])
    sc = calculate_normalization_score(findings_df, "fx_quote", "dataset_fx_quote", prof)
    assert 0.0 <= sc <= 1.0
    assert sc == 0.9  # 1.0 - 0.10 penalty for high severity manual review

    report_df, summary = build_normalization_score_report(findings_df, prof)
    assert not report_df.empty
    assert summary["is_trading_signal"] is False
    assert summary["is_official_approval"] is False
