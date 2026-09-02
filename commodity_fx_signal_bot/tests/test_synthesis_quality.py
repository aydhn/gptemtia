import pytest
import pandas as pd
from local_synthesis.synthesis_quality import check_phase_family_quality, build_final_synthesis_quality_report
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_synthesis_quality():
    prof = get_default_local_synthesis_profile()
    res = check_phase_family_quality(pd.DataFrame(), prof)
    assert res["valid"]
    report = build_final_synthesis_quality_report({})
    assert report["passed"]
