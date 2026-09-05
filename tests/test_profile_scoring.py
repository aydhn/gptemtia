from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_scoring import calculate_profile_readiness_score

def test_scoring():
    import pandas as pd
    p = get_default_advanced_config_system_profile()
    score = calculate_profile_readiness_score(pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([{"status": "passed"}]), p)
    assert 0 <= score <= 1.0
