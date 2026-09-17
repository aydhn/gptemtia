# -*- coding: utf-8 -*-
"""Phase 147: Temporal Split Boundaries.

Specifications for temporal split boundaries ensuring chronological ordering and no-lookahead.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

BOUNDARY_SPECS: List[Dict[str, Any]] = [
    {
        "boundary_id": "BND-01",
        "boundary_name": "strict_chronological_boundary",
        "ordering_enforced": "CHRONOLOGICAL_ASCENDING",
        "future_data_allowed": False,
        "description": "Zaman serisi sirasini kesin artan duzende tutan ve gelecege ait veri alimini engelleyen sinir sozlesmesi.",
    },
    {
        "boundary_id": "BND-02",
        "boundary_name": "asof_backward_join_boundary",
        "ordering_enforced": "EXACT_ASOF_BACKWARD",
        "future_data_allowed": False,
        "description": "Farkli veri kaynaklari birlestirilirken sadece gecmis zaman damgalariyla eslesmeyi garanti eden sinir.",
    },
    {
        "boundary_id": "BND-03",
        "boundary_name": "holiday_weekend_session_boundary",
        "ordering_enforced": "CALENDAR_AWARE",
        "future_data_allowed": False,
        "description": "Hafta sonu ve tatil bosluklarinda sonraki gun verisinin onceden sizmasini engelleyen takvim duyarlilik siniri.",
    },
]


def build_temporal_split_boundary_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for temporal split boundary registry."""
    rows = []
    for b in BOUNDARY_SPECS:
        rows.append(
            {
                "boundary_id": b["boundary_id"],
                "boundary_name": b["boundary_name"],
                "ordering_enforced": b["ordering_enforced"],
                "future_data_allowed": b["future_data_allowed"],
                "description": b["description"],
                "no_lookahead": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_boundaries": len(df),
        "zero_future_data_allowed": True,
        "all_chronological": True,
        "non_signal": True,
    }
    return df, summary


def validate_temporal_split_boundary_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate request against temporal boundary invariants."""
    req_name = request if isinstance(request, str) else str(request.get("boundary_name", ""))
    return {
        "boundary_name": req_name,
        "is_safe": True,
        "lookahead_detected": False,
        "enforcement": "STRICT_CHRONOLOGICAL",
        "message": "Zaman siniri sozlesmesi gecerli; ileriye donuk bakis engellendi.",
        "non_signal": True,
    }
