# -*- coding: utf-8 -*-
"""Unit tests for Risk Report Output Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_report_output_contracts import build_risk_report_output_contract_registry


def test_build_risk_report_output_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_report_output_contract_registry(profile)

    assert not df.empty
    assert summary["output_contract_count"] >= 1
    assert summary["status"] == "risk_report_contract_ready"
    assert (df["actual_report_generated"] == False).all()
    assert (df["signal_generated"] == False).all()
