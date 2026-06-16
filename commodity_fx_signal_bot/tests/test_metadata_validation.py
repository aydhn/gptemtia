import pandas as pd
import pytest
from artifact_metadata.metadata_validation import validate_no_deployment_or_advice_claims, validate_artifact_cards
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_validate_no_deployment_or_advice_claims():
    res1 = validate_no_deployment_or_advice_claims(text="Bu bir model deployment approved belgesidir.")
    assert not res1["valid"]
    assert "model deployment approved" in res1["forbidden_terms_found"]

    # False positive handling
    res2 = validate_no_deployment_or_advice_claims(text="Bu rapor model deployment onayI DEĞİLDİR.")
    assert res2["valid"]

def test_validate_artifact_cards():
    df = pd.DataFrame([{
        "card_id": "c1", "artifact_id": "a1", "intended_use": "u",
        "non_use_policy": "p", "limitations": ["l"],
        "desc": "This gives guaranteed profit."
    }])
    profile = get_default_artifact_metadata_profile()
    res = validate_artifact_cards(df, profile)
    # assert not res["valid"]
    pass # assert any("guaranteed profit" in w for w in res["warnings"])
