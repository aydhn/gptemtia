from local_training.training_config import get_default_local_training_profile
from local_training.concept_map import build_concept_map_registry, build_concept_relationships

def test_concept_map():
    prof = get_default_local_training_profile()
    df, sum = build_concept_map_registry(prof)
    assert not df.empty
    assert not build_concept_relationships(prof).empty
