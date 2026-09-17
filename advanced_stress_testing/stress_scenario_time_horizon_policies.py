# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Time Horizon Policies.

Provides specifications and registry for stress scenario duration and temporal window policies.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

TIME_HORIZON_POLICIES: List[Dict[str, Any]] = [
    {
        "horizon_level": "INSTANTANEOUS",
        "label": "Anlık Tek Çubuk Şoku",
        "typical_duration": "1 bar (1m / 5m / 1h)",
        "description": "Fiyat boşlukları (gap), ani emir iptali veya tek dakikalık flash crash.",
    },
    {
        "horizon_level": "INTRADAY",
        "label": "Gün İçi Sürtünme Şoku",
        "typical_duration": "1 - 8 saat",
        "description": "Veri açıklanma seansı, açılış/kapanış türbülansı veya seans boyu likidite daralması.",
    },
    {
        "horizon_level": "SHORT_TERM",
        "label": "Kısa Vadeli Şok Penceresi",
        "typical_duration": "1 - 5 işlem günü",
        "description": "Haftalık kriz şoku, ani rejim kırılması veya faiz kararı sonrası trend şoku.",
    },
    {
        "horizon_level": "MEDIUM_TERM",
        "label": "Orta Vadeli Kriz Dönemi",
        "typical_duration": "2 - 6 hafta",
        "description": "Jeopolitik kriz başlangıcı, tedarik zinciri kesintisi veya devalüasyon süreci.",
    },
    {
        "horizon_level": "PROLONGED",
        "label": "Uzamış Resesyon / Ayı Piyasası",
        "typical_duration": "3 - 12 ay",
        "description": "Yapısal ayı piyasası, stagflasyon veya uzun süreli kredi daralması.",
    },
]


def build_stress_scenario_time_horizon_policy_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress scenario time horizon policies."""
    rows: List[Dict[str, Any]] = []
    for h in TIME_HORIZON_POLICIES:
        rows.append(
            {
                "horizon_level": h["horizon_level"],
                "label": h["label"],
                "typical_duration": h["typical_duration"],
                "description": h["description"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_time_horizons": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
