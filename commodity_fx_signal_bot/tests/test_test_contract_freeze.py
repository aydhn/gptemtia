
import pytest
import pandas as pd
from pathlib import Path
from local_hardening.test_contract_freeze import build_test_contract_freeze_registry
from local_hardening.hardening_config import get_default_local_hardening_profile

def test_test_contract_freeze():
    prof = get_default_local_hardening_profile()
    df, summary = build_test_contract_freeze_registry(Path("."), prof)
    assert isinstance(df, pd.DataFrame)


def test_dummy(): pass
