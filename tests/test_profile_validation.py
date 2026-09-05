from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_validation import validate_no_forbidden_profile_claims

def test_validation():
    res = validate_no_forbidden_profile_claims("kesin al")
    assert res["status"] == "failed"
    
    res = validate_no_forbidden_profile_claims("yatırım tavsiyesi değildir")
    assert res["status"] == "passed"
