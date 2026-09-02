import pytest
from local_training.training_config import validate_local_training_profiles, get_default_local_training_profile, get_local_training_profile, ConfigError

def test_validate_local_training_profiles():
    validate_local_training_profiles()

def test_get_default_local_training_profile():
    p = get_default_local_training_profile()
    assert p.language == "tr"
    assert p.max_lessons > 0
    assert p.max_walkthrough_steps > 0
    assert 0 <= p.min_training_quality_score <= 1
    assert p.dry_run_default is True
    assert p.allow_cloud_upload is False
    assert p.allow_external_training_service is False
    assert p.allow_external_llm is False
    assert p.allow_file_modification is False
    assert p.allow_file_deletion is False
    assert p.allow_file_move is False
    assert p.allow_overwrite is False
    assert p.allow_live_commands is False
    assert p.allow_broker_commands is False
    assert p.allow_deploy_commands is False
    assert p.allow_background_daemons is False
    assert p.allow_real_market_download is False
    assert p.allow_certification_claim is False
    assert p.allow_investment_advice_training is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_training_profile("unknown_profile")
