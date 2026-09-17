# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Asset Scope Policies.

Provides specifications and registry for stress scenario asset coverage policies.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

ASSET_SCOPE_POLICIES: List[Dict[str, Any]] = [
    {
        "scope_code": "COMMODITY_ENERGY",
        "label": "Enerji Emtiaları Kapsamı",
        "symbols": ["BRENT", "WTI"],
        "description": "Ham petrol ve enerji türevleri için stres testi kapsamı.",
    },
    {
        "scope_code": "COMMODITY_METALS",
        "label": "Değerli ve Sanayi Metalleri",
        "symbols": ["GOLD", "SILVER", "COPPER"],
        "description": "Değerli sığınak metalleri ve sanayi metalleri kapsamı.",
    },
    {
        "scope_code": "FX_MAJORS",
        "label": "G10 Majör Döviz Çiftleri",
        "symbols": ["EURUSD", "GBPUSD", "USDJPY"],
        "description": "Yüksek likiditeli küresel majör döviz pariteleri kapsamı.",
    },
    {
        "scope_code": "FX_EMERGING",
        "label": "Gelişmekte Olan Para Birimleri",
        "symbols": ["USDTRY"],
        "description": "Yüksek volatilite ve faiz hassasiyeti olan gelişmekte olan kurlar.",
    },
    {
        "scope_code": "CROSS_ASSET_MULTI",
        "label": "Bütünleşik Çoklu Varlık Evreni",
        "symbols": ["BRENT", "WTI", "GOLD", "SILVER", "COPPER", "EURUSD", "GBPUSD", "USDJPY", "USDTRY"],
        "description": "Sistemik stres ve çapraz varlık bulaşma analizleri için tüm varlıklar.",
    },
]


def build_stress_scenario_asset_scope_policy_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress scenario asset scope policies."""
    rows: List[Dict[str, Any]] = []
    for a in ASSET_SCOPE_POLICIES:
        rows.append(
            {
                "scope_code": a["scope_code"],
                "label": a["label"],
                "symbols": ",".join(a["symbols"]),
                "symbol_count": len(a["symbols"]),
                "description": a["description"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_asset_scopes": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
