"""Tests for Phase 132 Macro/Event/News Regime Validation."""

import pandas as pd
from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.macro_event_news_regime_validation import (
    validate_macro_event_news_regime_profile_registry,
    validate_macro_event_news_entity_registries,
    validate_metadata_only_news_boundary,
    validate_macro_event_news_context_contracts,
    validate_macro_event_news_regime_context_manifest,
    validate_no_forbidden_macro_event_news_claims,
    build_macro_event_news_regime_validation_report,
)
from advanced_macro_event_news_regime.macro_event_news_regime_profile_registry import (
    build_macro_event_news_regime_profile_registry,
)
from advanced_macro_event_news_regime.metadata_only_news_boundary import (
    build_metadata_only_news_boundary_registry,
)
from advanced_macro_event_news_regime.macro_event_news_regime_context_contracts import (
    build_macro_event_news_regime_context_contract_registry,
)
from advanced_macro_event_news_regime.macro_event_news_regime_context_manifest import (
    build_macro_event_news_regime_context_manifest,
)


def test_validate_profile_registry():
    prof = get_macro_event_news_regime_profile()
    df, _ = build_macro_event_news_regime_profile_registry(prof)
    res = validate_macro_event_news_regime_profile_registry(df, prof)
    assert res["valid"] is True
    assert res["status"] == "PASS"


def test_validate_boundary_table():
    prof = get_macro_event_news_regime_profile()
    df, _ = build_metadata_only_news_boundary_registry(prof)
    res = validate_metadata_only_news_boundary(df, prof)
    assert res["valid"] is True
    assert res["status"] == "PASS"


def test_validate_contracts_table():
    prof = get_macro_event_news_regime_profile()
    df, _ = build_macro_event_news_regime_context_contract_registry(prof)
    res = validate_macro_event_news_context_contracts(df, prof)
    assert res["valid"] is True


def test_validate_manifest_table():
    prof = get_macro_event_news_regime_profile()
    df, _ = build_macro_event_news_regime_context_manifest(prof)
    res = validate_macro_event_news_regime_context_manifest(df, prof)
    assert res["valid"] is True


def test_validate_no_forbidden_claims():
    clean_text = "Phase 132 dry run offline research context."
    res_clean = validate_no_forbidden_macro_event_news_claims(text=clean_text)
    assert res_clean["valid"] is True

    dirty_text = "We provide official approval and investment advice with trained models."
    res_dirty = validate_no_forbidden_macro_event_news_claims(text=dirty_text)
    assert res_dirty["valid"] is False


def test_build_validation_report():
    prof = get_macro_event_news_regime_profile()
    p_df, _ = build_macro_event_news_regime_profile_registry(prof)
    b_df, _ = build_metadata_only_news_boundary_registry(prof)
    c_df, _ = build_macro_event_news_regime_context_contract_registry(prof)
    m_df, _ = build_macro_event_news_regime_context_manifest(prof)

    tables = {
        "profiles": p_df,
        "boundary": b_df,
        "contracts": c_df,
        "manifest": m_df,
    }
    df, summary = build_macro_event_news_regime_validation_report(tables, prof)
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["failed_checks"] == 0
    assert summary["all_non_signal"] is True
