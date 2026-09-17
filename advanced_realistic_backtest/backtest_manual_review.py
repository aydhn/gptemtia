# -*- coding: utf-8 -*-
"""Phase 146: Backtest Manual Review Queue.

Queues items for non-destructive human operator review before proceeding to Phase 147.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "review_id": "REV-146-01",
        "item_type": "ENGINE_CONTRACTS",
        "item_name": "inspect_backtest_engine_contracts",
        "description": "Olay tabanli, vektorize ve portfoy seviyesi motor sozlesmelerini insan gozuyle inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Motor sozlesmelerindeki lookahead ve veri baglanti referanslarini dogrulayiniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-02",
        "item_type": "EXECUTION_ASSUMPTIONS",
        "item_name": "inspect_order_simulation_assumptions",
        "description": "Emir simule varsayimlarini (sifir aninda dolum, makas zorunlulugu, gecikme) inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Saf (naive) backtest varsayimlarinin tamamen elendigini dogrulayiniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-03",
        "item_type": "FILL_MODELS",
        "item_name": "inspect_fill_model_contracts",
        "description": "Gerceklesme fiyati (bid/ask/mid) ve sonraki bar acilis modellerini inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Makas payinin alis ve satista dogru yonde uygulandigini teyit ediniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-04",
        "item_type": "TRANSACTION_COST",
        "item_name": "inspect_transaction_cost_components",
        "description": "Komisyon, borsa takas ucreti ve alis-satis makas bilesenlerini inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Ucret baremlerinin hedef piyasa gercekleriyle uyumlu oldugunu kontrol ediniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-05",
        "item_type": "SLIPPAGE_MODELS",
        "item_name": "inspect_slippage_model_contracts",
        "description": "Sabit, oynaklik ve likiditeye dayali kayma sozlesmelerini inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Stresli donemlerde kayma carpani artirimi yapildigini dogrulayiniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-06",
        "item_type": "BIAS_GUARDS",
        "item_name": "inspect_no_lookahead_and_bias_guards",
        "description": "Lookahead, survivorship, snooping ve overfitting muhafizlarini inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Zaman damgasi siralamasi ve asof backward kurallarinin korundugunu dogrulayiniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-07",
        "item_type": "DISABLED_REPORTS",
        "item_name": "inspect_disabled_execution_reports",
        "description": "Canli islem, broker emri, optimizer ve model egitim yasaklarini inceleyiniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Hicbir canli trading veya broker yetkisinin verilmedigini teyit ediniz.",
        "destructive_action_allowed": False,
    },
    {
        "review_id": "REV-146-08",
        "item_type": "PHASE_147_PREP",
        "item_name": "inspect_phase_147_walk_forward_blockers",
        "description": "Phase 147 Walk-Forward ve OOS Benchmarking oncesi bloklayici unsurlari kontrol ediniz.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Tum sozlesme onkosullarinin saglandigindan emin olunuz.",
        "destructive_action_allowed": False,
    },
]


def build_backtest_manual_review_queue(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of items queued for operator manual review."""
    rows = []
    for r in REVIEW_ITEMS:
        rows.append(
            {
                "review_id": r["review_id"],
                "item_type": r["item_type"],
                "item_name": r["item_name"],
                "description": r["description"],
                "review_status": r["review_status"],
                "recommendation": r["recommendation"],
                "destructive_action_allowed": r["destructive_action_allowed"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_manual_review_queue(df)
    return df, summary


def summarize_backtest_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    return {
        "total_review_items": len(df),
        "zero_destructive_actions_allowed": bool((~df["destructive_action_allowed"]).all()) if not df.empty else True,
        "human_review_required": True,
        "non_signal": True,
    }
