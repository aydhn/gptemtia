from advanced_feature_factor_acceptance.feature_factor_acceptance_validation import (
    validate_feature_factor_acceptance_profile_registry,
    validate_feature_engine_block_inventory,
    validate_feature_engine_block_acceptance_gates,
    validate_phase_116_125_acceptance_manifest,
    validate_no_forbidden_acceptance_claims,
    build_feature_factor_acceptance_validation_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_profile_registry import (
    build_feature_factor_acceptance_profile_registry,
)
from advanced_feature_factor_acceptance.feature_engine_block_inventory import (
    build_feature_engine_block_inventory_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
)
from advanced_feature_factor_acceptance.phase_116_125_acceptance_manifest import (
    build_phase_116_125_acceptance_manifest,
)

def test_feature_factor_acceptance_validation():
    df_prof, _ = build_feature_factor_acceptance_profile_registry()
    v_prof = validate_feature_factor_acceptance_profile_registry(df_prof)
    assert v_prof["valid"] is True

    df_inv, _ = build_feature_engine_block_inventory_report()
    v_inv = validate_feature_engine_block_inventory(df_inv)
    assert v_inv["valid"] is True

    df_gates, _ = build_feature_engine_block_acceptance_gate_registry()
    v_gates = validate_feature_engine_block_acceptance_gates(df_gates)
    assert v_gates["valid"] is True

    df_man, _ = build_phase_116_125_acceptance_manifest()
    v_man = validate_phase_116_125_acceptance_manifest(df_man)
    assert v_man["valid"] is True

    clean_claim = validate_no_forbidden_acceptance_claims(text="Acceptance report and readiness gate verification")
    assert clean_claim["valid"] is True
    assert clean_claim["violations_found"] == 0

    dirty_claim = validate_no_forbidden_acceptance_claims(text="This produces a buy signal with guaranteed profit")
    assert dirty_claim["valid"] is False
    assert dirty_claim["violations_found"] > 0

    tables = {
        "profiles": df_prof,
        "inventory": df_inv,
        "gates": df_gates,
        "manifest": df_man,
    }
    df_val, s_val = build_feature_factor_acceptance_validation_report(tables)
    assert s_val["validation_status"] == "VALIDATION_PASS"
    assert s_val["forbidden_claims_detected"] == 0
    assert s_val["non_signal"] is True
