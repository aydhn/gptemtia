"""Tests for Phase 131 Cross-Asset Regime Models."""

from advanced_cross_asset_regime_context.cross_asset_regime_models import (
    CrossAssetRegimeProfileItem,
    CrossAssetRegimeEntity,
    CrossAssetRegimePair,
    CrossAssetRelationshipTaxonomyItem,
    CrossAssetContextContract,
    CrossAssetContextFinding,
    CrossAssetContextScore,
    CrossAssetRegimeManifest,
    CrossAssetManualReviewItem,
)


def test_entity_model_instantiation():
    rec = CrossAssetRegimeEntity(
        entity_id="USDTRY",
        entity_name="USD/TRY",
        entity_type="fx_pair",
        domain="fx_usdtry",
        base_currency_or_asset="USD",
        quote_or_benchmark="TRY",
        source_phase=126,
        readiness_status="ready",
    )
    assert rec.entity_id == "USDTRY"
    assert rec.non_signal is True
    assert rec.source_preserved is True


def test_pair_model_instantiation():
    pair = CrossAssetRegimePair(
        pair_id="pair_usdtry_xauusd",
        left_entity_id="USDTRY",
        left_entity_type="fx_pair",
        right_entity_id="XAUUSD",
        right_entity_type="commodity_symbol",
        relationship_category="fx_commodity_linkage",
        timestamp_alignment_policy="backward_asof",
        asof_join_policy="exact_or_backward",
    )
    assert pair.pair_id == "pair_usdtry_xauusd"
    assert pair.non_signal is True


def test_manifest_model_instantiation():
    manifest = CrossAssetRegimeManifest(
        manifest_name="cross_asset_regime_context_manifest",
        current_phase=131,
        target_final_phase=160,
        next_phase=132,
    )
    assert manifest.manifest_status == "MANIFEST_VALID"
    assert manifest.current_phase == 131
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 132
    assert manifest.non_signal is True
