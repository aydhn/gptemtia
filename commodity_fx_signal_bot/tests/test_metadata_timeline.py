import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.metadata_timeline import classify_metadata_card_event, link_metadata_events_to_artifacts

def test_classify_metadata_card_event():
    assert classify_metadata_card_event(Path("model_card.json"), Path(".")) == "model_metadata"
    assert classify_metadata_card_event(Path("dataset_card.json"), Path(".")) == "dataset_metadata"
    assert classify_metadata_card_event(Path("experiment_card.json"), Path(".")) == "experiment_metadata"
    assert classify_metadata_card_event(Path("other.json"), Path(".")) == "general_metadata"

def test_link_metadata_events_to_artifacts():
    df = pd.DataFrame([{"relative_path": "a.json"}])
    mapped = link_metadata_events_to_artifacts(Path("."), df)
    assert not mapped.empty
    assert mapped.iloc[0]['linked_artifact'] == "inferred_artifact"
