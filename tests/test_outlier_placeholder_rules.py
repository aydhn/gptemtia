import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.outlier_placeholder_rules import (
    build_outlier_detection_placeholder_rule_set,
    build_outlier_placeholder_findings,
)


def test_outlier_placeholder_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_outlier_detection_placeholder_rule_set(profile)
    assert len(df_rules) >= 1

    # DataFrame with one extreme outlier
    test_df = pd.DataFrame([
        {"price": 10.0}, {"price": 10.2}, {"price": 10.1},
        {"price": 9.9}, {"price": 10.05}, {"price": 1000.0}
    ])
    findings = build_outlier_placeholder_findings(test_df, ["price"], "dataset_fx_ohlcv", "test_p")
    assert len(findings) == 1
    assert findings[0].finding_type == "finding_outlier_placeholder"
    assert findings[0].manual_review_required is True
