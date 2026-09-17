# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Validation."""

from advanced_final_hardening.final_hardening_validation import (
    validate_final_hardening_profile_registry,
    validate_final_hardening_contracts,
    validate_operator_runbook_contracts,
    validate_release_candidate_contracts,
    validate_release_candidate_manifest,
    validate_no_forbidden_release_candidate_claims,
    build_final_hardening_validation_report,
)
from advanced_final_hardening.final_hardening_profile_registry import (
    build_final_hardening_profile_registry,
)
from advanced_final_hardening.final_hardening_contracts import (
    build_final_hardening_contract_registry,
)
from advanced_final_hardening.operator_runbook_contracts import (
    build_operator_runbook_contract_registry,
)
from advanced_final_hardening.release_candidate_contracts import (
    build_release_candidate_contract_registry,
)
from advanced_final_hardening.release_candidate_manifest import (
    build_release_candidate_manifest,
)


def test_validation_functions():
    df_p, _ = build_final_hardening_profile_registry()
    df_c, _ = build_final_hardening_contract_registry()
    df_rb, _ = build_operator_runbook_contract_registry()
    df_rc, _ = build_release_candidate_contract_registry()
    df_mnf, _ = build_release_candidate_manifest()

    assert validate_final_hardening_profile_registry(df_p)["passed"] is True
    assert validate_final_hardening_contracts(df_c)["passed"] is True
    assert validate_operator_runbook_contracts(df_rb)["passed"] is True
    assert validate_release_candidate_contracts(df_rc)["passed"] is True
    assert validate_release_candidate_manifest(df_mnf)["passed"] is True
    assert validate_no_forbidden_release_candidate_claims(df=df_mnf)["passed"] is True

    val_tables = {
        "profiles": df_p,
        "contracts": df_c,
        "runbooks": df_rb,
        "rc_contracts": df_rc,
        "manifest": df_mnf,
    }
    df_val, s_val = build_final_hardening_validation_report(val_tables)
    assert s_val["all_passed"] is True
    assert s_val["validation_status"] == "VALIDATION_PASS"
