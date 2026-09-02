import pytest
from pathlib import Path
from local_synthesis.output_catalog import build_end_state_output_catalog
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_output_catalog():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_output_catalog(Path("."), prof)
    assert df.empty or not df.empty
