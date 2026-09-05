from advanced_regime_rule_free.regime_rule_free_pipeline import RegimeRuleFreePipeline
from advanced_regime_rule_free.regime_rule_free_validation import (
    validate_regime_rule_free_profile_registry,
    validate_rule_free_labeling_contracts,
    validate_candidate_state_schema,
    validate_unsupervised_prep_contracts,
    validate_candidate_state_integrity_manifest,
    validate_no_forbidden_rule_free_claims,
    build_regime_rule_free_validation_report,
)


def test_build_regime_rule_free_validation_report():
    pipeline = RegimeRuleFreePipeline()
    p_tables, _ = pipeline.build_profiles_domains_contracts(save=False)
    s_tables, _ = pipeline.build_candidate_state_schemas(save=False)
    u_tables, _ = pipeline.build_unsupervised_prep_registries(save=False)
    m_tables, _ = pipeline.build_policies_review_manifest(save=False)

    val_input = {**p_tables, **s_tables, **u_tables, **m_tables}
    df_val, summary = build_regime_rule_free_validation_report(val_input)

    assert len(df_val) == 6
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["total_checks"] == 6
    assert summary["passed_checks"] == 6
    assert summary["failed_checks"] == 0
    assert summary["forbidden_claims_clean"] is True
    assert summary["zero_execution_clean"] is True


def test_individual_validators():
    pipeline = RegimeRuleFreePipeline()
    p_tables, _ = pipeline.build_profiles_domains_contracts(save=False)
    s_tables, _ = pipeline.build_candidate_state_schemas(save=False)
    u_tables, _ = pipeline.build_unsupervised_prep_registries(save=False)
    m_tables, _ = pipeline.build_policies_review_manifest(save=False)

    assert validate_regime_rule_free_profile_registry(p_tables["profiles"])["is_valid"] is True
    assert validate_rule_free_labeling_contracts(p_tables["labeling_contracts"])["is_valid"] is True
    assert validate_candidate_state_schema(s_tables["candidate_state_schema"])["is_valid"] is True
    assert validate_unsupervised_prep_contracts(u_tables["unsupervised_prep"])["is_valid"] is True
    assert validate_candidate_state_integrity_manifest(m_tables["integrity_manifest"])["is_valid"] is True
