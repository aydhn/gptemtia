
import pandas as pd
from local_closure.closure_dossier import build_v1_local_closure_dossier
from local_closure.closure_config import get_default_local_closure_profile

def test_dossier():
    p = get_default_local_closure_profile()
    lessons = pd.DataFrame([{"lesson_id": "1"}])
    roadmap = pd.DataFrame([{"roadmap_id": "1"}])
    text, summary = build_v1_local_closure_dossier("meta", lessons, roadmap, {}, p)
    assert "V1.0 Local Closure Dossier" in text
    assert "UYARI" in text
