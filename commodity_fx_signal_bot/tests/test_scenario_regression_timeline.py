import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.scenario_regression_timeline import classify_scenario_regression_event, link_scenario_events_to_regression_outputs

def test_classify_scenario_regression_event():
    assert classify_scenario_regression_event(Path("a.txt"), Path(".")) == "regression_update"

def test_link_scenario_events_to_regression_outputs():
    df = pd.DataFrame([{"relative_path": "a.txt"}])
    mapped = link_scenario_events_to_regression_outputs(Path("."), df)
    assert not mapped.empty
    assert mapped.iloc[0]['linked_output'] == "inferred_output"
