# -*- coding: utf-8 -*-
"""Phase 153: Transaction-Cost-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    TRANSACTION_COST_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_transaction_cost_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build transaction cost-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "COST_TURNOVER_PENALTY", "penalty_model": "quadratic_turnover_penalty", "cost_basis_bps": 5.0, "description": "Karesel portfoy devir hizi maliyet cezasi taslagi."},
        {"placeholder_id": "COST_COMMISSION_AWARE", "penalty_model": "flat_commission_amortization", "cost_basis_bps": 2.0, "description": "Sabit komisyon itfa duyarli boyutlandirma taslagi."},
        {"placeholder_id": "COST_REBALANCE_DEADBAND", "penalty_model": "trade_size_deadband", "cost_basis_bps": 3.0, "description": "Kucuk rebalance islemlerini eleyen olu bant (deadband) taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "penalty_model": it["penalty_model"],
            "cost_basis_bps": it["cost_basis_bps"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_cost_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": TRANSACTION_COST_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
