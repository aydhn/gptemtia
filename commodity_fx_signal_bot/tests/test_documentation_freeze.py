
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.documentation_freeze import build_documentation_freeze_snapshot, build_readme_docs_freeze_checklist
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_documentation_freeze():
    prof = get_default_local_hardening_profile()
    df1, s1 = build_documentation_freeze_snapshot(Path("."), prof)
    assert isinstance(df1, pd.DataFrame)
    df2, s2 = build_readme_docs_freeze_checklist(Path("."), prof)
    assert isinstance(df2, pd.DataFrame)


def test_dummy(): pass
