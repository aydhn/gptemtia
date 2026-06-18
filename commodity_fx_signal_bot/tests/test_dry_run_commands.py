from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.dry_run_commands import build_dry_run_command_checklist

def test_dry_run_commands():
    profile = get_default_local_readiness_profile()
    df, s = build_dry_run_command_checklist(profile)
    assert not df.empty
    assert "is_safe" in df.columns
