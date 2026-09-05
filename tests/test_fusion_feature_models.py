"""Tests for Fusion Feature Models."""

import pytest
from advanced_feature_fusion.fusion_feature_models import (
    FusionFeatureProfileItem,
    FusionFeatureDomain,
    FusionContract,
    FusionPolicy,
    FusionFeatureMetadata,
    FusionFeatureMatrixManifest,
    FusionValidationFinding,
    build_fusion_feature_profile_id,
    build_fusion_contract_id,
)


def test_models_instantiation():
    item = FusionFeatureProfileItem(
        profile_id="p1",
        profile_name="test_prof",
        current_phase=120,
        target_final_phase=160,
        next_phase=121,
        local_only=True,
        non_production=True,
        research_only=True,
        dry_run=True,
        non_signal=True,
        metadata_only_news=True,
        status_label="ready",
    )
    d = item.to_dict()
    assert d["profile_id"] == "p1"
    assert d["current_phase"] == 120


def test_forbidden_terms_in_metadata():
    with pytest.raises(ValueError):
        FusionFeatureMetadata(
            metadata_id="meta_1",
            feature_name="buy_signal_feature",
            fusion_family="macro",
            source_domains=["macro"],
        )


def test_id_builders():
    pid = build_fusion_feature_profile_id("Balanced Profile")
    assert pid.startswith("ff_prof_")
    cid = build_fusion_contract_id("Contract A", "macro")
    assert cid.startswith("ff_cnt_macro_")
