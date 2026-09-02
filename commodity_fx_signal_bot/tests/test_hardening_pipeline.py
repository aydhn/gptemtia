
import pytest
import pandas as pd
from pathlib import Path
from unittest.mock import MagicMock
from commodity_fx_signal_bot.local_hardening.hardening_pipeline import LocalHardeningPipeline
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_hardening_pipeline():
    dl = MagicMock()
    prof = get_default_local_hardening_profile()
    p = LocalHardeningPipeline(dl, None, Path("."), prof)
    dfs, s = p.build_hardening_domain_registry(save=True)
    assert dl.save_hardening_domain_registry.called
    assert "hardening_domain_registry" in dfs
    
    dfs2, s2 = p.build_dead_code_review(save=True)
    assert dl.save_dead_code_candidate_report.called
    
    dfs3, s3 = p.build_contract_freeze_catalog(save=True)
    assert dl.save_contract_surface_registry.called
    
    dfs4, s4 = p.build_documentation_freeze(save=True)
    assert dl.save_documentation_freeze_snapshot.called
    
    dfs5, s5 = p.build_rc_dry_run_freeze(save=True)
    assert dl.save_rc_dry_run_freeze_manifest.called
