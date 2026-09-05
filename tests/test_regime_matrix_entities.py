from advanced_regime_matrix.regime_matrix_entities import (
    build_regime_matrix_entity_registry,
    build_regime_matrix_entities_registry,
    CANONICAL_ENTITIES,
)


def test_regime_matrix_entities_registry():
    df, s = build_regime_matrix_entity_registry()
    assert len(df) == 9
    assert s["total_entities"] == 9
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True

    types = set(df["entity_type"].values)
    assert "fx_pair" in types
    assert "commodity_symbol" in types
    assert "macro_indicator" in types
    assert "calendar_event" in types
    assert "news_metadata_tag" in types
    assert "cross_asset_context" in types
    assert "factor_family" in types
    assert "regime_family" in types
    assert "regime_state_candidate_context" in types


def test_build_regime_matrix_entities_registry_alias():
    df, s = build_regime_matrix_entities_registry()
    assert len(df) == 9
    assert s["status"] == "matrix_ready"
