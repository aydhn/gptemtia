from advanced_feature_store_integration.feature_store_integration_pipeline import (
    FeatureStoreIntegrationPipeline,
)

def test_pipeline_dry_run_no_save():
    pipeline = FeatureStoreIntegrationPipeline()
    t1, s1 = pipeline.build_profiles_domains_contracts(save=False)
    assert "profiles" in t1 and "domains" in t1 and "contracts" in t1

    t2, s2 = pipeline.build_entity_feature_factor_registries(save=False)
    assert "entities" in t2 and "features" in t2 and "factors" in t2

    t3, s3 = pipeline.build_schema_version_partition_lineage(save=False)
    assert "namespace" in t3 and "schemas" in t3 and "version" in t3

    t4, s4 = pipeline.build_validation_quality_drift_review(save=False)
    assert "validation" in t4 and "quality" in t4

    t5, s5 = pipeline.build_manifest_read_write_query_policies(save=False)
    assert "manifest" in t5 and "read_contracts" in t5

    t6, s6 = pipeline.build_catalog_reports(save=False)
    assert "feature_catalog" in t6 and "factor_catalog" in t6

    t7, s7 = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in t7 and "validation" in t7 and "handoff" in t7

    df_stat, s_stat = pipeline.build_feature_store_integration_status(save=False)
    assert not df_stat.empty
    assert s_stat["overall_status"] == "READY"
