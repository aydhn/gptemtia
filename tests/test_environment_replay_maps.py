"""Test environment replay maps."""
from commodity_fx_signal_bot.local_reproducibility_governance.environment_replay_maps import (
    build_environment_replay_variable_registry, build_environment_replay_path_registry,
    build_environment_replay_dependency_note_registry, build_environment_replay_non_install_boundary_registry,
    build_environment_replay_machine_assumption_registry, build_environment_replay_limitation_register
)
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_replay_maps():
    p = get_default_local_reproducibility_governance_profile()
    df1, s1 = build_environment_replay_variable_registry(p)
    df2, s2 = build_environment_replay_path_registry(p)
    df3, s3 = build_environment_replay_dependency_note_registry(p)
    df4, s4 = build_environment_replay_non_install_boundary_registry(p)
    df5, s5 = build_environment_replay_machine_assumption_registry(p)
    df6, s6 = build_environment_replay_limitation_register(p)
    assert not df1.empty
    assert not df2.empty
    assert not df3.empty
    assert not df4.empty
    assert not df5.empty
    assert not df6.empty
