import pandas as pd
from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.handover_binder import build_handover_education_binder, build_handover_binder_sections

def test_handover():
    prof = get_default_local_training_profile()
    txt, sum = build_handover_education_binder(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(txt, str)
    assert "official certification değildir" in txt.lower() or "certification" in txt.lower()
