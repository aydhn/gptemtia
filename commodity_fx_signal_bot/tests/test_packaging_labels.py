from portable_packaging.packaging_labels import (
    list_packaging_artifact_labels,
    list_install_verification_labels,
    list_packaging_safety_labels,
    list_environment_drift_labels,
    validate_packaging_artifact_label,
    validate_install_verification_label
)

def test_lists_not_empty():
    assert len(list_packaging_artifact_labels()) > 0
    assert len(list_install_verification_labels()) > 0
    assert len(list_packaging_safety_labels()) > 0
    assert len(list_environment_drift_labels()) > 0

def test_validate_labels():
    validate_packaging_artifact_label("source_artifact")
    validate_install_verification_label("install_check_passed")
