import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.command_timeline import classify_command_script, map_scripts_to_report_outputs

def test_classify_command_script():
    assert classify_command_script(Path("scripts/run_test.py"), Path(".")) == "run_script"
    assert classify_command_script(Path("scripts/update_test.py"), Path(".")) == "update_script"
    assert classify_command_script(Path("scripts/other.py"), Path(".")) == "other_script"

def test_map_scripts_to_report_outputs():
    df = pd.DataFrame([{"relative_path": "scripts/run_test.py"}])
    mapped = map_scripts_to_report_outputs(Path("."), df)
    assert not mapped.empty
    assert mapped.iloc[0]['inferred_report_output'] == "reports/output/test"
