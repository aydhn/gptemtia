from pathlib import Path
from local_acceptance.acceptance_simulation import build_final_acceptance_simulation_checklist
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_acceptance_simulation_checklist():
    p = get_default_local_acceptance_profile()
    df, s = build_final_acceptance_simulation_checklist(Path("."), p)
    assert not df.empty
    assert s["total_items"] > 0
