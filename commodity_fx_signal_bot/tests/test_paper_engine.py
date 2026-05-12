import pytest
import pandas as pd
from config.symbols import SymbolSpec
from paper.paper_engine import PaperTradingEngine
from paper.paper_config import get_default_paper_trading_profile

def test_paper_engine():
    spec = SymbolSpec("GC=F", "Gold", "commodity", "metals", "USD")
    profile = get_default_paper_trading_profile()
    engine = PaperTradingEngine(profile)

    price_df = pd.DataFrame(
        {'open': [100.0, 102.0], 'high': [105.0, 105.0], 'low': [95.0, 95.0], 'close': [101.0, 103.0], 'symbol': ['GC=F', 'GC=F']},
        index=pd.to_datetime(['2024-01-01', '2024-01-02'])
    )

    level_df = pd.DataFrame({
        'level_label': ['level_approved_candidate'],
        'directional_bias': ['long_bias'],
        'symbol': ['GC=F'],
        'close': [100.0],
        'stop_level': [90.0],
        'target_level': [110.0],
        'adjusted_theoretical_units': [1.0]
    }, index=[pd.to_datetime('2024-01-01')])

    from dataclasses import replace
    profile = replace(profile, require_risk_approval_candidate=False, require_sizing_approved_candidate=False)
    engine.profile = profile

    artifacts, summary = engine.run_symbol_paper(spec, "1d", price_df, level_df)

    assert "orders" in artifacts
    assert "positions" in artifacts
    assert summary["virtual_order_count"] == 1
