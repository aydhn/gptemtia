import pytest
from knowledge_base.kb_config import get_knowledge_base_profile, validate_knowledge_base_profiles, ConfigError, get_default_knowledge_base_profile

def test_validate_profiles():
    validate_knowledge_base_profiles()

def test_get_default_profile():
    p = get_default_knowledge_base_profile()
    assert p.max_documents > 0

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_knowledge_base_profile("non_existent")
