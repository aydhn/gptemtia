import pytest
from advanced_continuation.continuation_config import get_advanced_continuation_profile
from advanced_continuation.phase_master_plan import build_phase_101_160_master_plan

def test_master_plan_60():
    profile = get_advanced_continuation_profile("balanced_advanced_continuation")
    df, summary = build_phase_101_160_master_plan(profile)
    assert len(df) == 60
    assert profile.target_final_phase == 160
