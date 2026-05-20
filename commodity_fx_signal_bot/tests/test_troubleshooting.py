from devtools.troubleshooting import build_common_issue_catalog, find_troubleshooting_steps, build_troubleshooting_markdown, build_troubleshooting_report

def test_troubleshooting_functions():
    df1 = build_common_issue_catalog()
    assert not df1.empty
    steps = find_troubleshooting_steps("env")
    assert len(steps) > 0
    md = build_troubleshooting_markdown()
    assert isinstance(md, str)
    df, summary = build_troubleshooting_report()
    assert "total_issues" in summary
