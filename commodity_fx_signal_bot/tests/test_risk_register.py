import pytest
import pandas as pd
from final_review.risk_register import build_risks_from_audit_results, risks_to_dataframe, summarize_final_risks
from final_review.final_review_models import FinalRisk

def test_risk_register_functions():
    safety_df = pd.DataFrame([{"file": "test.py", "pattern_found": "live order", "critical": True}])
    risks = build_risks_from_audit_results({"safety": safety_df})
    assert len(risks) == 1
    assert risks[0].severity == "critical_risk"

    df = risks_to_dataframe(risks)
    assert not df.empty

    summary = summarize_final_risks(df)
    assert summary["blocking_risks"] == 1
