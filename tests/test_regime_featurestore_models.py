"""Tests for Phase 134 Regime FeatureStore Models."""

from advanced_regime_featurestore_integration.regime_featurestore_models import (
    RegimeFeatureStoreProfileItem,
    RegimeFeatureStoreContract,
    RegimeFeatureStoreEntity,
    RegimeFeatureStoreSchemaItem,
    RegimeStoreCatalogItem,
    RegimeAcceptedReferenceItem,
    RegimeLineageReference,
    RegimeManualReviewBlockerStoreItem,
    RegimeFeatureStoreMetadataManifest,
)


def test_models_instantiation_and_invariants():
    prof = RegimeFeatureStoreProfileItem(
        profile_name="test_profile",
        description="test description",
    )
    assert prof.non_signal is True
    assert prof.source_preserved is True
    assert prof.official_approval is False
    assert prof.production_ready is False
    assert prof.broker_ready is False

    contract = RegimeFeatureStoreContract(
        contract_name="test_contract",
        store_entity_type="store_entity_regime_taxonomy",
        entity_keys=["id"],
        timestamp_field="timestamp_utc",
        namespace_policy_ref="ns_ref",
        schema_policy_ref="schema_ref",
    )
    assert contract.non_signal_required is True
    assert contract.source_preservation_required is True
    assert contract.production_ready is False
    assert contract.broker_ready is False

    manifest = RegimeFeatureStoreMetadataManifest(
        manifest_name="test_manifest",
    )
    assert manifest.non_signal is True
    assert manifest.source_preserved is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.contains_target_or_prediction is False
    assert manifest.contains_trading_recommendation is False
    assert manifest.contains_full_article_text is False
    assert manifest.contains_embedding is False
    assert manifest.sentiment_model_output is False
    assert manifest.model_training_executed is False
    assert manifest.clustering_executed is False
