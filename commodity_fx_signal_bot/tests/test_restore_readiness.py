import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.restore_readiness import build_archive_restore_readiness_checklist

def test_restore_readiness():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame()
    manifest = {"statements": {"local_only": True}}

    df, summary = build_archive_restore_readiness_checklist(item_df, manifest, profile)

    assert not df.empty

    # CHK_MAN should pass since manifest is provided
    man_chk = df[df["step_id"] == "CHK_MAN"]
    assert man_chk.iloc[0]["status"] == "pass"
