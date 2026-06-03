from portable_packaging.reproducible_setup import (
    build_reproducible_setup_steps,
    build_reproducible_setup_guide
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile
import pandas as pd

def test_reproducible_setup(tmp_path):
    profile = get_default_portable_packaging_profile()

    steps = build_reproducible_setup_steps(profile)
    assert len(steps) > 0

    md, sum = build_reproducible_setup_guide(None, pd.DataFrame(), pd.DataFrame(), profile)
    assert "Reproducible Setup Guide" in md
    assert "Canlı emir, broker entegrasyonu, model deploy işlemleri YOKTUR" in md
