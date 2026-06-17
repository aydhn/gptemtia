import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.documentation_timeline import classify_documentation_type, map_docs_to_phase_references

def test_classify_documentation_type():
    assert classify_documentation_type(Path("docs/generated/a.md"), Path(".")) == "generated_documentation"
    assert classify_documentation_type(Path("docs/a.md"), Path(".")) == "source_documentation"

def test_map_docs_to_phase_references():
    df = pd.DataFrame([{"phase_number": 1, "relative_path": "docs/a.md"}])
    mapped = map_docs_to_phase_references(Path("."), df)
    assert not mapped.empty
    assert 'inferred_phase_ref' in mapped.columns
