# -*- coding: utf-8 -*-
"""Phase 146: Order Simulation Contracts.

Defines specifications for simulating orders (market, limit, stop, stop-limit,
partial fill, and rejected orders) within a local backtest environment.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

ORDER_SIMULATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "simulation_type": "market_order_simulation_contract",
        "order_type": "MARKET",
        "description": "Piyasa emri simule sozlesmesi. Sonraki barin acilisinda veya anlik teklifte gerceklesme modeli.",
        "fill_model_ref": "next_tick_fill_model",
        "latency_model_ref": "network_latency_placeholder",
        "liquidity_constraint_ref": "adv_participation_limit",
        "broker_order_sent": False,
        "live_order_sent": False,
        "real_fill_occurred": False,
        "manual_review_required": True,
    },
    {
        "simulation_type": "limit_order_simulation_contract",
        "order_type": "LIMIT",
        "description": "Limit emir simule sozlesmesi. Fiyat belirlenen limit seviyeye ulastiginda gerceklesme kurali.",
        "fill_model_ref": "touch_or_cross_fill_model",
        "latency_model_ref": "exchange_queue_latency_placeholder",
        "liquidity_constraint_ref": "queue_priority_limit",
        "broker_order_sent": False,
        "live_order_sent": False,
        "real_fill_occurred": False,
        "manual_review_required": True,
    },
    {
        "simulation_type": "stop_order_simulation_contract",
        "order_type": "STOP",
        "description": "Stop zarar kes emri sozlesmesi. Tetiklenme fiyati goruldugunde piyasa emrine donusur.",
        "fill_model_ref": "stop_trigger_fill_model",
        "latency_model_ref": "trigger_delay_placeholder",
        "liquidity_constraint_ref": "gap_slippage_limit",
        "broker_order_sent": False,
        "live_order_sent": False,
        "real_fill_occurred": False,
        "manual_review_required": True,
    },
    {
        "simulation_type": "stop_limit_order_simulation_contract",
        "order_type": "STOP_LIMIT",
        "description": "Stop-limit emri sozlesmesi. Tetiklenme sonrasi limit emir olarak deftere yazilir.",
        "fill_model_ref": "stop_limit_fill_model",
        "latency_model_ref": "trigger_delay_placeholder",
        "liquidity_constraint_ref": "limit_bound_limit",
        "broker_order_sent": False,
        "live_order_sent": False,
        "real_fill_occurred": False,
        "manual_review_required": True,
    },
    {
        "simulation_type": "partial_fill_simulation_contract",
        "order_type": "PARTIAL_FILL",
        "description": "Kismi gerceklesme simule sozlesmesi. Emir buyuklugu mevcut bar hacminin belirli bir yuzdesini asarsa.",
        "fill_model_ref": "liquidity_capped_fill_model",
        "latency_model_ref": "multi_slice_latency_placeholder",
        "liquidity_constraint_ref": "bar_volume_cap_limit",
        "broker_order_sent": False,
        "live_order_sent": False,
        "real_fill_occurred": False,
        "manual_review_required": True,
    },
    {
        "simulation_type": "rejected_order_simulation_contract",
        "order_type": "REJECTED_ORDER",
        "description": "Reddedilen emir simule sozlesmesi. Yetersiz teminat, piyasa kapali veya fiyat limitleri disinda.",
        "fill_model_ref": "rejection_handler_model",
        "latency_model_ref": "instant_rejection_placeholder",
        "liquidity_constraint_ref": "market_halt_limit",
        "broker_order_sent": False,
        "live_order_sent": False,
        "real_fill_occurred": False,
        "manual_review_required": True,
    },
]


def build_order_simulation_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of order simulation contract specifications."""
    rows = []
    for c in ORDER_SIMULATION_CONTRACTS:
        rows.append(
            {
                "simulation_type": c["simulation_type"],
                "order_type": c["order_type"],
                "description": c["description"],
                "fill_model_ref": c["fill_model_ref"],
                "latency_model_ref": c["latency_model_ref"],
                "liquidity_constraint_ref": c["liquidity_constraint_ref"],
                "broker_order_sent": c["broker_order_sent"],
                "live_order_sent": c["live_order_sent"],
                "real_fill_occurred": c["real_fill_occurred"],
                "manual_review_required": c["manual_review_required"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_order_simulation_contracts(df)
    return df, summary


def summarize_order_simulation_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize order simulation contract registry."""
    return {
        "total_order_types": len(df),
        "all_broker_orders_blocked": bool((~df["broker_order_sent"]).all()) if not df.empty else True,
        "all_live_orders_blocked": bool((~df["live_order_sent"]).all()) if not df.empty else True,
        "all_real_fills_blocked": bool((~df["real_fill_occurred"]).all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
