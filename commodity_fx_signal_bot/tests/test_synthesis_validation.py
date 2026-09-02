import pytest
import pandas as pd
from local_synthesis.synthesis_validation import validate_phase_family_registry
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_validate_phase_family_registry():
    prof = get_default_local_synthesis_profile()
    res = validate_phase_family_registry(pd.DataFrame(), prof)
    assert res["valid"]
