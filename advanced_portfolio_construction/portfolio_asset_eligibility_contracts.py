# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Asset Eligibility Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    ASSET_ELIGIBILITY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


ELIGIBILITY_RULES = [
    {"rule_id": "ELG_MIN_HISTORY", "rule_name": "Minimum History Contract", "condition": "history_days >= 252", "action_on_breach": "block_asset_contract", "description": "En az 252 is gunluk gecmis veri sartini tanimlar."},
    {"rule_id": "ELG_MAX_MISSINGNESS", "rule_name": "Maximum Missingness Contract", "condition": "missing_rate <= 0.05", "action_on_breach": "block_asset_contract", "description": "Eksik veri oraninin yuzde 5'i gecmemesi sartini tanimlar."},
    {"rule_id": "ELG_LIQUIDITY_FLOOR", "rule_name": "Liquidity Floor Contract", "condition": "daily_volume_rank >= 0.20", "action_on_breach": "block_asset_contract", "description": "Asgari likidite esik sozlesmesini tanimlar."},
    {"rule_id": "ELG_SPREAD_CEILING", "rule_name": "Spread Ceiling Contract", "condition": "relative_spread <= 0.02", "action_on_breach": "block_asset_contract", "description": "Azami spread sinir sartini tanimlar."},
    {"rule_id": "ELG_REGIME_COMPATIBILITY", "rule_name": "Regime Compatibility Contract", "condition": "regime_stability_score >= 0.40", "action_on_breach": "manual_review_required", "description": "Rejim uyumluluk asgari skor sartini tanimlar."},
    {"rule_id": "ELG_PRICE_SANITY", "rule_name": "Price Sanity Contract", "condition": "price > 0 and not_nan", "action_on_breach": "block_asset_contract", "description": "Pozitif ve gecerli fiyat veri sartini tanimlar."},
]


def build_portfolio_asset_eligibility_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for asset eligibility contracts."""
    rows = []
    for r in ELIGIBILITY_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "condition": r["condition"],
            "action_on_breach": r["action_on_breach"],
            "description": r["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_trade_decision": False,
            "investment_advice": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": ASSET_ELIGIBILITY_DOMAIN,
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "all_contract_only": True,
        "no_actual_trade_decision": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
