import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.productivity_checklist import (
    build_productivity_checklist, evaluate_productivity_checklist, summarize_productivity_checklist
)
import pandas as pd

def test_productivity_checklist():
    profile = get_default_analyst_ux_profile()
    df = build_productivity_checklist(profile)
    assert not df.empty

    evaluated = evaluate_productivity_checklist(df, pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]))
    assert not evaluated.empty

    summary = summarize_productivity_checklist(evaluated)
    assert summary["total_items"] > 0
    assert summary["passed_items"] > 0
    assert "passed" in summary
