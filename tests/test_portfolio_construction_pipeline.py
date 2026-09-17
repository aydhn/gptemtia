# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Pipeline, Integrations, and Handoff."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_construction_pipeline import (
    PortfolioConstructionPipeline,
    run_portfolio_construction_pipeline,
)
from advanced_portfolio_construction.portfolio_construction_report_builder import (
    build_portfolio_construction_disclaimer,
    build_portfolio_construction_profile_markdown_report,
    build_portfolio_construction_contracts_markdown_report,
    build_position_sizing_contracts_markdown_report,
    build_risk_budget_contracts_markdown_report,
    build_findings_markdown_report,
    build_readiness_score_markdown_report,
    build_manifest_markdown_report,
    build_phase_154_handoff_markdown_report,
)
from advanced_portfolio_construction.phase_154_handoff import (
    build_phase_154_handoff_report,
)
from advanced_portfolio_construction.portfolio_construction_safety_boundary import (
    build_portfolio_construction_safety_boundary_report,
)
from advanced_portfolio_construction.portfolio_construction_health import (
    build_portfolio_construction_health_check,
)
from advanced_portfolio_construction.portfolio_construction_validation import (
    validate_portfolio_construction_invariants,
)
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore


def test_pipeline_run_all():
    results = run_portfolio_construction_pipeline(save_artifacts=False)
    assert len(results) >= 70
    assert "profiles" in results
    assert "contracts" in results
    assert "position_sizing" in results
    assert "risk_budget" in results
    assert "concentration_limits" in results
    assert "exposure_limits" in results
    assert "findings" in results
    assert "readiness_score" in results
    assert "manifest" in results
    assert "handoff_phase_154" in results


def test_pipeline_class_methods():
    pipeline = PortfolioConstructionPipeline()
    dfs_prof, s_prof = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in dfs_prof
    assert s_prof["profiles"]["status"] == "portfolio_contract_ready"

    dfs_stat, s_stat = pipeline.build_portfolio_construction_status(save=False)
    assert s_stat["current_phase"] == 153
    assert s_stat["next_phase"] == 154
    assert s_stat["target_final_phase"] == 160
    assert s_stat["status"] == "PORTFOLIO_CONTRACT_READY"


def test_phase_154_handoff():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_phase_154_handoff_report(profile)
    assert len(df) == 8
    assert summary["all_satisfied"] is True
    assert summary["source_phase"] == 153
    assert summary["target_phase"] == 154
    assert summary["target_final_phase"] == 160
    assert summary["status"] == "HANDOFF_READY"


def test_report_builder_disclaimer_and_markdown():
    disclaimer = build_portfolio_construction_disclaimer()
    assert "PHASE 153 PORTFOLIO CONSTRUCTION CONTRACT REPORT" in disclaimer
    assert "YASAL UYARI VE GÜVENLİK BİLDİRİMİ" in disclaimer

    summary = {
        "active_profile": "test_profile",
        "total_profiles": 1,
        "total_contracts": 5,
        "total_models": 4,
        "total_rules": 6,
        "total_findings": 2,
        "critical_count": 0,
        "overall_score": 1.0,
        "classification": "portfolio_construction_contract_ready_non_production",
        "manifest_id": "MNF-153-001",
        "source_phase": 153,
        "target_phase": 154,
        "target_final_phase": 160,
    }
    assert "Portfolio Construction Profile Registry" in build_portfolio_construction_profile_markdown_report(summary)
    assert "Portfolio Construction Contracts" in build_portfolio_construction_contracts_markdown_report(summary)
    assert "Position Sizing Contracts" in build_position_sizing_contracts_markdown_report(summary)
    assert "Risk Budget Contracts" in build_risk_budget_contracts_markdown_report(summary)
    assert "Portfolio Construction Findings" in build_findings_markdown_report(summary)
    assert "Portfolio Construction Readiness Score" in build_readiness_score_markdown_report(summary)
    assert "Portfolio Construction Master Manifest" in build_manifest_markdown_report(summary)
    assert "Phase 154 Handoff Report" in build_phase_154_handoff_markdown_report(summary)


def test_safety_health_validation():
    profile = get_default_portfolio_construction_profile()
    df_saf, s_saf = build_portfolio_construction_safety_boundary_report(profile)
    assert s_saf["all_enforced"] is True
    assert s_saf["no_go_count"] >= 10

    df_hlth, s_hlth = build_portfolio_construction_health_check(profile=profile)
    assert s_hlth["all_healthy"] is True

    df_val, s_val = validate_portfolio_construction_invariants(profile)
    assert s_val["all_passed"] is True


def test_data_lake_and_feature_store_integration():
    lake = DataLake()
    fs = FeatureStore(data_lake=lake)

    assert hasattr(lake, "save_portfolio_construction_table")
    assert hasattr(lake, "load_portfolio_construction_table")
    assert hasattr(lake, "save_portfolio_construction_manifest")
    assert hasattr(lake, "save_phase_154_handoff")
    assert hasattr(lake, "load_phase_154_handoff")

    assert hasattr(fs, "load_portfolio_construction_profile_registry")
    assert hasattr(fs, "load_portfolio_construction_contract_registry")
    assert hasattr(fs, "load_position_sizing_contract_registry")
    assert hasattr(fs, "load_risk_budget_contract_registry")
    assert hasattr(fs, "load_phase_154_handoff")
