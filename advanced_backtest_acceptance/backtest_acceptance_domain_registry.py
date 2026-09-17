# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    ALL_DOMAINS,
    BACKTEST_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)


def build_backtest_acceptance_domain_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest acceptance domains."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for domain_name in ALL_DOMAINS:
        records.append({
            "domain_name": domain_name,
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": BACKTEST_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "total_domains": len(records),
        "all_ready": True,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
