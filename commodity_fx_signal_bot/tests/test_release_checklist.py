import pandas as pd
from quality_gates.quality_config import QualityGateProfile
from quality_gates.release_checklist import (
    build_release_candidate_checklist,
    evaluate_release_candidate_checklist,
    infer_release_candidate_status,
    summarize_release_checklist
)

def test_build_release_candidate_checklist():
    profile = QualityGateProfile(name="mock", description="mock")
    df = build_release_candidate_checklist(profile)
    assert isinstance(df, pd.DataFrame)

def test_evaluate_release_candidate_checklist():
    df = evaluate_release_candidate_checklist(pd.DataFrame(), {})
    assert isinstance(df, pd.DataFrame)

def test_infer_release_candidate_status():
    status = infer_release_candidate_status(pd.DataFrame(), {})
    assert isinstance(status, str)
    assert status != "production_ready"

def test_summarize_release_checklist():
    summary = summarize_release_checklist(pd.DataFrame())
    assert isinstance(summary, dict)
