from local_training.training_config import get_default_local_training_profile
from local_training.walkthrough_registry import build_guided_walkthrough_registry, build_default_walkthroughs

def test_walkthrough_registry():
    prof = get_default_local_training_profile()
    df, sum = build_guided_walkthrough_registry(prof)
    assert not df.empty
    assert not build_default_walkthroughs(prof).empty
