import pandas as pd
from synthetic_indices.index_models import (
    SyntheticIndexDefinition,
    SyntheticIndexSeries,
    build_synthetic_index_id,
    normalize_index_weights,
    synthetic_index_definition_to_dict
)

def test_build_synthetic_index_id_deterministic():
    id1 = build_synthetic_index_id("type", "1d", ["B", "A"], "equal")
    id2 = build_synthetic_index_id("type", "1d", ["A", "B"], "equal")
    assert id1 == id2

def test_normalize_index_weights():
    weights = {"A": 1.0, "B": 3.0}
    norm = normalize_index_weights(weights)
    assert norm["A"] == 0.25
    assert norm["B"] == 0.75

def test_synthetic_index_definition_to_dict():
    dfn = SyntheticIndexDefinition(
        index_id="test_id",
        index_name="Test Index",
        index_type="custom",
        timeframe="1d",
        symbols=["A", "B"],
        weights={"A": 0.5, "B": 0.5},
        weighting_scheme="equal",
        base_value=100.0,
        created_at_utc="2023-01-01",
        methodology="Test",
        warnings=[]
    )
    d = synthetic_index_definition_to_dict(dfn)
    assert d["index_id"] == "test_id"
    assert "Test Index" in d["index_name"]
    # Check that it is not a real index product
    assert "real index product" not in d["index_name"].lower()
