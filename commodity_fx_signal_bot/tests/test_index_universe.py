from config.symbols import SymbolSpec
from synthetic_indices.index_universe import (
    build_metals_universe,
    build_energy_universe,
    build_fx_try_universe,
    build_commodity_fx_universe
)

def test_universe_filtering():
    specs = [
        SymbolSpec(symbol="XAUUSD", name="Gold", asset_class="COMMODITY", sub_class="PRECIOUS_METAL", currency="USD", data_source="yahoo"),
        SymbolSpec(symbol="CL=F", name="Oil", asset_class="COMMODITY", sub_class="ENERGY", currency="USD", data_source="yahoo"),
        SymbolSpec(symbol="USDTRY=X", name="USD TRY", asset_class="FX", sub_class="EMERGING", currency="TRY", data_source="yahoo"),
        SymbolSpec(symbol="EURUSD=X", name="EUR USD", asset_class="FX", sub_class="MAJOR", currency="USD", data_source="yahoo")
    ]

    metals = build_metals_universe(specs)
    assert len(metals) == 1
    assert metals[0].symbol == "XAUUSD"

    energy = build_energy_universe(specs)
    assert len(energy) == 1
    assert energy[0].symbol == "CL=F"

    fx_try = build_fx_try_universe(specs)
    assert len(fx_try) == 1
    assert fx_try[0].symbol == "USDTRY=X"

    com_fx = build_commodity_fx_universe(specs)
    assert len(com_fx) == 3
