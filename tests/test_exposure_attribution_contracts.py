# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Exposure Attribution Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.exposure_attribution_contracts import build_exposure_attribution_contract_registry


def test_build_exposure_attribution_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_exposure_attribution_contract_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert summary["contract_count"] >= 8
    assert summary["all_contracts_placeholder"] is True
    assert summary["zero_exposure_calculated"] is True
    assert summary["zero_execution_allowed"] is True
    assert "contract_name" in df.columns
    assert "exposure_family" in df.columns
    assert "allows_execution" in df.columns
    assert (df["allows_execution"] == False).all()
