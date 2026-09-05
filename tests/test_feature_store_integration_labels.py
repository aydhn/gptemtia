from advanced_feature_store_integration.feature_store_integration_labels import (
    list_feature_store_integration_domain_labels,
    list_feature_store_status_labels,
    list_feature_store_entity_type_labels,
    validate_feature_store_integration_domain_label,
    validate_feature_store_status_label,
    validate_feature_store_entity_type_label,
)

def test_labels_lists_and_validation():
    domains = list_feature_store_integration_domain_labels()
    assert len(domains) >= 25
    assert "feature_store_contract_domain" in domains

    statuses = list_feature_store_status_labels()
    assert "store_ready" in statuses
    assert "store_manual_review_required" in statuses

    entities = list_feature_store_entity_type_labels()
    assert "entity_fx_pair" in entities
    assert "entity_commodity_symbol" in entities
    assert "entity_factor_family" in entities

    assert validate_feature_store_integration_domain_label("feature_store_contract_domain") == "feature_store_contract_domain"
    assert validate_feature_store_integration_domain_label("invalid") == "unknown_feature_store_integration_domain"

    assert validate_feature_store_status_label("store_ready") == "store_ready"
    assert validate_feature_store_status_label("bad") == "store_unknown"

    assert validate_feature_store_entity_type_label("entity_fx_pair") == "entity_fx_pair"
    assert validate_feature_store_entity_type_label("bad") == "entity_unknown"
