from local_training.training_config import get_default_local_training_profile
from local_training.glossary import build_glossary_registry, build_default_glossary_terms

def test_glossary():
    prof = get_default_local_training_profile()
    df, sum = build_glossary_registry(prof)
    assert not df.empty
    assert not build_default_glossary_terms(prof).empty
