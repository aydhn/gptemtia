import pytest
import pandas as pd
from experiments.experiment_quality import (
    check_for_forbidden_trade_terms_in_experiments,
    check_hypothesis_registry_quality,
    check_experiment_definition_quality,
    check_run_manifest_quality,
    check_artifact_manifest_quality,
    check_reproducibility_manifest_quality,
    build_experiment_quality_report
)
from experiments.experiment_config import get_default_experiment_profile

def test_check_for_forbidden_trade_terms():
    res = check_for_forbidden_trade_terms_in_experiments(text="This is a BUY signal")
    assert res["valid"] is False
    assert "BUY" in res["found_terms"]

    res2 = check_for_forbidden_trade_terms_in_experiments(text="This is candidate_better")
    assert res2["valid"] is True

def test_check_hypothesis_registry_quality():
    df = pd.DataFrame([{"hypothesis_status": "hypothesis_supported"}])
    res = check_hypothesis_registry_quality(df)
    assert res["valid"] is True

def test_check_experiment_definition_quality():
    profile = get_default_experiment_profile()
    res = check_experiment_definition_quality({"experiment_type": "candidate_experiment"}, profile)
    assert res["valid"] is True

def test_check_run_manifest_quality():
    res = check_run_manifest_quality({"status": "completed"})
    assert res["valid"] is True

def test_check_artifact_manifest_quality():
    res = check_artifact_manifest_quality({"missing_required": []})
    assert res["valid"] is True

def test_build_experiment_quality_report():
    report = build_experiment_quality_report(
        summary={"notes": "All good"},
        manifest={"missing_required": []},
        comparison_df=pd.DataFrame([{"comparison_label": "candidate_better"}]),
        leaderboard_df=pd.DataFrame([{"rank": 1}])
    )
    assert report["passed"] is True
    assert report["forbidden_trade_terms_found"] is False
