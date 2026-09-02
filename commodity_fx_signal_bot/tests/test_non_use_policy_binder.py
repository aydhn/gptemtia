import pytest
from local_synthesis.non_use_policy_binder import build_final_non_use_policy_binder
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_non_use_policy_binder():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_non_use_policy_binder(prof)
    assert isinstance(text, str)
