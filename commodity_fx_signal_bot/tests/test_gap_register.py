import pytest
import pandas as pd
from final_review.gap_register import build_gaps_from_audit_results, gaps_to_dataframe, summarize_final_gaps

def test_gap_register_functions():
    gaps = build_gaps_from_audit_results({}, {"documentation": {"missing_docs": ["README.md"]}})
    assert len(gaps) == 1

    df = gaps_to_dataframe(gaps)
    assert not df.empty

    summary = summarize_final_gaps(df)
    assert summary["total_gaps"] == 1
