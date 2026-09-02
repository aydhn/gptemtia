from local_acceptance.verification_scenarios import build_final_verification_scenario_registry
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_verification_scenario_registry():
    p = get_default_local_acceptance_profile()
    df, s = build_final_verification_scenario_registry(p)
    assert not df.empty
