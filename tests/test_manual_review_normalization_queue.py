import pandas as pd
from advanced_data_normalization.manual_review_normalization_queue import (
    build_manual_review_normalization_queue,
    summarize_manual_review_normalization_queue,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_manual_review_normalization_queue():
    findings_df = pd.DataFrame([
        {
            "finding_id": "find_bad_pair",
            "rule_id": "rule_fx",
            "dataset_type": "dataset_fx_quote",
            "source_field": "pair",
            "original_value_repr": "BADPAIR",
            "severity_label": "normalization_high",
            "manual_review_required": True,
        },
        {
            "finding_id": "find_good_pair",
            "rule_id": "rule_fx",
            "dataset_type": "dataset_fx_quote",
            "source_field": "pair",
            "original_value_repr": "EURUSD",
            "severity_label": "normalization_low",
            "manual_review_required": False,
        },
    ])
    prof = get_default_data_normalization_profile()
    df, summary = build_manual_review_normalization_queue(findings_df, prof)

    # Only manual_review_required item must be in queue
    assert len(df) == 1
    assert df["finding_id"].iloc[0] == "find_bad_pair"
    assert summary["destructive_actions_prevented"] is True
    assert summary["source_preserved_all"] is True
