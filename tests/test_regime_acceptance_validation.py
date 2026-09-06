"""Test suite for Phase 135 Validation Suite."""

import pytest
import pandas as pd
from advanced_regime_acceptance.regime_acceptance_profile_registry import (
    build_regime_acceptance_profile_registry,
)
from advanced_regime_acceptance.regime_block_inventory import (
    build_regime_block_inventory_report,
)
from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
)
from advanced_regime_acceptance.phase_126_135_acceptance_manifest import (
    build_phase_126_135_acceptance_manifest,
)
from advanced_regime_acceptance.regime_acceptance_validation import (
    validate_regime_acceptance_profile_registry,
    validate_regime_block_inventory,
    validate_regime_acceptance_gates,
    validate_phase_126_135_acceptance_manifest,
    validate_no_forbidden_regime_acceptance_claims,
    build_regime_acceptance_validation_report,
)


def test_validation_suite():
    df_prof, _ = build_regime_acceptance_profile_registry()
    df_inv, _ = build_regime_block_inventory_report()
    df_gates, _ = build_regime_block_acceptance_gate_registry()
    df_man, _ = build_phase_126_135_acceptance_manifest()

    assert validate_regime_acceptance_profile_registry(df_prof) is True
    assert validate_regime_block_inventory(df_inv) is True
    assert validate_regime_acceptance_gates(df_gates) is True
    assert validate_phase_126_135_acceptance_manifest(df_man) is True
    assert validate_no_forbidden_regime_acceptance_claims(df=df_man) is True

    tables = {
        "profiles": df_prof,
        "inventory": df_inv,
        "gates": df_gates,
        "manifest": df_man,
    }
    df_val, s_val = build_regime_acceptance_validation_report(tables)
    assert s_val["all_passed"] is True
    assert s_val["non_signal"] is True


def test_forbidden_claim_triggers_error():
    bad_df = pd.DataFrame([{"claim": "This system is production ready now"}])
    with pytest.raises(ValueError):
        validate_no_forbidden_regime_acceptance_claims(df=bad_df)
