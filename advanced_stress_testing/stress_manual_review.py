# -*- coding: utf-8 -*-
"""Phase 148: Stress Manual Review Queue.

Provides human operator review queue items and audits for stress testing and scenario contracts.
Strictly blocks destructive automated actions, approvals, and live execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressManualReviewItem

MANUAL_REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "review_id": "REV_STRESS_001",
        "item_type": "SCENARIO_CONTRACTS",
        "item_name": "stress_scenario_contracts",
        "description": "Temel stres senaryo sözleşmelerinin parametre ve bağımlılık kontrolü.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Sözleşme parametrelerini doğrula; otomatik stres yürütmesi yapma.",
    },
    {
        "review_id": "REV_STRESS_002",
        "item_type": "SHOCK_PLACEHOLDERS",
        "item_name": "shock_scenario_placeholders",
        "description": "Tarihsel ve varsayımsal şok yer tutucularının formül metaveri doğrulaması.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Yer tutucuların pnl_calculation_allowed=False olduğunu onayla.",
    },
    {
        "review_id": "REV_STRESS_003",
        "item_type": "FRICTION_SHOCKS",
        "item_name": "transaction_cost_and_slippage_shocks",
        "description": "Stresli spread, kayma ve komisyon modellerinin sınır kontrolü.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Ekstrem sürtünme katsayılarının aşırı uyum yaratmadığını denetle.",
    },
    {
        "review_id": "REV_STRESS_004",
        "item_type": "METRIC_PLACEHOLDERS",
        "item_name": "stress_and_scenario_metrics",
        "description": "VaR, ES, stressed drawdown formül tanımlarının incelenmesi.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Metriklerin gerçekte hesaplanmadığını teyit et.",
    },
    {
        "review_id": "REV_STRESS_005",
        "item_type": "GUARDS_AND_BIAS",
        "item_name": "no_lookahead_and_leakage_guards",
        "description": "Lookahead, senaryo sızıntısı ve yasaklı sütun korumalarının denetimi.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Tüm korumaların aktif olduğunu doğrula.",
    },
    {
        "review_id": "REV_STRESS_006",
        "item_type": "DISABLED_EXECUTION",
        "item_name": "disabled_execution_reports",
        "description": "Canlı işlem, broker, optimizer ve model eğitimi engellerinin doğrulanması.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Canlı trading ve broker bağlantısının kesin kapalı kaldığını onayla.",
    },
    {
        "review_id": "REV_STRESS_007",
        "item_type": "PHASE_149_HANDOFF",
        "item_name": "monte_carlo_robustness_prerequisites",
        "description": "Phase 149 Monte Carlo ve parametre stabilitesi devir gereksinimleri kontrolü.",
        "review_status": "PENDING_OPERATOR_AUDIT",
        "recommendation": "Phase 149 hazırlık paketini incele; üretim onayı vermeden devret.",
    },
]


def build_stress_manual_review_queue(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame queue of manual review items for human oversight."""
    rows: List[Dict[str, Any]] = []
    for item in MANUAL_REVIEW_ITEMS:
        review_item = StressManualReviewItem(
            review_id=item["review_id"],
            item_type=item["item_type"],
            item_name=item["item_name"],
            description=item["description"],
            review_status=item["review_status"],
            recommendation=item["recommendation"],
            destructive_action_allowed=False,
        )
        rows.append(
            {
                "review_id": review_item.review_id,
                "item_type": review_item.item_type,
                "item_name": review_item.item_name,
                "description": review_item.description,
                "review_status": review_item.review_status,
                "recommendation": review_item.recommendation,
                "destructive_action_allowed": review_item.destructive_action_allowed,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_review_items": len(df),
        "all_destructive_actions_blocked": not bool(df["destructive_action_allowed"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
