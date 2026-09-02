
import pytest
from commodity_fx_signal_bot.local_hardening.hardening_config import validate_local_hardening_profiles, get_default_local_hardening_profile, LocalHardeningProfile, ConfigError

def test_config():
    validate_local_hardening_profiles()
    prof = get_default_local_hardening_profile()
    assert prof.language
    assert prof.max_files > 0
    assert prof.max_functions > 0
    assert 0 <= prof.min_quality_score <= 1
    assert prof.dry_run_default is True
    assert not prof.allow_auto_refactor
    assert not prof.allow_dead_code_delete
