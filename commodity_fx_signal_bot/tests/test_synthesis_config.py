import pytest
from local_synthesis.synthesis_config import (
    get_local_synthesis_profile, list_local_synthesis_profiles,
    validate_local_synthesis_profiles, get_default_local_synthesis_profile, ConfigError
)

def test_validate_local_synthesis_profiles():
    validate_local_synthesis_profiles()

def test_get_default_local_synthesis_profile():
    p = get_default_local_synthesis_profile()
    assert p.name == "balanced_local_synthesis"
    assert p.language != ""
    assert p.max_index_items > 0
    assert p.max_sections > 0
    assert 0.0 <= p.min_quality_score <= 1.0
    assert p.dry_run_default is True
    assert p.allow_investment_advice is False
    assert p.allow_live_trading_claim is False
    assert p.allow_broker_readiness_claim is False
    assert p.allow_production_release_claim is False
    assert p.allow_model_deployment_claim is False
    assert p.allow_official_completion_claim is False
    assert p.allow_official_compliance_claim is False
    assert p.allow_cloud_upload is False
    assert p.allow_external_service is False
    assert p.allow_external_llm is False
    assert p.allow_file_modification is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_synthesis_profile("unknown_xyz")
