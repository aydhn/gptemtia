import pytest
from local_synthesis.local_only_statement import build_final_local_only_statement
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_local_only_statement():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_local_only_statement(prof)
    assert isinstance(text, str)
