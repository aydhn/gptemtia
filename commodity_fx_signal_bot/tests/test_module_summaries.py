import pandas as pd
from report_summarization.module_summaries import build_module_summary, build_all_module_summaries, rank_modules_by_attention_need

def test_build_module_summary():
    sums = pd.DataFrame([{"module_name": "mod1", "source_path": "path1"}])
    finds = pd.DataFrame([{"module_name": "mod1", "text": "f1", "priority": "high_priority"}])
    warns = pd.DataFrame([{"module_name": "mod1", "text": "w1", "priority": "critical_priority"}])

    card = build_module_summary("mod1", sums, finds, warns)
    assert card.module_name == "mod1"
    assert card.priority == "critical_priority"

def test_rank_modules_by_attention_need():
    finds = pd.DataFrame([{"module_name": "mod1"}, {"module_name": "mod1"}, {"module_name": "mod2"}])
    warns = pd.DataFrame([{"module_name": "mod1", "priority": "critical_priority"}])

    rank = rank_modules_by_attention_need(finds, warns)
    assert not rank.empty
    assert rank.iloc[0]["module_name"] == "mod1"
