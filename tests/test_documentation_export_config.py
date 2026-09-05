"""Test config."""
import pytest
from commodity_fx_signal_bot.local_documentation_export.export_config import get_local_documentation_export_profile, validate_local_documentation_export_profiles, get_default_local_documentation_export_profile, ConfigError

def test_config():
    p = get_default_local_documentation_export_profile()
    assert p.name == "balanced_local_documentation_export"
    assert p.dry_run_default is True
    assert p.max_items > 0
    validate_local_documentation_export_profiles()
