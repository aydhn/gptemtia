from local_training.training_config import get_default_local_training_profile
from local_training.training_validation import build_training_validation_report

def test_validation():
    prof = get_default_local_training_profile()
    df, sum = build_training_validation_report({"test": True}, prof)
    assert not df.empty
