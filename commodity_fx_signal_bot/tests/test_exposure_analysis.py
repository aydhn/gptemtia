import pandas as pd
from config.symbols import SymbolSpec
from portfolio_research.portfolio_config import get_default_portfolio_research_profile
from portfolio_research.exposure_analysis import (
    build_symbol_metadata_table,
    calculate_asset_class_exposure,
    calculate_currency_exposure,
    calculate_symbol_exposure,
    infer_exposure_label
)

def test_exposure_analysis():
    specs = [
        SymbolSpec(symbol="A", asset_class="metals", base_currency="XAU", quote_currency="USD", currency="USD", name="test", sub_class="test"),
        SymbolSpec(symbol="B", asset_class="forex", base_currency="EUR", quote_currency="USD", currency="USD", name="test", sub_class="test")
    ]
    meta = build_symbol_metadata_table(specs)
    assert len(meta) == 2

    weights = {"A": 0.6, "B": 0.4}

    ac_exp = calculate_asset_class_exposure(weights, meta)
    assert len(ac_exp) == 2

    ccy_exp = calculate_currency_exposure(weights, meta)
    assert not ccy_exp.empty

    sym_exp = calculate_symbol_exposure(weights)
    assert len(sym_exp) == 2

    profile = get_default_portfolio_research_profile()
    label = infer_exposure_label(ac_exp, sym_exp, profile)
    assert label in ["balanced_exposure", "asset_class_concentrated", "symbol_concentrated", "currency_concentrated"]
