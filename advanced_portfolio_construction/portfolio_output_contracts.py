# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Output Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


PORTFOLIO_OUTPUT_SPECS = [
    {"field_name": "target_symbol", "field_type": "string", "nullable": False, "description": "Portfoydeki varlik sembol kodu."},
    {"field_name": "target_weight_contract", "field_type": "float", "nullable": True, "description": "Teorik agirlik sozlesme alani (Phase 153'te None/0.0)."},
    {"field_name": "target_notional_contract", "field_type": "float", "nullable": True, "description": "Teorik notional tutar sozlesme alani (Phase 153'te None/0.0)."},
    {"field_name": "regime_profile", "field_type": "string", "nullable": False, "description": "Rejim profili tanimi."},
    {"field_name": "risk_budget_assigned", "field_type": "float", "nullable": True, "description": "Tahsis edilen risk butcesi sozlesme alani."},
    {"field_name": "rebalance_timestamp", "field_type": "datetime", "nullable": True, "description": "Dengeleme zaman damgasi."},
    {"field_name": "contract_status", "field_type": "string", "nullable": False, "description": "Sozlesme onay durumu."},
]


def build_portfolio_output_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio output contract specifications."""
    rows = []
    for spec in PORTFOLIO_OUTPUT_SPECS:
        rows.append({
            "field_name": spec["field_name"],
            "field_type": spec["field_type"],
            "nullable": spec["nullable"],
            "description": spec["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_output_generated": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_DOMAIN,
        "category": "portfolio_output_contracts",
        "active_profile": profile.profile_name,
        "total_fields": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
