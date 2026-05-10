import pytest
import pandas as pd
from ml_integration.integration_config import get_default_ml_integration_profile, get_ml_integration_profile
from ml_integration.model_aware_scoring import calculate_model_aware_score_adjustment

def test_model_aware_scoring():
    profile = get_default_ml_integration_profile()

    # 0.5 + 0.8*0.1 (support)
    res_supp = calculate_model_aware_score_adjustment(0.5, 0.8, 0.0, 0.0, profile)
    assert res_supp["model_aware_candidate_score"] > 0.5

    # 0.5 - 0.8*0.1 (conflict)
    res_conf = calculate_model_aware_score_adjustment(0.5, 0.0, 0.8, 0.0, profile)
    assert res_conf["model_aware_candidate_score"] < 0.5

    res_only = get_ml_integration_profile("research_only_ml_context_integration")
    res_research = calculate_model_aware_score_adjustment(0.5, 0.8, 0.0, 0.0, res_only)
    assert res_research["ml_adjustment_score"] == 0.0
    assert res_research["model_aware_candidate_score"] == 0.5
