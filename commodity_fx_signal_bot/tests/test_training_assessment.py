from local_training.training_config import get_default_local_training_profile
from local_training.training_assessment import build_training_assessment_dry_run

def test_assessment():
    prof = get_default_local_training_profile()
    df, sum = build_training_assessment_dry_run(prof)
    assert not df.empty
