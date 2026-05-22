from config.symbols import SymbolSpec
from synthetic_indices.index_config import get_default_synthetic_index_profile
from synthetic_indices.benchmark_definitions import (
    build_metals_composite_definition,
    build_energy_composite_definition,
    build_fx_try_composite_definition,
    build_default_synthetic_benchmark_definitions
)

def test_benchmark_definitions():
    specs = [
        SymbolSpec(symbol="XAUUSD", name="Gold", asset_class="COMMODITY", sub_class="PRECIOUS_METAL", currency="USD", data_source="yahoo"),
        SymbolSpec(symbol="XAGUSD", name="Silver", asset_class="COMMODITY", sub_class="PRECIOUS_METAL", currency="USD", data_source="yahoo"),
        SymbolSpec(symbol="CL=F", name="Oil", asset_class="COMMODITY", sub_class="ENERGY", currency="USD", data_source="yahoo"),
        SymbolSpec(symbol="USDTRY=X", name="USD TRY", asset_class="FX", sub_class="EMERGING", currency="TRY", data_source="yahoo"),
    ]

    profile = get_default_synthetic_index_profile()

    # We may get warnings for min symbols, but definitions should be created
    metals_def = build_metals_composite_definition(specs, "1d", profile)
    assert metals_def.index_type == "metals_composite_index"
    assert "XAUUSD" in metals_def.symbols
    assert "real index product" not in metals_def.index_name.lower()

    energy_def = build_energy_composite_definition(specs, "1d", profile)
    assert "CL=F" in energy_def.symbols

    fxtry_def = build_fx_try_composite_definition(specs, "1d", profile)
    assert "USDTRY=X" in fxtry_def.symbols

    defs, summary = build_default_synthetic_benchmark_definitions(specs, "1d", profile)
    assert len(defs) == 6 # Metals, Energy, Agri, FX_TRY, Commodity, Commodity_FX
    assert isinstance(defs, list)
