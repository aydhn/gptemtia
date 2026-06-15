from artifact_metadata.metadata_labels import (
    list_artifact_type_labels, list_card_type_labels, list_metadata_status_labels,
    list_artifact_use_labels, list_reproducibility_labels,
    validate_artifact_type, validate_card_type
)

def test_label_lists_not_empty():
    assert len(list_artifact_type_labels()) > 0
    assert len(list_card_type_labels()) > 0
    assert len(list_metadata_status_labels()) > 0
    assert len(list_artifact_use_labels()) > 0
    assert len(list_reproducibility_labels()) > 0

def test_validate_artifact_type():
    validate_artifact_type("model_artifact")

def test_validate_card_type():
    validate_card_type("model_card")

def test_metadata_complete_not_deployment_approval():
    assert "metadata_complete" in list_metadata_status_labels()
    assert "deployment_approval" not in list_metadata_status_labels()
