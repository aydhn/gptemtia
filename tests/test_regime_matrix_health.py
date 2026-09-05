from advanced_regime_matrix.regime_matrix_health import (
    run_regime_matrix_health_check,
)


def test_run_regime_matrix_health_check():
    df, s = run_regime_matrix_health_check()
    assert len(df) == 12
    assert s["total_subsystems"] == 12
    assert s["healthy_subsystems"] == 12
    assert s["degraded_subsystems"] == 0
    assert s["overall_health"] == "HEALTHY"
    assert s["non_signal"] is True
    assert s["model_training_executed"] is False
