# -*- coding: utf-8 -*-
"""Phase 148: Stress Forbidden Column Policies.

Enforces quarantine and strict rejection of forbidden trading, prediction,
realized stress PnL, full article, and leakage columns.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem

FORBIDDEN_COLUMNS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "realized_future_pnl",
    "future_pnl",
    "stressed_pnl",
    "actual_stressed_pnl",
    "stressed_drawdown",
    "actual_stressed_drawdown",
    "stress_return",
    "actual_stress_return",
    "scenario_performance",
    "actual_scenario_result",
    "actual_var",
    "actual_expected_shortfall",
    "performance_claim",
    "leak",
    "leakage",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_stress_forbidden_column_policy_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of forbidden column policies."""
    guard = StressGuardItem(
        guard_name="stress_forbidden_column_policy",
        guard_type="COLUMN_QUARANTINE",
        description="Stres testi veri setlerinde işlem sinyali, gerçekleşen PnL ve sızıntı kolonlarını engeller.",
        enforcement_level="STRICT",
        active=True,
        violating_columns=FORBIDDEN_COLUMNS,
    )
    rows = [
        {
            "guard_name": guard.guard_name,
            "guard_type": guard.guard_type,
            "description": guard.description,
            "enforcement_level": guard.enforcement_level,
            "active": guard.active,
            "prohibited_column_count": len(guard.violating_columns),
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "guard_active": guard.active,
        "enforcement_level": guard.enforcement_level,
        "forbidden_columns": guard.violating_columns,
        "total_forbidden_columns": len(guard.violating_columns),
        "non_signal": True,
    }
    return df, summary


def validate_stress_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect input column names and detect any quarantined forbidden columns."""
    normalized = [c.lower().strip() for c in column_names]
    violations = [c for c in normalized if c in FORBIDDEN_COLUMNS]
    return {
        "has_violations": len(violations) > 0,
        "violating_columns": violations,
        "is_safe": len(violations) == 0,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
