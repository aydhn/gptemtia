# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: cost_adjusted_evaluation_report_contracts."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.cost_adjusted_evaluation_report_contracts import build_cost_adjusted_evaluation_report_contract_registry


def test_build_cost_adjusted_evaluation_report_contract_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_cost_adjusted_evaluation_report_contract_registry(profile)

    assert not df.empty
    assert len(df) >= 2
    assert "contract_name" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["non_signal"] is True
    assert summary["status"] == "evaluation_contract_ready"
