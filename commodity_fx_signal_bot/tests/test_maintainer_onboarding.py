from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.maintainer_onboarding import build_maintainer_onboarding_simplification_guide

def test_build_onboarding():
    p = get_default_local_simplification_profile()
    text, summary = build_maintainer_onboarding_simplification_guide(Path("."), p)
    assert len(text) > 0
