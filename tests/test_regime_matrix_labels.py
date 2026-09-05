from advanced_regime_matrix.regime_matrix_labels import (
    REGIME_MATRIX_DOMAIN_LABELS,
    REGIME_MATRIX_STATUS_LABELS,
    REGIME_MATRIX_ENTITY_LABELS,
    list_regime_matrix_domain_labels,
    list_regime_matrix_status_labels,
    list_regime_matrix_entity_labels,
    validate_regime_matrix_domain_label,
    validate_regime_matrix_status_label,
    validate_regime_matrix_entity_label,
)


def test_regime_matrix_labels_lists():
    domains = list_regime_matrix_domain_labels()
    assert len(domains) >= 20
    assert "regime_matrix_domain" in domains
    assert "regime_feature_matrix_contract_domain" in domains

    statuses = list_regime_matrix_status_labels()
    assert "matrix_ready" in statuses
    assert "matrix_placeholder_only" in statuses

    entities = list_regime_matrix_entity_labels()
    assert "matrix_entity_fx_pair" in entities
    assert "matrix_entity_commodity_symbol" in entities


def test_regime_matrix_label_validators():
    assert validate_regime_matrix_domain_label("regime_matrix_domain") is True
    assert validate_regime_matrix_domain_label("invalid_domain") is False

    assert validate_regime_matrix_status_label("matrix_ready") is True
    assert validate_regime_matrix_status_label("invalid_status") is False

    assert validate_regime_matrix_entity_label("matrix_entity_fx_pair") is True
    assert validate_regime_matrix_entity_label("invalid_entity") is False
