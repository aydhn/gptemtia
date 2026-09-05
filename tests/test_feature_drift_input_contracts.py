import pytest
from advanced_feature_quality_drift.feature_drift_input_contracts import build_feature_drift_input_contract_registry


def test_feature_drift_input_contracts():
    df, summary = build_feature_drift_input_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] >= 4
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False

    contract_ids = list(df["contract_id"])
    assert "contract_baseline_alignment" in contract_ids
    assert "contract_min_sample_size" in contract_ids
    assert "contract_temporal_precedence" in contract_ids
