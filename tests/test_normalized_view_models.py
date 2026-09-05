from advanced_data_normalization.normalized_view_models import (
    create_normalized_view_manifest,
    build_normalized_view_registry,
    summarize_normalized_view_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalized_view_models():
    m = create_normalized_view_manifest(
        dataset_name="fx_test",
        dataset_type="dataset_fx_quote",
        provider_name="prov",
        original_ref="orig.csv",
        normalized_ref="norm.csv",
        schema_version="v1.0",
        row_count=100,
        normalized_field_count=5,
    )
    assert m.source_preserved is True
    assert m.destructive_action_allowed is False

    prof = get_default_data_normalization_profile()
    df, summary = build_normalized_view_registry([m], prof)
    assert len(df) == 1
    assert summary["all_source_preserved"] is True
    assert summary["destructive_actions_prevented"] is True
