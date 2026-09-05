import pytest
from pathlib import Path
from local_post_completion_preservation.preservation_config import get_default_local_post_completion_preservation_profile
from local_post_completion_preservation.archive_seal_rehearsal import *

def test_archive_seal():
    profile = get_default_local_post_completion_preservation_profile()
    text, summary = build_final_local_archive_seal_rehearsal_packet(Path("."), profile)
    assert len(text) > 0
    df, sum2 = build_archive_seal_checklist_registry(profile)
    assert len(df) > 0
