from advanced_regime_matrix.regime_matrix_quality_dependencies import (
    build_regime_matrix_quality_dependencies,
    validate_matrix_quality_dependencies_satisfied,
)


def test_build_regime_matrix_quality_dependencies():
    df, s = build_regime_matrix_quality_dependencies()
    assert len(df) == 4
    assert s["total_dependencies"] == 4
    assert s["all_verified"] is True
    assert validate_matrix_quality_dependencies_satisfied() is True
