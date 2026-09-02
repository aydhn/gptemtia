from local_dr.dr_config import get_local_dr_profile, list_local_dr_profiles, validate_local_dr_profiles, get_default_local_dr_profile

def test_dr_config():
    profile = get_local_dr_profile("balanced_local_dr")
    assert profile.name == "balanced_local_dr"
    
    profiles = list_local_dr_profiles()
    assert len(profiles) == 4
    
    validate_local_dr_profiles()
    
    default = get_default_local_dr_profile()
    assert default.name == "balanced_local_dr"
