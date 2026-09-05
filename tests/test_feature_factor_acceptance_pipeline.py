from advanced_feature_factor_acceptance.feature_factor_acceptance_pipeline import (
    FeatureFactorAcceptancePipeline,
)

def test_feature_factor_acceptance_pipeline_dry_run():
    pipeline = FeatureFactorAcceptancePipeline()

    t1, s1 = pipeline.build_profiles_domains_inventory(save=False)
    assert "profiles" in t1 and "domains" in t1 and "inventory" in t1
    assert s1["inventory"]["total_modules"] == 10

    t2, s2 = pipeline.build_dependencies_gates_scoring(save=False)
    assert "dependencies" in t2 and "gates" in t2 and "scoring" in t2
    assert s2["gates"]["all_passed"] is True
    assert s2["scoring"]["overall_score"] >= 0.9

    t3, s3 = pipeline.build_compliance_and_safety(save=False)
    assert "safety" in t3 and "non_signal" in t3 and "no_lookahead" in t3
    assert s3["non_signal"]["compliant_modules"] == 10

    t4, s4 = pipeline.build_contract_reports(save=False)
    assert "documentation" in t4 and "scripts" in t4 and "tests" in t4

    t5, s5 = pipeline.build_manifest_and_handoff(save=False)
    assert "status" in t5 and "manifest" in t5 and "handoff" in t5
    assert s5["status"]["overall_status"] == "ACCEPTANCE_PASS"
    assert s5["handoff"]["handoff_status"] == "READY"

    t6, s6 = pipeline.build_health_validation_status(save=False)
    assert "health" in t6 and "validation" in t6
    assert s6["health"]["health_status"] == "HEALTHY"
    assert s6["validation"]["validation_status"] == "VALIDATION_PASS"

    res = pipeline.run_full_acceptance_pipeline(save=False)
    assert res["overall_status"] == "ACCEPTANCE_PASS"
    assert res["non_signal"] is True
    assert res["official_approval"] is False
    assert res["production_ready"] is False
    assert res["broker_ready"] is False
