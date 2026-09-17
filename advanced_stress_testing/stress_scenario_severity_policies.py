# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Severity Policies.

Provides specifications and registry for shock severity classifications and parameters.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SEVERITY_POLICIES: List[Dict[str, Any]] = [
    {
        "severity_level": "MILD",
        "label": "Hafif Şok Seviyesi",
        "volatility_multiplier_range": "1.2x - 1.8x",
        "spread_multiplier_range": "1.5x - 2.0x",
        "liquidity_drop_pct": "15% - 25%",
        "description": "Rutin piyasa dalgalanması ve standart makro veri tepkisi.",
    },
    {
        "severity_level": "MODERATE",
        "label": "Orta Şiddetli Şok Seviyesi",
        "volatility_multiplier_range": "1.8x - 2.5x",
        "spread_multiplier_range": "2.0x - 3.5x",
        "liquidity_drop_pct": "25% - 40%",
        "description": "Öngörülemeyen faiz kararları veya orta çaplı jeopolitik gerginlik.",
    },
    {
        "severity_level": "SEVERE",
        "label": "Şiddetli Kriz Seviyesi",
        "volatility_multiplier_range": "2.5x - 4.0x",
        "spread_multiplier_range": "3.5x - 6.0x",
        "liquidity_drop_pct": "40% - 60%",
        "description": "Sistemik finansal stres, bankacılık baskısı veya bölgesel kriz.",
    },
    {
        "severity_level": "EXTREME",
        "label": "Aşırı Kriz Seviyesi",
        "volatility_multiplier_range": "4.0x - 6.0x",
        "spread_multiplier_range": "6.0x - 10.0x",
        "liquidity_drop_pct": "60% - 80%",
        "description": "Büyük küresel kriz (2008 GFC dengi), piyasa kilitlenmesi.",
    },
    {
        "severity_level": "BLACK_SWAN",
        "label": "Siyah Kuğu Kuyruk Riski",
        "volatility_multiplier_range": "> 6.0x",
        "spread_multiplier_range": "> 10.0x",
        "liquidity_drop_pct": "> 80%",
        "description": "Eşi benzeri görülmemiş rejim çöküşü (2020 negatif petrol, CHF depeg vb.).",
    },
]


def build_stress_scenario_severity_policy_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress scenario severity policies."""
    rows: List[Dict[str, Any]] = []
    for s in SEVERITY_POLICIES:
        rows.append(
            {
                "severity_level": s["severity_level"],
                "label": s["label"],
                "volatility_multiplier_range": s["volatility_multiplier_range"],
                "spread_multiplier_range": s["spread_multiplier_range"],
                "liquidity_drop_pct": s["liquidity_drop_pct"],
                "description": s["description"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_severity_levels": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
