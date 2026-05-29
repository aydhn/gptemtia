import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.query_mapping import build_query_mapping_report

def test_query_mapping():
    profile = get_default_analyst_ux_profile()

    tables, summary = build_query_mapping_report("scenario regression hatası", profile)

    assert not tables["runbooks"].empty
    assert not tables["workflows"].empty
    assert not tables["docs"].empty

def test_investment_advice_fallback():
    profile = get_default_analyst_ux_profile()
    tables, summary = build_query_mapping_report("kesin al", profile)

    assert "SAFE_USAGE_GUIDE.md" in tables["docs"]["doc"].values
