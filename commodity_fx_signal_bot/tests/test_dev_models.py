from devtools.dev_models import (
    CLICommandInfo, DXFinding, DXQualitySummary, build_dx_finding_id,
    cli_command_info_to_dict, dx_finding_to_dict, dx_quality_summary_to_dict
)

def test_build_dx_finding_id():
    fid = build_dx_finding_id("cat", "title", "file.py")
    assert "cat_title" in fid
    assert "file_py" in fid

def test_to_dict_methods():
    info = CLICommandInfo("name", "path", "group", "desc", "ex", True, True, False, False, None, [])
    d = cli_command_info_to_dict(info)
    assert "command_name" in d

    finding = DXFinding("id", "cat", "stat", "title", "desc")
    d2 = dx_finding_to_dict(finding)
    assert "finding_id" in d2

    summary = DXQualitySummary("id", "time", 1, 0, 0, 1, "dx_passed", [])
    d3 = dx_quality_summary_to_dict(summary)
    assert "summary_id" in d3
