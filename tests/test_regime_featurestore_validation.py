import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_validation import (
    validate_regime_featurestore_profile_registry,
    validate_regime_featurestore_contract_registry,
    validate_regime_featurestore_schema_registry,
    validate_regime_component_store_catalogs,
    validate_regime_featurestore_metadata_manifest,
    build_regime_featurestore_validation_report,
    summarize_regime_featurestore_validation,
)
from advanced_regime_featurestore_integration.regime_featurestore_profile_registry import (
    build_regime_featurestore_profile_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_contracts import (
    build_regime_featurestore_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_schema import (
    build_regime_featurestore_schema_registry,
)
from advanced_regime_featurestore_integration.regime_taxonomy_store_catalog import (
    build_regime_taxonomy_store_catalog,
)
from advanced_regime_featurestore_integration.regime_featurestore_metadata_manifest import (
    build_regime_featurestore_metadata_manifest,
)


def test_validation_functions():
    p_df, _ = build_regime_featurestore_profile_registry()
    p_res = validate_regime_featurestore_profile_registry(p_df)
    assert p_res["passed"] is True

    c_df, _ = build_regime_featurestore_contract_registry()
    c_res = validate_regime_featurestore_contract_registry(c_df)
    assert c_res["passed"] is True

    s_df, _ = build_regime_featurestore_schema_registry()
    s_res = validate_regime_featurestore_schema_registry(s_df)
    assert s_res["passed"] is True

    tax_df, _ = build_regime_taxonomy_store_catalog()
    cat_res = validate_regime_component_store_catalogs({"taxonomy": tax_df})
    assert cat_res["passed"] is True

    m_df, _ = build_regime_featurestore_metadata_manifest()
    m_res = validate_regime_featurestore_metadata_manifest(m_df)
    assert m_res["passed"] is True


def test_build_regime_featurestore_validation_report():
    p_df, _ = build_regime_featurestore_profile_registry()
    c_df, _ = build_regime_featurestore_contract_registry()
    s_df, _ = build_regime_featurestore_schema_registry()
    tax_df, _ = build_regime_taxonomy_store_catalog()
    m_df, _ = build_regime_featurestore_metadata_manifest()

    input_tables = {
        "profiles": p_df,
        "contracts": c_df,
        "schema": s_df,
        "catalogs": {"taxonomy": tax_df},
        "manifest": m_df,
    }

    df, summary = build_regime_featurestore_validation_report(input_tables)
    assert isinstance(df, pd.DataFrame)
    assert summary["all_passed"] is True
    assert summary["failed_checks"] == 0
    assert summary["current_phase"] == 134


def test_summarize_regime_featurestore_validation():
    input_tables = {
        "profiles": build_regime_featurestore_profile_registry()[0],
        "contracts": build_regime_featurestore_contract_registry()[0],
        "schema": build_regime_featurestore_schema_registry()[0],
        "catalogs": {"taxonomy": build_regime_taxonomy_store_catalog()[0]},
        "manifest": build_regime_featurestore_metadata_manifest()[0],
    }
    df, _ = build_regime_featurestore_validation_report(input_tables)
    summary = summarize_regime_featurestore_validation(df)
    assert summary["all_passed"] is True
