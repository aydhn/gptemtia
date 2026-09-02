import pandas as pd
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.dr_domain_registry import build_dr_domain_registry, build_default_dr_domains, summarize_dr_domains

def test_dr_domain_registry():
    profile = get_default_local_dr_profile()
    domains = build_default_dr_domains(profile)
    assert len(domains) == 2

    df, summary = build_dr_domain_registry(profile)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert summary["total_domains"] == 2
    assert summary["critical_domains"] == 1
