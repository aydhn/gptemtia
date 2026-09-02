from local_delivery.portable_reviewer_guide import build_portable_reviewer_archive_guide
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd
from pathlib import Path

def test_build_guide():
    prof = get_default_local_delivery_profile()
    text, summary = build_portable_reviewer_archive_guide(Path("."), pd.DataFrame(), prof)
    assert isinstance(text, str)
    assert "Review Order" in text
