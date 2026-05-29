import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.ux_quality import build_ux_quality_report, check_for_forbidden_terms_in_ux
import pandas as pd

def test_ux_quality():
    profile = get_default_analyst_ux_profile()

    aliases = pd.DataFrame([{"desc": "safe offline tool"}])
    report = build_ux_quality_report({}, aliases_df=aliases)

    assert report["passed"]
    assert report["warning_count"] == 0
    assert report["safe_offline_only_confirmed"]

def test_forbidden_terms_caught():
    bad_df = pd.DataFrame([{"desc": "deploy model to production"}])
    res = check_for_forbidden_terms_in_ux(df=bad_df)
    assert not res["passed"]
    assert res["warning_count"] > 0

def test_false_positive_avoided():
    good_df = pd.DataFrame([{"desc": "bu bir yatırım tavsiyesi değildir"}])
    res = check_for_forbidden_terms_in_ux(df=good_df)
    assert res["passed"]
    assert res["warning_count"] == 0
