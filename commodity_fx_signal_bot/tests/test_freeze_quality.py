
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.freeze_quality import build_final_freeze_quality_report
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_freeze_quality():
    prof = get_default_local_hardening_profile()
    q = build_final_freeze_quality_report({"total": 0})
    assert isinstance(q, dict)
    assert "no_release_claim_confirmed" in q
    assert not q.get("forbidden_terms_found")
