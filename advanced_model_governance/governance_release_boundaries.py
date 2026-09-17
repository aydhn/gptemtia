# -*- coding: utf-8 -*-
"""Phase 144: Governance Release Boundaries Registry."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

RELEASE_BOUNDARY_ITEMS: List[Dict[str, str]] = [
    {
        "boundary_id": "REL-01",
        "scope": "production_release",
        "description": "Production release is strictly disabled across all phases.",
        "enforcement": "Release pipeline trigger returns blocked status.",
    },
    {
        "boundary_id": "REL-02",
        "scope": "model_publish",
        "description": "Publishing models or weights to artifact stores/hubs is disabled.",
        "enforcement": "Artifact export intercepted and blocked.",
    },
    {
        "boundary_id": "REL-03",
        "scope": "live_stream_release",
        "description": "Streaming real-time execution signals to brokers is prohibited.",
        "enforcement": "Signal generation engine disconnected.",
    },
]


def build_governance_release_boundary_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance release boundaries."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in RELEASE_BOUNDARY_ITEMS:
        row = dict(item)
        row["release_allowed"] = False
        row["phase"] = prof.current_phase
        row["status"] = "BLOCKED_BY_POLICY"
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_release_boundaries(df)
    return df, summary


def summarize_governance_release_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance release boundaries."""
    return {
        "total_release_boundaries": len(df),
        "all_releases_blocked": not bool(df["release_allowed"].any()),
        "status": "ALL_BLOCKED",
    }


def validate_governance_release_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Intercept and reject release requests."""
    return {
        "request": str(request),
        "release_granted": False,
        "status": "BLOCKED_BY_POLICY",
        "reason": "Releases are disabled in non-production research layer.",
    }
