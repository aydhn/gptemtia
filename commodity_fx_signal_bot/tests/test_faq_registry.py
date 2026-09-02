from local_training.training_config import get_default_local_training_profile
from local_training.faq_registry import build_faq_registry, build_default_faq_items

def test_faq():
    prof = get_default_local_training_profile()
    df, sum = build_faq_registry(prof)
    assert not df.empty
    assert len(build_default_faq_items(prof)) > 0
