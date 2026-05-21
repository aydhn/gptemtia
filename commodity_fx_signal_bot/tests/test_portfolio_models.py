from portfolio_research.portfolio_models import (
    build_virtual_basket_id,
    normalize_weights,
    virtual_basket_definition_to_dict,
    VirtualBasketDefinition
)

def test_build_virtual_basket_id():
    id1 = build_virtual_basket_id("equal", "1d", ["AAPL", "MSFT"])
    id2 = build_virtual_basket_id("equal", "1d", ["MSFT", "AAPL"])
    assert id1 == id2
    assert id1.startswith("vb_")

def test_normalize_weights():
    w = {"A": 2.0, "B": 2.0}
    norm = normalize_weights(w)
    assert norm["A"] == 0.5
    assert norm["B"] == 0.5

def test_dataclass_to_dict():
    b = VirtualBasketDefinition(
        basket_id="b1",
        basket_name="test",
        basket_type="equal",
        timeframe="1d",
        symbols=["A"],
        weights={"A": 1.0},
        created_at_utc="2023-01-01T00:00:00",
        methodology="test"
    )
    d = virtual_basket_definition_to_dict(b)
    assert "basket_id" in d
    assert d["basket_name"] == "test"
