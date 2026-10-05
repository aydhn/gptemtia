
import pytest
import pandas as pd
from pathlib import Path
from local_hardening.rc_freeze_manifest import build_rc_dry_run_freeze_manifest, validate_rc_freeze_manifest_safety
from local_hardening.hardening_config import get_default_local_hardening_profile

def test_rc_freeze_manifest():
    prof = get_default_local_hardening_profile()
    m, s = build_rc_dry_run_freeze_manifest(Path("."), prof)
    assert isinstance(m, dict)
    assert "status" in m
