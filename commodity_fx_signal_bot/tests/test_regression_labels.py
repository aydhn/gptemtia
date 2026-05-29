import pytest
from scenario_regression.regression_labels import (
    list_regression_type_labels, list_regression_status_labels,
    list_snapshot_diff_labels, list_replay_status_labels, list_acceptance_labels,
    validate_regression_type, validate_acceptance_label
)

def test_labels_not_empty():
    assert len(list_regression_type_labels()) > 0
    assert len(list_acceptance_labels()) > 0

def test_validate_labels():
    validate_regression_type("golden_output_regression")
    validate_acceptance_label("demo_accepted_offline")

    with pytest.raises(ValueError):
        validate_regression_type("invalid_label")
