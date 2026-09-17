# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Schedule Placeholders.

Placeholders for walk-forward execution schedules without creating any cron jobs or background tasks.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

SCHEDULE_SPECS: List[Dict[str, Any]] = [
    {
        "schedule_name": "monthly_recalibration_schedule_placeholder",
        "frequency": "MONTHLY_END_OF_MONTH",
        "cron_expression_placeholder": "0 0 L * *",
        "real_job_scheduled": False,
        "description": "Her ay sonu yapilacak yeniden kalibrasyon adimlarini sembolize eden yer tutucu sozlesme.",
    },
    {
        "schedule_name": "quarterly_rebalance_schedule_placeholder",
        "frequency": "QUARTERLY",
        "cron_expression_placeholder": "0 0 1 1,4,7,10 *",
        "real_job_scheduled": False,
        "description": "Ceyreklik rebalance ve OOS performans izleme yer tutucu sozlesmesi.",
    },
]


def build_walk_forward_schedule_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for schedule placeholder registry."""
    rows = []
    for s in SCHEDULE_SPECS:
        rows.append(
            {
                "schedule_name": s["schedule_name"],
                "frequency": s["frequency"],
                "cron_expression_placeholder": s["cron_expression_placeholder"],
                "real_job_scheduled": s["real_job_scheduled"],
                "description": s["description"],
                "scheduler_active": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_schedules": len(df),
        "all_real_jobs_disabled": True,
        "zero_scheduler_active": True,
        "non_signal": True,
    }
    return df, summary
