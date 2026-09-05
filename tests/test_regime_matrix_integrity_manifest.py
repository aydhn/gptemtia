from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_matrix_integrity_manifest import (
    build_regime_matrix_integrity_manifest,
)


def test_build_regime_matrix_integrity_manifest():
    prof = get_default_regime_matrix_profile()
    df, s = build_regime_matrix_integrity_manifest(prof)
    assert len(df) == 1
    assert s["manifest_status"] == "MANIFEST_VALID"
    assert s["current_phase"] == 127
    assert s["next_phase"] == 128
    assert s["target_final_phase"] == 160
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    assert s["production_ready"] is False
    assert s["broker_ready"] is False
