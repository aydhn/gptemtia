import pytest
import pandas as pd
from paper.paper_quality import check_for_forbidden_live_terms_in_paper, build_paper_quality_report, check_virtual_orders_dataframe

def test_check_forbidden_terms():
    df = pd.DataFrame({'notes': ["Generated via paper adapter.", "LIVE_ORDER sent"]})
    res = check_for_forbidden_live_terms_in_paper(df)
    assert not res["passed"]
    assert "LIVE_ORDER" in res["forbidden_live_terms_found"]

def test_check_dataframes():
    df = pd.DataFrame([{"order_id": "o1", "symbol": "GC", "order_status": "virtual_pending"}])
    res = check_virtual_orders_dataframe(df)
    assert res["passed"]

def test_build_report():
    orders = pd.DataFrame([{"order_id": "o1", "symbol": "GC", "order_status": "virtual_pending"}])
    positions = pd.DataFrame()
    ledger = pd.DataFrame()

    report = build_paper_quality_report({}, orders, positions, ledger)
    assert report["passed"]
    assert report["order_rows"] == 1
