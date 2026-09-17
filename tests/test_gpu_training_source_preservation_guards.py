"""Test suite for Phase 139 GPU Training Source Preservation Guards."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_source_preservation_guards import (
    build_gpu_training_source_preservation_guard_registry,
    summarize_gpu_training_source_preservation_guards,
    validate_gpu_training_source_preservation_action,
)


def test_build_gpu_training_source_preservation_guard_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_source_preservation_guard_registry(profile)

    assert len(df) == 3
    assert summary["total_guards"] == 3
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_gpu_training_source_preservation_action():
    safe_res = validate_gpu_training_source_preservation_action("read_parquet_metadata_only")
    assert safe_res["is_safe"] is True
    assert safe_res["blocked"] is False
    assert safe_res["status"] == "SAFE_OPERATION"

    destructive_actions = [
        "overwrite_lake_table",
        "delete_file",
        "destructive_clean",
        "auto_drop",
        "drop_na_in_place",
        "wipe_catalog",
    ]
    for act in destructive_actions:
        res = validate_gpu_training_source_preservation_action(act)
        assert res["is_safe"] is False
        assert res["blocked"] is True
        assert res["status"] == "BLOCKED_DESTRUCTIVE"
