# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Validation Report."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_profile_registry import (
    build_stress_testing_profile_registry,
)
from advanced_stress_testing.stress_scenario_contracts import (
    build_stress_scenario_contract_registry,
)
from advanced_stress_testing.stress_testing_manifest import (
    build_stress_testing_manifest,
)
from advanced_stress_testing.stress_testing_validation import (
    build_stress_testing_validation_report,
    validate_no_forbidden_stress_claims,
)


def test_validation():
    prof = get_default_stress_testing_profile()
    df_prof, _ = build_stress_testing_profile_registry(prof)
    df_core, _ = build_stress_scenario_contract_registry(prof)
    df_man, _ = build_stress_testing_manifest(prof)
    tables = {"profiles": df_prof, "contracts": df_core, "manifest": df_man}

    df_val, summary = build_stress_testing_validation_report(tables, prof)
    assert not df_val.empty
    assert summary["validation_status"] == "PASS"
    assert summary["all_passed"] is True

    claim_res = validate_no_forbidden_stress_claims("clean text without claims")
    assert claim_res["is_clean"] is True
