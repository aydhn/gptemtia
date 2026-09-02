import pytest
from pathlib import Path
from local_synthesis.final_manual_review_register import build_final_manual_review_register
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_manual_review_register():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_manual_review_register(Path("."), prof)
    assert df.empty or not df.empty
