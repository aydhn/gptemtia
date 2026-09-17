# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Manual Review Queue Module.

Compiles operator verification items ensuring human governance before Phase 150 progression.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    FINDING_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

MANUAL_REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "item_id": "REV_149_01",
        "title": "Inspect Monte Carlo Robustness Contracts",
        "category": "contract_governance",
        "inspection_focus": "Verify all 9 robustness families are defined with zero simulation execution enabled.",
    },
    {
        "item_id": "REV_149_02",
        "title": "Inspect Bootstrap and Resampling Contracts",
        "category": "methodological_integrity",
        "inspection_focus": "Check block bootstrap and stationary bootstrap specifications for autocorrelation preservation.",
    },
    {
        "item_id": "REV_149_03",
        "title": "Inspect Parameter Stability and Sensitivity Contracts",
        "category": "overfitting_prevention",
        "inspection_focus": "Verify parameter perturbation ranges and plateau detection criteria across strategies.",
    },
    {
        "item_id": "REV_149_04",
        "title": "Inspect Robustness Envelope and Distribution Placeholders",
        "category": "metric_safety",
        "inspection_focus": "Confirm all envelope bounds, quantiles, and VaR/ES placeholders remain uncalculated.",
    },
    {
        "item_id": "REV_149_05",
        "title": "Inspect No-Lookahead and Bias Guards",
        "category": "temporal_integrity",
        "inspection_focus": "Ensure zero forward return leakage and zero data snooping bias across registered tables.",
    },
    {
        "item_id": "REV_149_06",
        "title": "Inspect Disabled Execution Reports",
        "category": "safety_boundary",
        "inspection_focus": "Confirm simulation, training, optimizer, and live trading capabilities are disabled.",
    },
    {
        "item_id": "REV_149_07",
        "title": "Inspect Phase 150 Governance and Bias Control Blockers",
        "category": "handoff_readiness",
        "inspection_focus": "Confirm all 10 handoff prerequisites are satisfied prior to Phase 150 commencement.",
    },
]


def build_monte_carlo_manual_review_queue(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the manual review queue DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for item in MANUAL_REVIEW_ITEMS:
        rows.append(
            {
                "item_id": item["item_id"],
                "title": item["title"],
                "category": item["category"],
                "inspection_focus": item["inspection_focus"],
                "status": "PENDING_REVIEW",
                "safe_resolution": "Review contract metadata and formula definitions without executing simulations.",
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": FINDING_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": FINDING_DOMAIN,
        "total_review_items": len(df),
        "pending_review_count": len(df),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
