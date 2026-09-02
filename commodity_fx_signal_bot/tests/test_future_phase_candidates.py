
import pandas as pd
from local_closure.future_phase_candidates import build_future_phase_candidate_registry
from local_closure.closure_config import get_default_local_closure_profile

def test_candidates():
    p = get_default_local_closure_profile()
    roadmap_df = pd.DataFrame([{"title": "Test", "status": "roadmap_candidate", "rationale": "R"}])
    df, summary = build_future_phase_candidate_registry(roadmap_df, p)
    assert not df.empty
    assert summary["total_candidates"] == 1


def test_dummy(): pass
