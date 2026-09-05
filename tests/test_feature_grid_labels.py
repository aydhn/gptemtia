from advanced_feature_grid.feature_grid_labels import (
    list_feature_grid_domain_labels,
    list_feature_grid_family_labels,
    list_feature_grid_status_labels,
    validate_feature_grid_domain_label,
    validate_feature_grid_family_label,
    validate_feature_grid_status_label,
)


def test_feature_grid_labels():
    domains = list_feature_grid_domain_labels()
    assert len(domains) >= 20
    assert "window_grid_contract_domain" in domains
    assert "no_lookahead_guard_domain" in domains
    assert "duplicate_detection_domain" in domains

    families = list_feature_grid_family_labels()
    assert "grid_family_moving_average" in families
    assert "grid_family_momentum" in families
    assert "grid_family_volatility" in families
    assert "grid_family_range_channel" in families
    assert "grid_family_mean_reversion" in families
    assert "grid_family_return" in families

    statuses = list_feature_grid_status_labels()
    assert "feature_grid_ready" in statuses
    assert "feature_grid_blocked_by_safety" in statuses

    assert validate_feature_grid_domain_label("window_grid_contract_domain") == "window_grid_contract_domain"
    assert validate_feature_grid_domain_label("invalid_dom") == "unknown_feature_grid_domain"

    assert validate_feature_grid_family_label("grid_family_momentum") == "grid_family_momentum"
    assert validate_feature_grid_family_label("invalid_fam") == "grid_family_unknown"

    assert validate_feature_grid_status_label("feature_grid_ready") == "feature_grid_ready"
    assert validate_feature_grid_status_label("invalid_stat") == "feature_grid_unknown"
