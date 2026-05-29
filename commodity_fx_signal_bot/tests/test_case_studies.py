import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.case_studies import build_default_case_studies, case_studies_to_dataframe

def test_case_studies():
    profile = get_default_scenario_profile()
    cs = build_default_case_studies(profile)
    assert len(cs) > 0

    df = case_studies_to_dataframe(cs)
    assert not df.empty
    assert "objective" in df.columns
    assert "warnings" in df.columns
    assert "offline" in df.iloc[0]["warnings"][0].lower()
