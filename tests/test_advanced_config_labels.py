from advanced_config_profiles.advanced_config_labels import list_profile_domain_labels

def test_labels():
    labels = list_profile_domain_labels()
    assert "config_profile_domain" in labels
