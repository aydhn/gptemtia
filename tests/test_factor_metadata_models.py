import pytest
from advanced_factor_metadata.factor_metadata_models import (
    FactorContract,
    FactorDependency,
    FactorFamily,
    FactorInputFeatureSet,
    FactorManualReviewItem,
    FactorMetadataManifest,
    FactorMetadataProfileItem,
    build_factor_contract_id,
    build_factor_dependency_id,
    build_factor_family_id,
    build_factor_input_feature_set_id,
    build_factor_manual_review_id,
    build_factor_metadata_manifest_id,
    build_factor_metadata_profile_id,
)


def test_factor_metadata_models_and_invariants():
    prof = FactorMetadataProfileItem(
        profile_id=build_factor_metadata_profile_id("balanced"),
        profile_name="balanced",
    )
    assert prof.non_signal is True
    assert prof.current_phase == 122

    fam = FactorFamily(
        family_id=build_factor_family_id("trend"),
        family_label="factor_family_trend",
        family_name="Trend",
        description="Trend family",
    )
    assert fam.manual_review_required is False

    cntr = FactorContract(
        contract_id=build_factor_contract_id("factor_trend", "trend"),
        factor_name="factor_trend",
        factor_family="trend",
        required_feature_sets=["fset_sma"],
    )
    assert cntr.non_signal is True
    assert cntr.namespace.startswith("factor_")

    fset = FactorInputFeatureSet(
        feature_set_id=build_factor_input_feature_set_id("factor_trend"),
        factor_name="factor_trend",
        factor_family="trend",
        required_features=["sma_20"],
    )
    assert fset.non_signal is True
    assert fset.validation_required is True

    dep = FactorDependency(
        dependency_id=build_factor_dependency_id("factor_trend", "sma_grid"),
        factor_name="factor_trend",
        dependency_type="grid",
        dependency_ref="sma_grid",
        source_phase="Phase 118",
        dependency_note="test note",
    )
    assert dep.mandatory is True

    manf = FactorMetadataManifest(
        manifest_id=build_factor_metadata_manifest_id("factor_trend"),
        factor_name="factor_trend",
        factor_family="trend",
    )
    assert manf.non_signal is True
    assert manf.contains_target_or_prediction is False
    assert manf.contains_trading_recommendation is False
    assert manf.source_preserved is True

    rev = FactorManualReviewItem(
        review_id=build_factor_manual_review_id("factor_quote", "liquidity"),
        factor_name="factor_quote",
        factor_family="quote_microstructure",
        review_reason="liquidity",
        suggested_action="check",
    )
    assert rev.destructive_action_allowed is False
