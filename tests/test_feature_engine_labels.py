from advanced_feature_engine.feature_engine_labels import (
    list_feature_domain_labels,
    list_feature_type_labels,
    list_feature_status_labels,
    list_feature_dataset_labels,
    validate_feature_domain_label,
    validate_feature_type_label,
    validate_feature_status_label,
    validate_feature_dataset_label,
)


def test_feature_engine_labels():
    domains = list_feature_domain_labels()
    assert "price_indicator_domain" in domains
    assert "trend_indicator_domain" in domains
    assert "feature_input_contract_domain" in domains
    assert validate_feature_domain_label("price_indicator_domain") is True
    assert validate_feature_domain_label("invalid_domain") is False

    types = list_feature_type_labels()
    assert "feature_type_price" in types
    assert "feature_type_trend" in types
    assert validate_feature_type_label("feature_type_price") is True
    assert validate_feature_type_label("invalid_type") is False

    statuses = list_feature_status_labels()
    assert "feature_ready" in statuses
    assert validate_feature_status_label("feature_ready") is True
    assert validate_feature_status_label("invalid_status") is False

    datasets = list_feature_dataset_labels()
    assert "dataset_fx_ohlcv" in datasets
    assert "dataset_commodity_ohlcv" in datasets
    assert validate_feature_dataset_label("dataset_fx_ohlcv") is True
    assert validate_feature_dataset_label("invalid_dataset") is False
