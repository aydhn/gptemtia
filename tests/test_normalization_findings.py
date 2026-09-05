from advanced_data_normalization.normalization_findings import (
    create_normalization_finding,
    build_normalization_finding_registry,
    summarize_normalization_findings,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalization_findings():
    f = create_normalization_finding(
        rule_id="rule_test",
        dataset_type="dataset_fx_quote",
        source_field="pair",
        original_value_repr="EURUSD",
        normalized_value_repr="EUR/USD",
        status_label="normalization_applied",
        severity_label="normalization_low",
        message="normalized",
        manual_review_required=False,
    )
    prof = get_default_data_normalization_profile()
    df, summary = build_normalization_finding_registry([f], prof)
    assert len(df) == 1
    assert summary["total_findings"] == 1
    assert summary["applied_count"] == 1
    assert summary["manual_review_required_count"] == 0
