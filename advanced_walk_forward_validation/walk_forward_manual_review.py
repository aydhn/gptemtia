# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Manual Review Queue.

Queues items for operator review to verify that walk-forward validation contracts,
split boundaries, and benchmark baselines meet research integrity standards.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "review_id": "REV-WF-01",
        "item_type": "SPLIT_CONTRACT",
        "item_name": "walk_forward_split_contracts",
        "description": "Rolling, expanding ve anchored split parametrelerinin zaman serisi dinamiklerine uygunlugunu incele.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Pencere uzunluklarinin ve adim boyutlarinin piyasa rejimleriyle uyumunu dogrula.",
    },
    {
        "review_id": "REV-WF-02",
        "item_type": "OOS_BOUNDARY",
        "item_name": "oos_boundary_contracts",
        "description": "Orneklem disi kesisimsiz bolumleme sinirlarini ve holdout muhur durumunu denetle.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "OOS periyotlarinin egitim setinden sizinti almadigini teyit et.",
    },
    {
        "review_id": "REV-WF-03",
        "item_type": "PURGE_EMBARGO",
        "item_name": "purge_embargo_policy",
        "description": "Purge ve embargo tampon surelerinin otoregresif etkiyi kesmeye yeterli oldugunu denetle.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Etiket suresine bagli olarak en az 5-10 bar embargo araligi sagla.",
    },
    {
        "review_id": "REV-WF-04",
        "item_type": "BENCHMARK_CONTRACT",
        "item_name": "benchmark_universe_and_baselines",
        "description": "Buy & Hold, nakit ve esit agirlikli referans sozlesmelerinin gercekciligi.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Maliyet modeliyle entegre net referans getiri formullerini kontrol et.",
    },
    {
        "review_id": "REV-WF-05",
        "item_type": "METRIC_PLACEHOLDERS",
        "item_name": "validation_metric_placeholders",
        "description": "Metrik yer tutucularinin hesaplama yapmadan dogru formulleri gosterdigini incele.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Hesaplamanin kesinlikle kapali oldugunu teyit et.",
    },
    {
        "review_id": "REV-WF-06",
        "item_type": "BIAS_GUARDS",
        "item_name": "bias_and_lookahead_guards",
        "description": "Lookahead, data snooping ve survivorship muhafizlarinin aktifligini dogrula.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Yasakli kolon listesinin eksiksiz oldugunu kontrol et.",
    },
    {
        "review_id": "REV-WF-07",
        "item_type": "PHASE_148_BLOCKERS",
        "item_name": "phase_148_stress_test_prerequisites",
        "description": "Phase 148 Stress Testing and Scenario Simulation oncesi tum engellerin temizlendigini kontrol et.",
        "review_status": "PENDING_REVIEW",
        "recommendation": "Stress testi ve senaryo simulasyonlari sozlesme altyapisi icin hazir olun.",
    },
]


def build_walk_forward_manual_review_queue(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for manual review queue."""
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
                "destructive_action_allowed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_review_items": len(df),
        "pending_review_count": len(df),
        "zero_destructive_actions": True,
        "non_signal": True,
    }
    return df, summary
