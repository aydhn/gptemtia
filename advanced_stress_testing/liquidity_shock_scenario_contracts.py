# -*- coding: utf-8 -*-
"""Phase 148: Liquidity Shock Scenario Contracts.

Provides specifications and registry for liquidity reduction and market depth collapse contracts.
Contract and metadata definition only; no actual liquidity shock execution or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

LIQUIDITY_SHOCKS: List[Dict[str, Any]] = [
    {
        "shock_name": "order_book_depth_halving_contract",
        "depth_reduction_ratio": 0.50,
        "description": "Emir Defteri Derinliği Yarılanması (%50 Kayıp): En iyi 5 kademedeki toplam lot hacminin yarıya inmesi.",
        "expected_slippage_impact": "+100%",
        "execution_allowed": False,
    },
    {
        "shock_name": "volume_freeze_80pct_contract",
        "depth_reduction_ratio": 0.80,
        "description": "İşlem Hacmi Donması (%80 Daralma): Piyasa katılımcılarının geri çekilmesiyle hacmin %20'ye düşmesi.",
        "expected_slippage_impact": "+250%",
        "execution_allowed": False,
    },
    {
        "shock_name": "quote_staleness_spike_contract",
        "depth_reduction_ratio": 0.60,
        "description": "Fiyat Bayatlaması ve Gecikme Şoku: Kotasyon güncelleme sıklığının 10x gecikmesi.",
        "expected_slippage_impact": "+150%",
        "execution_allowed": False,
    },
    {
        "shock_name": "illiquid_hours_execution_contract",
        "depth_reduction_ratio": 0.70,
        "description": "Likidite Düşük Seans Saatleri Şoku: Asya seansı sonu veya New York kapanışı sonrası sığ piyasa koşulları.",
        "expected_slippage_impact": "+180%",
        "execution_allowed": False,
    },
    {
        "shock_name": "bid_ask_depth_asymmetry_contract",
        "depth_reduction_ratio": 0.65,
        "description": "Alış-Satış Derinlik Asimetrisi: Panik satışta alış kademelerinin boşalması (bid-side vacuum).",
        "expected_slippage_impact": "+300%",
        "execution_allowed": False,
    },
]


def build_liquidity_shock_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of liquidity shock scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for s in LIQUIDITY_SHOCKS:
        rows.append(
            {
                "shock_name": s["shock_name"],
                "depth_reduction_ratio": s["depth_reduction_ratio"],
                "description": s["description"],
                "expected_slippage_impact": s["expected_slippage_impact"],
                "execution_allowed": s["execution_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_liquidity_shocks": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
