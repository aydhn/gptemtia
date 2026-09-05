import pytest
from advanced_continuation.continuation_config import get_advanced_continuation_profile

def test_continuation_models_basic():
    profile = get_advanced_continuation_profile("balanced_advanced_continuation")
    assert profile.target_final_phase == 160
    assert profile.current_phase == 101
