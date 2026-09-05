import pytest
from advanced_factor_metadata.factor_contract_registry import build_factor_contract_registry
from advanced_factor_metadata.factor_family_registry import build_factor_family_registry
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_manifest import build_factor_metadata_manifest
from advanced_factor_metadata.factor_metadata_profile_registry import build_factor_metadata_profile_registry
from advanced_factor_metadata.factor_metadata_validation import (
    build_factor_metadata_validation_report,
    validate_factor_contract_registry,
    validate_factor_family_registry,
    validate_factor_metadata_manifest,
    validate_factor_metadata_profile_registry,
    validate_factor_namespace_registry,
    validate_factor_output_schema,
    validate_no_forbidden_factor_claims,
)
from advanced_factor_metadata.factor_namespace_registry import build_factor_namespace_registry
from advanced_factor_metadata.factor_output_schema import build_factor_output_schema_registry


def test_validation_suite():
    profile = get_default_factor_metadata_profile()
    df_prof, _ = build_factor_metadata_profile_registry(profile)
    df_fam, _ = build_factor_family_registry(profile)
    df_cntr, _ = build_factor_contract_registry(profile)
    df_ns, _ = build_factor_namespace_registry(profile)
    df_sch, _ = build_factor_output_schema_registry(profile)
    df_manf, _ = build_factor_metadata_manifest(profile)

    assert validate_factor_metadata_profile_registry(df_prof, profile)["is_valid"] is True
    assert validate_factor_family_registry(df_fam, profile)["is_valid"] is True
    assert validate_factor_contract_registry(df_cntr, profile)["is_valid"] is True
    assert validate_factor_namespace_registry(df_ns, profile)["is_valid"] is True
    assert validate_factor_output_schema(df_sch, profile)["is_valid"] is True
    assert validate_factor_metadata_manifest(df_manf, profile)["is_valid"] is True

    tables = {
        "profiles": df_prof,
        "families": df_fam,
        "contracts": df_cntr,
        "namespaces": df_ns,
        "schemas": df_sch,
        "manifests": df_manf,
    }
    df_report, summary = build_factor_metadata_validation_report(tables, profile)
    assert not df_report.empty
    assert summary["status"] == "factor_ready"
    assert summary["failed_checks"] == 0
    assert summary["all_non_signal"] is True
    assert summary["zero_forbidden_claims"] is True


def test_validate_no_forbidden_factor_claims():
    clean_summary = {"status": "factor_ready", "non_signal": True}
    res = validate_no_forbidden_factor_claims(summary=clean_summary)
    assert res["is_clean"] is True

    dirty_summary = {"status": "kesin al tavsiyesi"}
    res_dirty = validate_no_forbidden_factor_claims(summary=dirty_summary)
    assert res_dirty["is_clean"] is False
