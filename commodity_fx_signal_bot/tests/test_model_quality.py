import pytest
import pandas as pd
from ml.model_quality import check_model_metric_sanity, check_for_forbidden_live_terms_in_model_metadata

def test_check_model_metric_sanity():
    res = check_model_metric_sanity({"balanced_accuracy": 0.4}, "classification")
    assert not res["passed"] or len(res["warnings"]) > 0

    res = check_model_metric_sanity({"r2": -0.1}, "regression")
    assert not res["passed"] or len(res["warnings"]) > 0

def test_check_for_forbidden_live_terms_in_model_metadata():
    metadata = {"status": "DEPLOYED_LIVE_MODEL"}
    res = check_for_forbidden_live_terms_in_model_metadata(metadata)
    assert not res["passed"]

    metadata = {"status": "trained_candidate"}
    res = check_for_forbidden_live_terms_in_model_metadata(metadata)
    assert res["passed"]
