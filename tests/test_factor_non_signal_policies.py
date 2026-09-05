import pandas as pd
import pytest
from advanced_factor_metadata.factor_non_signal_policies import (
    build_factor_non_signal_policy_registry,
    summarize_factor_non_signal_policy,
    validate_factor_non_signal_policy,
)


def test_build_factor_non_signal_policy_registry():
    df, summary = build_factor_non_signal_policy_registry()
    assert not df.empty
    assert summary["total_policies"] >= 5
    assert summary["non_signal"] is True

    stats = summarize_factor_non_signal_policy(df)
    assert stats["total_policies"] == len(df)
    assert stats["non_signal"] is True


def test_validate_factor_non_signal_policy():
    valid_res = validate_factor_non_signal_policy(text="Pure research factor metadata container.")
    assert valid_res["is_compliant"] is True
    assert len(valid_res["violations"]) == 0

    invalid_res = validate_factor_non_signal_policy(text="This factor produces a buy signal for trading.")
    assert invalid_res["is_compliant"] is False
    assert len(invalid_res["violations"]) > 0

    df_invalid = pd.DataFrame({"target_column": [1, 2]})
    col_res = validate_factor_non_signal_policy(df=df_invalid)
    assert col_res["is_compliant"] is False
