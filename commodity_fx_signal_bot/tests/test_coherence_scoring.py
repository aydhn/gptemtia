import pytest
import pandas as pd
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.coherence_scoring import build_cross_layer_coherence_score_report, calculate_cross_layer_coherence_score

def test_calculate_cross_layer_coherence_score():
    profile = get_default_local_consistency_profile()
    score = calculate_cross_layer_coherence_score(pd.DataFrame(), pd.DataFrame(), profile)
    assert 0.0 <= score <= 1.0

def test_build_cross_layer_coherence_score_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_cross_layer_coherence_score_report(pd.DataFrame(), pd.DataFrame(), profile)
    assert df is not None
