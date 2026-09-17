# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Groups.

Provides specifications and registry for stress scenario group taxonomy.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SCENARIO_GROUPS: List[Dict[str, Any]] = [
    {
        "group_code": "HISTORICAL",
        "group_name": "Tarihsel Kriz Senaryoları",
        "description": "Geçmişte yaşanmış gerçek krizlerin (2008, 2020, 2010 vb.) parametrik kopyaları.",
    },
    {
        "group_code": "HYPOTHETICAL",
        "group_name": "Varsayımsal Kriz Senaryoları",
        "description": "Geleceğe dönük teorik, makroekonomik ve jeopolitik şok simülasyonları.",
    },
    {
        "group_code": "REGIME",
        "group_name": "Rejim Kırılması ve Geçiş Şokları",
        "description": "Piyasa davranışı, volatilite ve trend rejimlerindeki ani geçişler.",
    },
    {
        "group_code": "MICROSTRUCTURE_FRICTION",
        "group_name": "Mikroyapı ve Sürtünme Şokları",
        "description": "Spread patlaması, kayma (slippage), komisyon artışı ve likidite çekilmesi.",
    },
    {
        "group_code": "MACRO_SYSTEMIC",
        "group_name": "Makro ve Sistemik Şoklar",
        "description": "Merkez bankası faiz şokları, enflasyon sürprizleri ve resesyon dalgaları.",
    },
    {
        "group_code": "CROSS_ASSET_CONTAGION",
        "group_name": "Çapraz Varlık ve Bulaşma Şokları",
        "description": "FX, emtia, faiz ve tahvil piyasaları arasındaki negatif yayılım etkileri.",
    },
]


def build_stress_scenario_group_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress scenario groups."""
    rows: List[Dict[str, Any]] = []
    for g in SCENARIO_GROUPS:
        rows.append(
            {
                "group_code": g["group_code"],
                "group_name": g["group_name"],
                "description": g["description"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_scenario_groups": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
