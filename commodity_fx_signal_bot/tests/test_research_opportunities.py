import pandas as pd
from research_planning.research_opportunities import calculate_research_opportunity_score, classify_research_opportunity, identify_research_opportunities
from research_planning.planning_models import ResearchSignal

def test_calculate_score():
    sig = ResearchSignal("s", "gov", "audit", None, None, 0.5, 0.9, 0.1, 0.5, "t", "d", {}, [])
    score = calculate_research_opportunity_score(sig)
    assert score > 0.7

def test_classify():
    assert classify_research_opportunity(0.9) == "high_opportunity"
    assert classify_research_opportunity(0.7) == "medium_opportunity"
    assert classify_research_opportunity(0.3) == "low_opportunity"

def test_identify():
    sig1 = ResearchSignal("s1", "gov", "audit", None, None, 0.5, 0.9, 0.1, 0.5, "t", "d", {}, [])
    sig2 = ResearchSignal("s2", "gov", "audit", None, None, 0.5, 0.1, 0.9, 0.5, "t", "d", {}, [])

    df = identify_research_opportunities([sig1, sig2], pd.DataFrame())
    assert len(df) == 1
    assert df.iloc[0]["signal_id"] == "s1"
