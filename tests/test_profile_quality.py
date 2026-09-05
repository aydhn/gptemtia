from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_quality import check_for_forbidden_terms_in_profiles

def test_quality():
    res = check_for_forbidden_terms_in_profiles("live trading approved")
    assert len(res["forbidden_terms_found"]) > 0
    
    res = check_for_forbidden_terms_in_profiles("yatırım tavsiyesi değildir")
    assert len(res["forbidden_terms_found"]) == 0
