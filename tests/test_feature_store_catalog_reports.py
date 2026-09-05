from advanced_feature_store_integration.feature_store_catalog_reports import (
    build_feature_store_feature_catalog_report,
    build_feature_store_factor_catalog_report,
    build_feature_store_quality_drift_catalog_report,
    build_feature_store_validation_catalog_report,
    summarize_feature_store_catalog_report,
)

def test_catalog_reports():
    df_fc, s_fc = build_feature_store_feature_catalog_report()
    assert not df_fc.empty
    assert s_fc["total_features"] >= 9

    df_fac, s_fac = build_feature_store_factor_catalog_report()
    assert not df_fac.empty
    assert s_fac["total_factors"] >= 6

    df_qd, s_qd = build_feature_store_quality_drift_catalog_report()
    assert not df_qd.empty
    assert s_qd["total_items"] >= 6

    df_vc, s_vc = build_feature_store_validation_catalog_report()
    assert not df_vc.empty
    assert s_vc["total_validations"] >= 5
