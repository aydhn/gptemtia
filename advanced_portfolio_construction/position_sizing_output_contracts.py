# -*- coding: utf-8 -*-
"""Phase 153: Position Sizing Output Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    POSITION_SIZING_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


SIZING_OUTPUT_SPECS = [
    {"field_name": "target_symbol", "field_type": "string", "nullable": False, "description": "Pozisyon buyuklugu hesaplanan varlik sembol kodu."},
    {"field_name": "sizing_method", "field_type": "string", "nullable": False, "description": "Kullanilacak teorik pozisyon boyutlandirma yontemi sozlesmesi."},
    {"field_name": "recommended_fraction", "field_type": "float", "nullable": True, "description": "Teorik oransal buyukluk (Phase 153'te hesaplanmaz, None)."},
    {"field_name": "recommended_units", "field_type": "float", "nullable": True, "description": "Teorik birim/lot sayisi (Phase 153'te uretilmez, None)."},
    {"field_name": "volatility_target_annualized", "field_type": "float", "nullable": True, "description": "Yillik hedeflenen volatilite orani."},
    {"field_name": "drawdown_scale_factor", "field_type": "float", "nullable": True, "description": "Drawdown duyarlilik olcek katsayisi."},
    {"field_name": "contract_status", "field_type": "string", "nullable": False, "description": "Sozlesme onay durumu."},
]


def build_position_sizing_output_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for position sizing output contracts."""
    rows = []
    for spec in SIZING_OUTPUT_SPECS:
        rows.append({
            "field_name": spec["field_name"],
            "field_type": spec["field_type"],
            "nullable": spec["nullable"],
            "description": spec["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_units_generated": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": POSITION_SIZING_DOMAIN,
        "category": "position_sizing_output_contracts",
        "active_profile": profile.profile_name,
        "total_fields": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
