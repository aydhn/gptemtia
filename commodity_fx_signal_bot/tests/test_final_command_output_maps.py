from pathlib import Path
from local_project_completion.final_command_output_maps import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_final_command_output_maps():
    prof = get_default_local_project_completion_profile()
    df1, sum1 = build_final_command_map(Path("."), prof)
    df2, sum2 = build_final_output_map(Path("."), prof)
    assert not df1.empty
    assert not df2.empty
