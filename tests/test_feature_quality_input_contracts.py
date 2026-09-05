import pytest
from advanced_feature_quality_drift.feature_quality_input_contracts import build_feature_quality_input_contract_registry


def test_feature_quality_input_contracts():
    df, summary = build_feature_quality_input_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] >= 5
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False

    contract_ids = list(df["contract_id"])
    assert "contract_df_immutability" in contract_ids
    assert "contract_non_destructive" in contract_ids
    assert "contract_forbidden_columns" in contract_ids
