
import pytest
from local_review_governance.review_config import get_default_local_review_governance_profile, validate_local_review_governance_profiles, get_local_review_governance_profile, ConfigError

def test_config():
    validate_local_review_governance_profiles()
    p = get_default_local_review_governance_profile()
    assert p.language == "tr"
    assert p.max_items > 0
    with pytest.raises(ConfigError):
        get_local_review_governance_profile("non_existent")
