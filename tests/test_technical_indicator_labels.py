from advanced_technical_indicators.technical_indicator_labels import (
    list_technical_indicator_domain_labels,
    list_indicator_family_labels,
    list_indicator_status_labels,
    validate_technical_indicator_domain_label,
    validate_indicator_family_label,
    validate_indicator_status_label,
)


def test_technical_indicator_labels():
    domains = list_technical_indicator_domain_labels()
    families = list_indicator_family_labels()
    statuses = list_indicator_status_labels()

    assert len(domains) >= 20
    assert len(families) >= 12
    assert len(statuses) >= 5

    assert validate_technical_indicator_domain_label("technical_indicator_profile_domain")
    assert validate_indicator_family_label("family_price_action")
    assert validate_indicator_status_label("indicator_ready")

    assert not validate_technical_indicator_domain_label("invalid_domain_xyz")
    assert not validate_indicator_family_label("invalid_family_xyz")
    assert not validate_indicator_status_label("invalid_status_xyz")
