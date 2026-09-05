from advanced_config_profiles.advanced_config_models import ConfigProfileItem

def test_model():
    c = ConfigProfileItem("id", "domain", "name", "desc", {}, "ready", [], False)
    assert c.profile_id == "id"
