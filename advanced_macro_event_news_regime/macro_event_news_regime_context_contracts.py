"""Phase 132: Macro/Event/News Regime Context Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_CONTRACTS = [
    {
        "contract_name": "contract_macro_indicator_context",
        "context_type": "macro_indicator_context",
        "entity_type": "macro_indicator",
        "timestamp_policy_ref": "policy_backward_timestamp_only",
        "asof_policy_ref": "asof_backward_join_policy",
        "validation_dependency_ref": "val_dep_phase_120_121",
        "quality_dependency_ref": "qual_dep_phase_123_124",
        "source_phase_refs": ["Phase 120", "Phase 121", "Phase 126", "Phase 127"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_calendar_event_context",
        "context_type": "calendar_event_context",
        "entity_type": "calendar_event",
        "timestamp_policy_ref": "policy_scheduled_actual_alignment",
        "asof_policy_ref": "asof_backward_join_policy",
        "validation_dependency_ref": "val_dep_phase_127_128",
        "quality_dependency_ref": "qual_dep_phase_129_130",
        "source_phase_refs": ["Phase 120", "Phase 127", "Phase 128", "Phase 129"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_news_metadata_context",
        "context_type": "news_metadata_context",
        "entity_type": "news_metadata_entity",
        "timestamp_policy_ref": "policy_published_at_utc_only",
        "asof_policy_ref": "asof_backward_join_policy",
        "validation_dependency_ref": "val_dep_metadata_only_boundary",
        "quality_dependency_ref": "qual_dep_phase_131",
        "source_phase_refs": ["Phase 120", "Phase 121", "Phase 131"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
]


def build_macro_event_news_regime_context_contract_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro/event/news context contracts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_CONTRACTS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_contracts": len(df),
        "all_require_no_lookahead": True,
        "all_require_metadata_only": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def validate_macro_event_news_context_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a single contract satisfies Phase 132 safety and integrity invariants."""
    required_keys = [
        "contract_name",
        "context_type",
        "entity_type",
        "timestamp_policy_ref",
        "asof_policy_ref",
        "validation_dependency_ref",
        "quality_dependency_ref",
        "source_phase_refs",
        "metadata_only_news_required",
        "no_lookahead_required",
        "non_signal_required",
    ]
    missing = [k for k in required_keys if k not in contract]
    if missing:
        return {"valid": False, "missing_keys": missing, "contract_status": "INVALID"}

    is_safe = (
        contract.get("metadata_only_news_required", False)
        and contract.get("no_lookahead_required", False)
        and contract.get("non_signal_required", False)
    )

    return {
        "valid": is_safe,
        "contract_name": contract.get("contract_name"),
        "contract_status": "PASS" if is_safe else "FAIL_SAFETY_INVARIANT_VIOLATION",
    }


def summarize_macro_event_news_context_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for context contracts registry."""
    return {
        "total_contracts": len(df),
        "all_no_lookahead": bool(df["no_lookahead_required"].all()) if "no_lookahead_required" in df.columns else False,
        "all_metadata_only": bool(df["metadata_only_news_required"].all()) if "metadata_only_news_required" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
