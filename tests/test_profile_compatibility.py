from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_compatibility import evaluate_profile_compatibility

def test_compatibility():
    item = evaluate_profile_compatibility("no_scraping", "any")
    assert item.compatibility_status == "profile_ready"
    
    item = evaluate_profile_compatibility("intraday_research_no_live", "live_trading")
    assert item.compatibility_status == "profile_incompatible"
