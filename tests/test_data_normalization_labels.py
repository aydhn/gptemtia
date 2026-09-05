from advanced_data_normalization.data_normalization_labels import (
    list_normalization_domain_labels,
    list_normalization_status_labels,
    list_normalization_severity_labels,
    list_normalization_action_labels,
    list_normalization_dataset_type_labels,
    validate_normalization_domain_label,
    validate_normalization_status_label,
    validate_normalization_severity_label,
    validate_normalization_action_label,
    validate_normalization_dataset_type_label,
)


def test_normalization_labels():
    domains = list_normalization_domain_labels()
    assert "fx_symbol_normalization_domain" in domains
    assert "timestamp_timezone_normalization_domain" in domains
    assert validate_normalization_domain_label("fx_symbol_normalization_domain") is True
    assert validate_normalization_domain_label("invalid_domain") is False

    statuses = list_normalization_status_labels()
    assert "normalization_applied" in statuses
    assert "normalization_manual_review_required" in statuses
    assert validate_normalization_status_label("normalization_applied") is True

    sevs = list_normalization_severity_labels()
    assert "normalization_critical" in sevs
    assert validate_normalization_severity_label("normalization_high") is True

    actions = list_normalization_action_labels()
    assert "action_canonicalize_symbol" in actions
    assert validate_normalization_action_label("action_canonicalize_symbol") is True

    datasets = list_normalization_dataset_type_labels()
    assert "dataset_fx_quote" in datasets
    assert validate_normalization_dataset_type_label("dataset_fx_quote") is True
