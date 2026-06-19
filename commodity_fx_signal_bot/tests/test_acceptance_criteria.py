from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.acceptance_criteria import build_milestone_acceptance_criteria, map_acceptance_criteria_to_evidence
from config.paths import PROJECT_ROOT

def test_acceptance_criteria():
    profile = get_default_local_readiness_profile()
    df, summary = build_milestone_acceptance_criteria(profile)
    assert not df.empty

    map_df, map_summ = map_acceptance_criteria_to_evidence(df, PROJECT_ROOT)
    assert not map_df.empty
