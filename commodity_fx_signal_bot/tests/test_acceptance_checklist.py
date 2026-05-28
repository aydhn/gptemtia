import pytest
import pandas as pd
from final_review.acceptance_checklist import (
    build_final_acceptance_checklist, evaluate_final_acceptance_checklist,
    calculate_acceptance_score, calculate_safety_score, infer_final_readiness_label, summarize_acceptance_checklist
)
from final_review.final_review_config import get_default_final_review_profile

def test_acceptance_checklist_functions():
    profile = get_default_final_review_profile()
    df = build_final_acceptance_checklist(profile)
    assert not df.empty

    eval_df = evaluate_final_acceptance_checklist(df, {}, {"blocking_risks": 0}, {})
    assert not eval_df.empty

    score = calculate_acceptance_score(eval_df, {})
    assert score > 0.0

    safety = calculate_safety_score(pd.DataFrame(), pd.DataFrame())
    assert safety == 1.0

    label = infer_final_readiness_label(0.9, 1.0, 0, profile)
    assert label == "offline_ready_for_research_use"
