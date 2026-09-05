"""Tests for Cross-Asset Regime Validation."""

import pandas as pd
from advanced_cross_asset_regime_context.cross_asset_regime_validation import (
    build_cross_asset_regime_validation_report,
    validate_no_forbidden_cross_asset_claims,
)
from advanced_cross_asset_regime_context.cross_asset_regime_profile_registry import (
    build_cross_asset_regime_profile_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_pairs import (
    build_cross_asset_regime_pair_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_context_contracts import (
    build_cross_asset_regime_context_contract_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_context_manifest import (
    build_cross_asset_regime_context_manifest,
)


def test_build_cross_asset_regime_validation_report():
    tables = {
        "profiles": build_cross_asset_regime_profile_registry()[0],
        "pairs": build_cross_asset_regime_pair_registry()[0],
        "contracts": build_cross_asset_regime_context_contract_registry()[0],
        "manifest": build_cross_asset_regime_context_manifest()[0],
    }
    df, summary = build_cross_asset_regime_validation_report(tables)
    assert len(df) >= 4
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["all_passed"] is True
    assert summary["forbidden_claims_clean"] is True


def test_validate_no_forbidden_cross_asset_claims():
    clean_text = "This is a non-signal local offline research experiment with official_approval: False"
    res = validate_no_forbidden_cross_asset_claims(text=clean_text)
    assert res["clean"] is True

    dirty_text = "We guarantee production-ready live trading signal with broker-ready execution"
    res_dirty = validate_no_forbidden_cross_asset_claims(text=dirty_text)
    assert res_dirty["clean"] is False
    assert len(res_dirty["violations"]) > 0
