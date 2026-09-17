# -*- coding: utf-8 -*-
"""Phase 153: Risk Budget Output Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


RISK_BUDGET_OUTPUT_SPECS = [
    {"field_name": "budget_scope", "field_type": "string", "nullable": False, "description": "Risk butcesi kapsami (ASSET, STRATEGY, REGIME, PORTFOLIO)."},
    {"field_name": "target_identifier", "field_type": "string", "nullable": False, "description": "Hedef varlik, strateji veya rejim tanimlayicisi."},
    {"field_name": "allocated_vol_budget", "field_type": "float", "nullable": True, "description": "Tahsis edilen volatilite butcesi payi."},
    {"field_name": "allocated_drawdown_budget", "field_type": "float", "nullable": True, "description": "Tahsis edilen drawdown butcesi payi."},
    {"field_name": "allocated_exposure_budget", "field_type": "float", "nullable": True, "description": "Tahsis edilen maruziyet butcesi payi."},
    {"field_name": "contract_status", "field_type": "string", "nullable": False, "description": "Sozlesme onay durumu."},
]


def build_risk_budget_output_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for risk budget output contracts."""
    rows = []
    for spec in RISK_BUDGET_OUTPUT_SPECS:
        rows.append({
            "field_name": spec["field_name"],
            "field_type": spec["field_type"],
            "nullable": spec["nullable"],
            "description": spec["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_budget_enforced": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": RISK_BUDGET_DOMAIN,
        "category": "risk_budget_output_contracts",
        "active_profile": profile.profile_name,
        "total_fields": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
