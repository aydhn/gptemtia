import pandas as pd
from report_summarization.follow_up_tasks import build_follow_up_tasks_from_findings, follow_up_tasks_to_dataframe
from report_summarization.summary_config import get_default_report_summary_profile

def test_build_follow_up_tasks():
    profile = get_default_report_summary_profile()
    finds = pd.DataFrame([
        {"finding_type": "quality_finding", "module_name": "mod1", "text": "bad quality"},
        {"finding_type": "documentation_finding", "module_name": "mod1", "text": "bad doc"}
    ])
    warns = pd.DataFrame()
    rg = pd.DataFrame()

    tasks = build_follow_up_tasks_from_findings(finds, warns, rg, profile)
    assert len(tasks) == 2

    df = follow_up_tasks_to_dataframe(tasks)
    assert not df.empty

    cmds = df["suggested_safe_command"].tolist()
    for c in cmds:
        assert "live" not in c
        assert "broker" not in c
        assert "deploy" not in c
