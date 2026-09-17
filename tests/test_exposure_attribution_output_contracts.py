# -*- coding: utf-8 -*-
"""Unit tests for Exposure Attribution Output Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.exposure_attribution_output_contracts import build_exposure_attribution_output_contract_registry


def test_build_exposure_attribution_output_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_exposure_attribution_output_contract_registry(profile)

    assert not df.empty
    assert summary["output_contract_count"] >= 1
    assert summary["status"] == "exposure_attribution_contract_ready"
    assert (df["actual_attribution_generated"] == False).all()
    assert (df["capital_allocation_recommended"] == False).all()
