import pytest
from report_summarization.summary_config import validate_report_summary_profiles, get_default_report_summary_profile, ConfigError

def test_validate_report_summary_profiles():
    # Should not raise any error on defaults
    validate_report_summary_profiles()

def test_get_default_report_summary_profile():
    profile = get_default_report_summary_profile()
    assert profile is not None
    assert profile.name == "balanced_local_summaries"
    assert profile.language == "tr"
    assert profile.max_reports > 0
    assert profile.max_chars_per_report > 0
    assert profile.use_local_only is True
    assert profile.allow_external_llm is False
    assert profile.allow_live_commands is False
    assert profile.allow_broker_commands is False
    assert profile.allow_deploy_commands is False
    assert profile.allow_background_daemons is False
    assert profile.allow_real_market_download is False
