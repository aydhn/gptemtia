# -*- coding: utf-8 -*-
"""Phase 148: Regime Shock Scenario Contracts.

Provides specifications and registry for sudden regime transitions and market state breakdown contracts.
Contract and metadata definition only; non-signal, no trading recommendation, no execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

REGIME_SHOCKS: List[Dict[str, Any]] = [
    {
        "shock_name": "regime_shock_sudden_trend_reversal",
        "regime_source": "BULLISH_EXPANSION",
        "regime_target": "BEARISH_CRASH",
        "description": "Ani Trend Dönüş Şoku: Güçlü yükseliş trendinden anlık ve sert düşüş rejimine geçiş.",
        "transition_speed": "INSTANTANEOUS_1_BAR",
        "expected_slippage_multiplier": "3.0x",
        "execution_allowed": False,
        "is_trading_signal": False,
    },
    {
        "shock_name": "regime_shock_volatility_breakout",
        "regime_source": "LOW_VOL_COMPRESSION",
        "regime_target": "EXTREME_VOL_EXPLOSION",
        "description": "Volatilite Patlaması Şoku: Düşük volatilite sıkışmasından 4x üzerinde aşırı volatilite rejimine geçiş.",
        "transition_speed": "FAST_2_BARS",
        "expected_slippage_multiplier": "4.5x",
        "execution_allowed": False,
        "is_trading_signal": False,
    },
    {
        "shock_name": "regime_shock_liquidity_drought",
        "regime_source": "NORMAL_LIQUIDITY",
        "regime_target": "ILLIQUID_FROZEN",
        "description": "Likidite Kuraklığı Şoku: Normal piyasa koşullarından emir defterinin boşaldığı illikit rejime geçiş.",
        "transition_speed": "MODERATE_5_BARS",
        "expected_slippage_multiplier": "6.0x",
        "execution_allowed": False,
        "is_trading_signal": False,
    },
    {
        "shock_name": "regime_shock_macro_regime_pivot",
        "regime_source": "DISINFLATION_GROWTH",
        "regime_target": "STAGFLATION_CRISIS",
        "description": "Makro Rejim Kırılması: Beklenmedik faiz/enflasyon verisiyle makro rejim kutbunun değişmesi.",
        "transition_speed": "SESSION_BOUNDARY",
        "expected_slippage_multiplier": "2.5x",
        "execution_allowed": False,
        "is_trading_signal": False,
    },
    {
        "shock_name": "regime_shock_cross_asset_decoupling",
        "regime_source": "HISTORICAL_CORRELATION",
        "regime_target": "COMPLETE_DECOUPLING",
        "description": "Çapraz Varlık Ayrışması: FX-Emtia arasındaki tarihsel bağın anlık kopması.",
        "transition_speed": "INSTANTANEOUS_1_BAR",
        "expected_slippage_multiplier": "3.5x",
        "execution_allowed": False,
        "is_trading_signal": False,
    },
]


def build_regime_shock_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of regime shock scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for s in REGIME_SHOCKS:
        rows.append(
            {
                "shock_name": s["shock_name"],
                "regime_source": s["regime_source"],
                "regime_target": s["regime_target"],
                "description": s["description"],
                "transition_speed": s["transition_speed"],
                "expected_slippage_multiplier": s["expected_slippage_multiplier"],
                "execution_allowed": s["execution_allowed"],
                "is_trading_signal": s["is_trading_signal"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_regime_shocks": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": not bool(df["is_trading_signal"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
