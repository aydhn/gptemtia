# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Pipeline."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_pipeline import RiskReportingPipeline
from data.storage.data_lake import DataLake


def test_risk_reporting_pipeline():
    profile = get_default_risk_reporting_profile()
    data_lake = DataLake()
    pipeline = RiskReportingPipeline(data_lake=data_lake, profile=profile)

    _, s_p = pipeline.build_profiles_domains_scope(save=False)
    assert s_p["profile_summary"]["profile_count"] >= 3

    _, s_rc = pipeline.build_risk_report_contracts(save=False)
    assert s_rc["contract_summary"]["contract_count"] >= 8

    _, s_eac = pipeline.build_exposure_attribution_contracts(save=False)
    assert s_eac["exposure_contract_summary"]["contract_count"] >= 8

    _, s_lmc = pipeline.build_limit_monitoring_contracts(save=False)
    assert s_lmc["limit_contract_summary"]["contract_count"] >= 8

    _, s_m = pipeline.build_monitor_placeholders(save=False)
    assert s_m["risk_contribution"]["placeholder_count"] >= 1

    _, s_om = pipeline.build_outputs_metrics(save=False)
    assert s_om["risk_output"]["output_contract_count"] >= 1

    _, s_dg = pipeline.build_dependencies_guards(save=False)
    assert s_dg["dependency_summary"]["all_available"] is True

    _, s_de = pipeline.build_disabled_execution_reports(save=False)
    assert s_de["risk_report"]["is_disabled"] is True

    _, s_fsm = pipeline.build_findings_scoring_manifest(save=False)
    assert s_fsm["scoring"]["is_contract_ready"] is True

    _, s_hvsh = pipeline.build_health_validation_safety_handoff(save=False)
    assert s_hvsh["handoff"]["handoff_ready"] is True

    df_status, s_status = pipeline.build_risk_reporting_status(save=False)
    assert not df_status.empty
    assert s_status["pipeline_status"] == "RISK_REPORTING_CONTRACT_READY"
    assert s_status["current_phase"] == 155
    assert s_status["next_phase"] == 156
    assert s_status["target_final_phase"] == 160
