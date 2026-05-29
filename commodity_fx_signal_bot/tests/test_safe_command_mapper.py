import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.command_aliases import build_default_command_aliases, command_aliases_to_dataframe
from analyst_ux.intent_classifier import classify_analyst_intent
from analyst_ux.safe_command_mapper import (
    build_safe_command_suggestions, rank_command_suggestions, validate_suggestion_safety
)

def test_safe_command_suggestions():
    profile = get_default_analyst_ux_profile()
    aliases = command_aliases_to_dataframe(build_default_command_aliases(profile))

    df, summary = build_safe_command_suggestions("final review raporu üret", aliases, profile)
    assert not df.empty
    assert summary["count"] > 0

    df = rank_command_suggestions(df)
    assert df["rank"].iloc[0] == 1

    val = validate_suggestion_safety(df, profile)
    assert val["passed"]

def test_blocked_command_suggestion():
    profile = get_default_analyst_ux_profile()
    aliases = command_aliases_to_dataframe(build_default_command_aliases(profile))

    df, summary = build_safe_command_suggestions("live broker order send", aliases, profile)
    val = validate_suggestion_safety(df, profile)
    assert val["passed"] # Blocked commands are filtered out, so the resulting df should have 0 blocked
    assert summary["count"] == 0 # no safe suggestions
