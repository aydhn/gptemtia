import pytest
from command_center.onboarding import (
    build_analyst_onboarding_sections,
    build_new_user_safe_start_guide,
    build_codex_agent_onboarding_guide,
    build_onboarding_checklist,
    summarize_onboarding
)
from command_center.command_config import get_default_command_center_profile

def test_build_analyst_onboarding_sections():
    profile = get_default_command_center_profile()
    sections = build_analyst_onboarding_sections(profile)
    assert len(sections) > 0
    assert "Safety Limits" in [s["title"] for s in sections]

def test_build_guides():
    guide1 = build_new_user_safe_start_guide([], [], [])
    assert "Safe Start Guide" in guide1

    guide2 = build_codex_agent_onboarding_guide([], [])
    assert "Codex Agent Guide" in guide2
    assert "live deployments" in guide2

def test_build_onboarding_checklist():
    profile = get_default_command_center_profile()
    df = build_onboarding_checklist(profile)
    assert not df.empty

    summary = summarize_onboarding(df)
    assert summary["pending_steps"] > 0

def test_onboarding_no_trading():
    profile = get_default_command_center_profile()
    sections = build_analyst_onboarding_sections(profile)
    for s in sections:
        assert "investment advice" not in s["content"] or "NOT" in s["content"]
