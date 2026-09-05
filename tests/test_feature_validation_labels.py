import pytest
from advanced_feature_validation.feature_validation_labels import (
    FEATURE_VALIDATION_LABELS,
    get_feature_validation_label,
)


def test_feature_validation_labels():
    assert "phase_name" in FEATURE_VALIDATION_LABELS
    assert FEATURE_VALIDATION_LABELS["current_phase"] == 121
    assert FEATURE_VALIDATION_LABELS["target_final_phase"] == 160
    assert FEATURE_VALIDATION_LABELS["next_phase"] == 122
    assert get_feature_validation_label("current_phase") == 121
    assert get_feature_validation_label("non_existent", "default_val") == "default_val"
