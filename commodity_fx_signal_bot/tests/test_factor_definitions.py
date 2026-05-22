from factor_research.factor_config import get_default_factor_research_profile
from factor_research.factor_definitions import build_default_factor_definitions, factor_definitions_to_dataframe

def test_factor_definitions():
    prof = get_default_factor_research_profile()
    defs = build_default_factor_definitions(prof)
    assert len(defs) > 0
    df = factor_definitions_to_dataframe(defs)
    assert not df.empty
    assert "factor_id" in df.columns
