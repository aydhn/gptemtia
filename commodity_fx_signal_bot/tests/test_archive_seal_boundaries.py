import pytest
from local_post_completion_preservation.preservation_config import get_default_local_post_completion_preservation_profile
from local_post_completion_preservation.archive_seal_boundaries import *

def test_boundaries():
    profile = get_default_local_post_completion_preservation_profile()
    df, s = build_archive_seal_boundary_registry(profile)
    assert len(df) > 0
    df2, s2 = build_non_seal_boundary_registry(profile)
    assert len(df2) > 0
