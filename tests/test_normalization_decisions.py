import pandas as pd
from advanced_data_normalization.normalization_decisions import (
    build_normalization_decision_registry,
    summarize_normalization_decisions,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalization_decisions():
    findings_df = pd.DataFrame([
        {
            "finding_id": "find_1",
            "rule_id": "rule_1",
            "status_label": "normalization_applied",
            "manual_review_required": False,
        }
    ])
    prof = get_default_data_normalization_profile()
    df, summary = build_normalization_decision_registry(findings_df, prof)
    assert len(df) == 1
    assert summary["source_preserved_all"] is True
    assert summary["destructive_action_zero"] is True
    assert summary["lineage_required_all"] is True
