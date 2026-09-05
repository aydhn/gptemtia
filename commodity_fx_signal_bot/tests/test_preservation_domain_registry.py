import pytest
from local_post_completion_preservation.preservation_config import get_default_local_post_completion_preservation_profile
from local_post_completion_preservation.preservation_domain_registry import *

def test_registry():
    profile = get_default_local_post_completion_preservation_profile()
    df, summary = build_preservation_domain_registry(profile)
    assert len(df) > 0
