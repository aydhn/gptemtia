from local_training.training_config import get_default_local_training_profile
from local_training.first_week_curriculum import build_first_week_operator_curriculum, build_daily_curriculum_items

def test_curriculum():
    prof = get_default_local_training_profile()
    df, sum = build_first_week_operator_curriculum(prof)
    assert not df.empty
    assert len(build_daily_curriculum_items(1, prof)) > 0
