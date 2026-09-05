"""Unit tests for Phase 119 cross-asset alignment dataclass models and ID generators."""

import pytest
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    CrossAssetAlignmentDomain,
    AssetUniverseAlignment,
    AssetSymbolMapping,
    TimestampAlignmentContract,
    SessionCalendarAlignment,
    FeatureMatrixContract,
    FeatureMatrixJoinPolicy,
    AlignedFeatureMatrixManifest,
    CrossAssetAlignmentFinding,
    FORBIDDEN_OUTPUT_WORDS,
    build_cross_asset_alignment_domain_id,
    build_asset_universe_alignment_id,
    build_asset_symbol_mapping_id,
    build_timestamp_contract_id,
    build_session_calendar_id,
    build_feature_matrix_contract_id,
    build_join_policy_id,
    build_aligned_feature_matrix_manifest_id,
    build_cross_asset_alignment_finding_id,
)


def test_id_generators():
    assert build_cross_asset_alignment_domain_id("fx_core") == "caad_fx_core"
    assert build_asset_universe_alignment_id("fx", "EUR/USD") == "aua_fx_eur_usd"
    assert build_asset_symbol_mapping_id("fx", "EUR/USD", "macro", "US_10Y") == "asm_fx_eur_usd_to_macro_us_10y"
    assert build_timestamp_contract_id("fx_daily") == "tac_fx_daily"
    assert build_session_calendar_id("fx_24_5") == "sca_fx_24_5"
    assert build_feature_matrix_contract_id("fx_base") == "fmc_fx_base"
    assert build_join_policy_id("asof_backward") == "fmjp_asof_backward"
    assert build_aligned_feature_matrix_manifest_id("cross_domain_research") == "afmm_cross_domain_research"
    assert build_cross_asset_alignment_finding_id("rule_01", "warn") == "caaf_rule_01_warn"


def test_manifest_defaults_non_signal():
    manifest = AlignedFeatureMatrixManifest(
        manifest_id="test_id",
        matrix_name="test_matrix",
        base_domain="fx",
        aligned_domains=["macro", "commodity"],
        row_count=100,
        feature_count=10,
        join_policy="join_policy_asof_backward",
    )
    d = manifest.to_dict()
    assert d["source_preserved"] is True
    assert d["non_signal"] is True
    assert d["contains_target_or_prediction"] is False


def test_forbidden_output_words():
    assert "signal" in FORBIDDEN_OUTPUT_WORDS
    assert "buy" in FORBIDDEN_OUTPUT_WORDS
    assert "sell" in FORBIDDEN_OUTPUT_WORDS
    assert "target" in FORBIDDEN_OUTPUT_WORDS
    assert "prediction" in FORBIDDEN_OUTPUT_WORDS
