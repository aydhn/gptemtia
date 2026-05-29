import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.command_aliases import (
    build_default_command_aliases, command_aliases_to_dataframe, validate_command_aliases
)

def test_default_aliases():
    profile = get_default_analyst_ux_profile()
    aliases = build_default_command_aliases(profile)
    assert len(aliases) > 0
    df = command_aliases_to_dataframe(aliases)
    assert not df.empty
    assert "command" in df.columns

    res = validate_command_aliases(aliases)
    assert res["passed"]
    assert res["blocked_count"] == 0

def test_alias_blocks_live():
    profile = get_default_analyst_ux_profile()
    aliases = build_default_command_aliases(profile)
    from analyst_ux.ux_models import CommandAlias
    aliases.append(CommandAlias("test", "test", "type", "run live", "desc", "mod", "safe", [], []))
    res = validate_command_aliases(aliases)
    assert not res["passed"]
    assert res["blocked_count"] > 0
