from advanced_regime_matrix.regime_matrix_validation_dependencies import (
    build_regime_matrix_validation_dependencies,
    validate_matrix_validation_dependencies_satisfied,
)


def test_build_regime_matrix_validation_dependencies():
    df, s = build_regime_matrix_validation_dependencies()
    assert len(df) == 5
    assert s["total_dependencies"] == 5
    assert s["all_verified"] is True
    assert validate_matrix_validation_dependencies_satisfied() is True
