import pytest
from pathlib import Path
from local_synthesis.final_limitation_register import build_final_limitation_register
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_limitation_register():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_limitation_register(Path("."), prof)
    assert not df.empty
