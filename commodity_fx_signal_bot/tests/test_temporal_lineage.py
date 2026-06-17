import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.temporal_lineage import infer_temporal_predecessors, infer_temporal_successors, build_artifact_temporal_lineage
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_infer_temporal_predecessors():
    event_data = [
        {"relative_path": "a.txt", "module_name": "modA", "event_time_utc": "2023-01-01T00:00:00Z"},
        {"relative_path": "b.txt", "module_name": "modA", "event_time_utc": "2023-01-02T00:00:00Z"}
    ]
    df = pd.DataFrame(event_data)
    preds = infer_temporal_predecessors("b.txt", df)
    assert "a.txt" in preds

def test_infer_temporal_successors():
    event_data = [
        {"relative_path": "a.txt", "module_name": "modA", "event_time_utc": "2023-01-01T00:00:00Z"},
        {"relative_path": "b.txt", "module_name": "modA", "event_time_utc": "2023-01-02T00:00:00Z"}
    ]
    df = pd.DataFrame(event_data)
    succs = infer_temporal_successors("a.txt", df)
    assert "b.txt" in succs

def test_build_artifact_temporal_lineage():
    event_data = [
        {"relative_path": "a.txt", "module_name": "modA", "event_time_utc": "2023-01-01T00:00:00Z"},
        {"relative_path": "b.txt", "module_name": "modA", "event_time_utc": "2023-01-02T00:00:00Z"}
    ]
    evo_data = [{"artifact_id": "1", "relative_path": "b.txt"}]
    df_evt = pd.DataFrame(event_data)
    df_evo = pd.DataFrame(evo_data)
    profile = get_default_local_timeline_profile()
    df, summary = build_artifact_temporal_lineage(df_evt, df_evo, profile)

    assert not df.empty
    assert "a.txt" in df.iloc[0]['predecessors']
