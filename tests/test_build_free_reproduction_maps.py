"""Test build free maps."""
from commodity_fx_signal_bot.local_reproducibility_governance.build_free_reproduction_maps import (
    build_build_free_reproduction_reading_order, build_build_free_reproduction_script_map,
    build_build_free_reproduction_report_map, build_build_free_reproduction_datalake_map
)
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_build_free_maps():
    p = get_default_local_reproducibility_governance_profile()
    df1, s1 = build_build_free_reproduction_reading_order(p)
    df2, s2 = build_build_free_reproduction_script_map(p)
    df3, s3 = build_build_free_reproduction_report_map(p)
    df4, s4 = build_build_free_reproduction_datalake_map(p)
    assert not df1.empty
    assert not df2.empty
    assert not df3.empty
    assert not df4.empty
