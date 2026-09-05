from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_matrix_profile_registry import (
    build_regime_matrix_profile_registry,
)


def test_build_regime_matrix_profile_registry():
    prof = get_default_regime_matrix_profile()
    df, s = build_regime_matrix_profile_registry(prof)
    assert len(df) >= 3
    assert s["active_profile"] == prof.profile_name
    assert s["current_phase"] == 127
    assert s["next_phase"] == 128
    assert s["target_final_phase"] == 160
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert "strict_non_signal_regime_matrix_safety" in df["profile_name"].values
