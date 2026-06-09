import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_digest import (
    build_evidence_digest,
    build_safe_evidence_follow_ups
)

def test_evidence_digest():
    profile = get_default_evidence_governance_profile()

    gap_df = pd.DataFrame([{"gap_id": "g1", "severity": "high", "recommended_safe_follow_up": "do something"}])
    scoring_summary = {"completeness_score": 0.8, "freshness_score": 0.9}

    text, summary = build_evidence_digest(pd.DataFrame(), pd.DataFrame(), gap_df, scoring_summary, profile)

    assert "Completeness Score:** 0.80" in text
    assert "Freshness Score:** 0.90" in text
    assert "do something" in text
    assert "yatırım tavsiyesi değildir" in text

    fu = build_safe_evidence_follow_ups(gap_df)
    assert not fu.empty
