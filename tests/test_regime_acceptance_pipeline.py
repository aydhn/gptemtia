"""Test suite for Phase 135 Regime Acceptance Pipeline."""

from pathlib import Path
from advanced_regime_acceptance.regime_acceptance_pipeline import (
    RegimeAcceptancePipeline,
)


def test_pipeline_dry_run_no_save():
    root = Path(__file__).resolve().parent.parent
    pipeline = RegimeAcceptancePipeline(project_root=root)

    t1, s1 = pipeline.build_profiles_domains_inventory(save=False)
    assert "profiles" in t1
    assert "domains" in t1
    assert "inventory" in t1

    t2, s2 = pipeline.build_dependencies_gates_scoring(save=False)
    assert "dependencies" in t2
    assert "gates" in t2
    assert "scoring" in t2
    assert "manual_review" in t2

    t3, s3 = pipeline.build_compliance_and_safety(save=False)
    assert "safety" in t3
    assert "non_signal" in t3
    assert "no_lookahead" in t3
    assert "news_metadata_only" in t3
    assert "forbidden_columns" in t3
    assert "source_preservation" in t3
    assert "featurestore_readiness" in t3

    t4, s4 = pipeline.build_component_acceptance(save=False)
    assert "component_acceptance" in t4

    t5, s5 = pipeline.build_contract_reports(save=False)
    assert "documentation" in t5
    assert "scripts" in t5
    assert "tests" in t5

    t6, s6 = pipeline.build_manifest_and_handoff(save=False)
    assert "status" in t6
    assert "manifest" in t6
    assert "handoff" in t6

    t7, s7 = pipeline.build_health_validation_status(save=False)
    assert "health" in t7
    assert "validation" in t7

    result = pipeline.run_full_acceptance_pipeline(save=False)
    assert result["non_signal"] is True
    assert result["official_approval"] is False
    assert result["production_ready"] is False
    assert result["broker_ready"] is False
    assert result["total_modules"] == 10
    assert result["total_gates"] == 17
