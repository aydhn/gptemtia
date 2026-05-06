from risk.risk_filters import (
    should_block_for_risk,
    should_watchlist_for_risk,
    infer_risk_candidate_label,
    rank_risk_candidates,
)
from risk.risk_config import get_default_risk_precheck_profile
import pandas as pd


def test_should_block_for_risk():
    prof = get_default_risk_precheck_profile()
    evaluation = {"total_pretrade_risk_score": 0.9, "blocking_reasons": []}
    block, reasons = should_block_for_risk(evaluation, prof)
    assert block
    assert len(reasons) > 0


def test_infer_risk_candidate_label():
    prof = get_default_risk_precheck_profile()
    ev_reject = {"total_pretrade_risk_score": 0.9}
    label1 = infer_risk_candidate_label(ev_reject, prof)
    assert label1 == "risk_rejection_candidate"

    ev_approve = {"total_pretrade_risk_score": 0.2, "risk_readiness_score": 0.8}
    label2 = infer_risk_candidate_label(ev_approve, prof)
    assert label2 == "risk_approval_candidate"


def test_rank_risk_candidates():
    df = pd.DataFrame([{"risk_readiness_score": 0.5}, {"risk_readiness_score": 0.9}])
    ranked = rank_risk_candidates(df)
    assert ranked.iloc[0]["risk_readiness_score"] == 0.9
