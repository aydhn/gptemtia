import pandas as pd
from research_planning.research_debt import calculate_research_debt_score, classify_research_debt_level, build_research_debt_table

def test_calculate_score():
    df = pd.DataFrame([
        {"task_type": "governance_task", "priority_label": "critical_research_priority"}
    ])
    score = calculate_research_debt_score(df)
    assert score > 0
    assert score <= 1.0

def test_classify():
    assert classify_research_debt_level(0.8) == "critical_research_debt"
    assert classify_research_debt_level(0.6) == "high_research_debt"
    assert classify_research_debt_level(0.3) == "moderate_research_debt"
    assert classify_research_debt_level(0.1) == "low_research_debt"

def test_build_table():
    df = pd.DataFrame([
        {"task_id": "1", "task_type": "governance_task", "title": "t", "priority_score": 0.9, "priority_label": "critical_research_priority"},
        {"task_id": "2", "task_type": "meta_research_task", "title": "t", "priority_score": 0.5, "priority_label": "medium"}
    ])
    debt_df = build_research_debt_table(df)
    assert len(debt_df) == 1
    assert debt_df.iloc[0]["task_id"] == "1"
