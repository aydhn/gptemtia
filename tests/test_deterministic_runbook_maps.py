"""Test runbook maps."""
from commodity_fx_signal_bot.local_reproducibility_governance.deterministic_runbook_maps import (
    build_deterministic_command_sequence_registry, build_deterministic_output_expectation_registry,
    build_deterministic_rerun_checklist, build_deterministic_rerun_boundary_registry
)
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_runbook_maps():
    p = get_default_local_reproducibility_governance_profile()
    df1, s1 = build_deterministic_command_sequence_registry(p)
    df2, s2 = build_deterministic_output_expectation_registry(p)
    df3, s3 = build_deterministic_rerun_checklist(p)
    df4, s4 = build_deterministic_rerun_boundary_registry(p)
    assert not df1.empty
    assert not df2.empty
    assert not df3.empty
    assert not df4.empty
