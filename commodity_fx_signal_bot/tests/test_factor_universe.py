from factor_research.factor_universe import build_factor_universe
from config.symbols import SymbolSpec

def test_factor_universe():
    specs = [SymbolSpec(symbol="A", name="A", asset_class="test", sub_class="test", currency="USD"), SymbolSpec(symbol="B", name="B", asset_class="test", sub_class="test", currency="USD")]
    valid, summary = build_factor_universe(specs, min_symbols=5)
    assert len(valid) == 2
    assert "insufficient_data: Universe size below minimum for factor research." in summary["warnings"]
