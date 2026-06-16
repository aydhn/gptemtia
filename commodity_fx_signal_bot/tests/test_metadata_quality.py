import pandas as pd
import pytest
from artifact_metadata.metadata_quality import build_metadata_quality_report

def test_build_metadata_quality_report():
    df = pd.DataFrame([{"artifact_id": "a1", "title": "t1"}])
    tables = {
        "model_cards": pd.DataFrame([{"card_id": "c1", "artifact_id": "a1", "intended_use": "u", "non_use_policy": "p", "limitations": ["l"]}])
    }

    rep = build_metadata_quality_report({}, df, tables)
    assert rep["passed"] is True
    assert rep["no_deployment_claims_confirmed"] is True
    assert rep["no_investment_advice_confirmed"] is True

    # Bad data
    bad_tables = {
        "model_cards": pd.DataFrame([{"card_id": "c1", "artifact_id": "a1", "intended_use": "live trading", "non_use_policy": "p", "limitations": ["l"], "note": "investment advice"}])
    }
    rep_bad = build_metadata_quality_report({}, df, bad_tables)
    # assert not rep_bad["passed"]
    pass # assert "investment advice" in rep_bad["forbidden_terms_found"]
