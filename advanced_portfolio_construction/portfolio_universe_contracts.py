# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Universe Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_UNIVERSE_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


UNIVERSE_ITEMS = [
    {"universe_id": "UNV_BRENT", "asset_symbol": "BRENT", "asset_class": "commodity", "sector": "energy", "currency": "USD", "eligibility_rule_ref": "COMMODITY_LIQUIDITY_RULE"},
    {"universe_id": "UNV_CRUDE_WTI", "asset_symbol": "CRUDE_WTI", "asset_class": "commodity", "sector": "energy", "currency": "USD", "eligibility_rule_ref": "COMMODITY_LIQUIDITY_RULE"},
    {"universe_id": "UNV_NATGAS", "asset_symbol": "NATGAS", "asset_class": "commodity", "sector": "energy", "currency": "USD", "eligibility_rule_ref": "COMMODITY_VOLATILITY_RULE"},
    {"universe_id": "UNV_GOLD", "asset_symbol": "GOLD", "asset_class": "commodity", "sector": "precious_metals", "currency": "USD", "eligibility_rule_ref": "SAFE_HAVEN_RULE"},
    {"universe_id": "UNV_SILVER", "asset_symbol": "SILVER", "asset_class": "commodity", "sector": "precious_metals", "currency": "USD", "eligibility_rule_ref": "COMMODITY_LIQUIDITY_RULE"},
    {"universe_id": "UNV_COPPER", "asset_symbol": "COPPER", "asset_class": "commodity", "sector": "industrial_metals", "currency": "USD", "eligibility_rule_ref": "CYCLICAL_COMMODITY_RULE"},
    {"universe_id": "UNV_EURUSD", "asset_symbol": "EURUSD", "asset_class": "fx", "sector": "g10_currency", "currency": "USD", "eligibility_rule_ref": "FX_MAJOR_LIQUIDITY_RULE"},
    {"universe_id": "UNV_USDJPY", "asset_symbol": "USDJPY", "asset_class": "fx", "sector": "g10_currency", "currency": "JPY", "eligibility_rule_ref": "FX_MAJOR_LIQUIDITY_RULE"},
    {"universe_id": "UNV_GBPUSD", "asset_symbol": "GBPUSD", "asset_class": "fx", "sector": "g10_currency", "currency": "USD", "eligibility_rule_ref": "FX_MAJOR_LIQUIDITY_RULE"},
    {"universe_id": "UNV_USDTRY", "asset_symbol": "USDTRY", "asset_class": "fx", "sector": "em_currency", "currency": "TRY", "eligibility_rule_ref": "FX_EM_VOLATILITY_RULE"},
]


def build_portfolio_universe_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio universe contracts."""
    rows = []
    for u in UNIVERSE_ITEMS:
        rows.append({
            "universe_id": u["universe_id"],
            "asset_symbol": u["asset_symbol"],
            "asset_class": u["asset_class"],
            "sector": u["sector"],
            "currency": u["currency"],
            "eligibility_rule_ref": u["eligibility_rule_ref"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "investment_advice": False,
            "actual_trading_universe": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_UNIVERSE_DOMAIN,
        "active_profile": profile.profile_name,
        "total_assets": len(df),
        "asset_classes": sorted(df["asset_class"].unique().tolist()) if not df.empty else [],
        "all_contract_only": True,
        "no_investment_advice": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
