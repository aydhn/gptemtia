from advanced_data_normalization.data_normalization_models import (
    DataNormalizationProfileItem,
    DataNormalizationDomain,
    NormalizationRule,
    CanonicalSchema,
    CanonicalField,
    NormalizationFinding,
    NormalizationDecision,
    NormalizedViewManifest,
    NormalizationScore,
    build_data_normalization_profile_id,
    build_data_normalization_domain_id,
    build_normalization_rule_id,
    build_canonical_schema_id,
    build_canonical_field_id,
    build_normalization_finding_id,
    build_normalization_decision_id,
    build_normalized_view_manifest_id,
    build_normalization_score_id,
)


def test_models_instantiation_and_dict():
    p_id = build_data_normalization_profile_id("test_prof")
    item = DataNormalizationProfileItem(
        profile_id=p_id,
        profile_name="test_prof",
        current_phase=113,
        target_final_phase=160,
        next_phase=114,
        local_only=True,
        non_production=True,
        research_only=True,
        dry_run=True,
        non_destructive=True,
        status_label="ready",
        warnings=[],
    )
    d = item.to_dict()
    assert d["profile_id"] == p_id
    assert d["non_destructive"] is True

    f_id = build_normalization_finding_id("rule1", "ds1", "col1")
    finding = NormalizationFinding(
        finding_id=f_id,
        rule_id="rule1",
        dataset_type="ds1",
        source_field="col1",
        original_value_repr="val",
        normalized_value_repr="norm_val",
        status_label="normalization_applied",
        severity_label="normalization_low",
        message="ok",
        manual_review_required=False,
    )
    assert finding.finding_id == f_id
    assert finding.to_dict()["manual_review_required"] is False

    dec_id = build_normalization_decision_id(f_id)
    dec = NormalizationDecision(
        decision_id=dec_id,
        finding_id=f_id,
        rule_id="rule1",
        decision_type="applied_canonical_mapping",
        decision_note="applied",
        source_preserved=True,
        destructive_action_allowed=False,
        lineage_required=True,
        future_phase_owner="Phase 114",
    )
    assert dec.source_preserved is True
    assert dec.destructive_action_allowed is False

    man_id = build_normalized_view_manifest_id("ds_name", "prov_name")
    manifest = NormalizedViewManifest(
        manifest_id=man_id,
        dataset_name="ds_name",
        dataset_type="dataset_fx_quote",
        provider_name="prov_name",
        original_ref="orig.csv",
        normalized_ref="norm.csv",
        schema_version="v1.0",
        row_count=10,
        normalized_field_count=2,
        source_preserved=True,
        destructive_action_allowed=False,
        manual_review_required=False,
    )
    assert manifest.source_preserved is True
    assert manifest.destructive_action_allowed is False
