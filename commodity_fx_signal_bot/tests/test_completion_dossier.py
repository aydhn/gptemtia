import pytest
import pandas as pd
from local_synthesis.completion_dossier import build_project_completion_dossier
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_project_completion_dossier():
    prof = get_default_local_synthesis_profile()
    text, summary = build_project_completion_dossier(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(text, str)
    assert "production release" not in text.lower() or "no production release" in text.lower()
