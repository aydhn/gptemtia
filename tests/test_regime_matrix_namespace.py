from advanced_regime_matrix.regime_matrix_namespace import (
    build_regime_matrix_key,
    validate_regime_matrix_key,
    build_regime_matrix_namespace_registry,
    summarize_regime_matrix_namespace,
    FORBIDDEN_TERMS,
)


def test_build_regime_matrix_key():
    key = build_regime_matrix_key("fx", "eur_usd", "trend_context")
    assert key == "regime_matrix__fx__eur_usd__trend_context"


def test_validate_regime_matrix_key():
    clean_key = "regime_matrix__fx__eur_usd__trend_context"
    res_clean = validate_regime_matrix_key(clean_key)
    assert res_clean["is_valid"] is True
    assert res_clean["starts_correctly"] is True
    assert res_clean["is_snake_case"] is True
    assert len(res_clean["forbidden_hits"]) == 0

    dirty_key = "regime_matrix__fx__eur_usd__buy_signal"
    res_dirty = validate_regime_matrix_key(dirty_key)
    assert res_dirty["is_valid"] is False
    assert len(res_dirty["forbidden_hits"]) >= 2


def test_build_regime_matrix_namespace_registry():
    df, s = build_regime_matrix_namespace_registry()
    assert len(df) == 4
    assert s["total_conventions"] == 4
    assert s["status"] == "matrix_ready"
