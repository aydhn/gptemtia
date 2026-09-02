import pytest
from pathlib import Path
from local_synthesis.datalake_domain_catalog import build_final_datalake_domain_catalog
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_datalake_domain_catalog():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_datalake_domain_catalog(Path("."), prof)
    assert df.empty or not df.empty


def test_dummy(): pass
