from pathlib import Path
from local_project_completion.final_inventories import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_final_inventories():
    prof = get_default_local_project_completion_profile()
    df, sum1 = build_final_module_inventory(Path("."), prof)
    assert not df.empty
