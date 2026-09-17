# -*- coding: utf-8 -*-
"""Phase 150: Backtest Result Release Boundaries.

Governs internal vs external dissemination of backtest findings.
Enforces that results can only be released as internal research hypotheses.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    RESULT_REPORTING_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

RELEASE_BOUNDARIES: List[Dict[str, Any]] = [
    {
        "boundary_id": "REL_01_INTERNAL_RESEARCH_ONLY",
        "name": "internal_research_release_only",
        "description": "Backtest documentation is strictly restricted to internal research; public or marketing release is prohibited.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "boundary_id": "REL_02_WATERMARK_REQUIREMENT",
        "name": "unverified_simulation_watermark_mandate",
        "description": "All visual charts and tabular outputs must bear the watermark: 'UNVERIFIED HISTORICAL RESEARCH HYPOTHESIS - NOT TRADING ADVICE'.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "boundary_id": "REL_03_NO_PROMOTIONAL_DISSEMINATION",
        "name": "promotional_performance_claim_prohibition",
        "description": "Strict prohibition against using backtest statistics in promotional, investor-facing, or capital-raising materials.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]


def build_backtest_result_release_boundary_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for result release boundaries."""
    rows: List[Dict[str, Any]] = []
    for r in RELEASE_BOUNDARIES:
        rows.append({
            "boundary_id": r["boundary_id"],
            "name": r["name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "public_release_allowed": False,
            "marketing_release_allowed": False,
            "status": "ENFORCED",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": RESULT_REPORTING_DOMAIN,
        "subdomain": "result_release_boundaries",
        "total_boundaries": len(df),
        "public_release_blocked": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
