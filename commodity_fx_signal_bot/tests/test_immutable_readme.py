import pytest
import pandas as pd
from local_post_completion_preservation.preservation_config import get_default_local_post_completion_preservation_profile

def test_mock():
    profile = get_default_local_post_completion_preservation_profile()
    assert profile.dry_run_default == True
    assert profile.enabled == True
