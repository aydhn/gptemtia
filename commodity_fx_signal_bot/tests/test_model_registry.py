import pytest
from ml.model_registry import ModelRegistryEntry, model_registry_entry_to_dict, build_registry_status

def test_model_registry_entry_to_dict():
    entry = ModelRegistryEntry(
        model_id="test_id",
        symbol="TEST",
        timeframe="1d",
        training_profile="test",
        dataset_profile="test",
        model_family="dummy",
        task_type="classification",
        target_column="target",
        artifact_paths={},
        metrics={},
        cv_summary={},
        leakage_audit_passed=True,
        dataset_quality_passed=True,
        model_quality_passed=True,
        registry_status="registered_candidate",
        created_at_utc="2023-01-01T00:00:00Z",
        warnings=[]
    )

    d = model_registry_entry_to_dict(entry)
    assert d["model_id"] == "test_id"

def test_build_registry_status():
    status = build_registry_status({}, {"passed": True}, {"passed": False})
    assert status == "rejected_candidate"

    status = build_registry_status({}, {"passed": False}, {"passed": True})
    assert status == "quality_failed"

    status = build_registry_status({}, {"passed": True, "warnings": ["warn"]}, {"passed": True})
    assert status == "registered_warning_candidate"

    status = build_registry_status({}, {"passed": True}, {"passed": True})
    assert status == "registered_candidate"
