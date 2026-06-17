import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.evidence_timeline import classify_evidence_event, link_evidence_events_to_controls

def test_classify_evidence_event():
    assert classify_evidence_event(Path("a.txt"), Path(".")) == "evidence_update"

def test_link_evidence_events_to_controls():
    df = pd.DataFrame([{"relative_path": "a.txt"}])
    mapped = link_evidence_events_to_controls(Path("."), df)
    assert not mapped.empty
    assert mapped.iloc[0]['linked_control'] == "inferred_control"
