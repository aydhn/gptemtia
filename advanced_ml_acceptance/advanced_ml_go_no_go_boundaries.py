# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Go / No-Go Boundary Registry."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    GO_NO_GO_BOUNDARY_DOMAIN,
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_BROKER_EXECUTION,
    NO_GO_PRODUCTION_DEPLOYMENT,
    NO_GO_MODEL_REGISTRY_WRITE,
    NO_GO_MODEL_TRAINING,
    NO_GO_PREDICTION,
    NO_GO_SIGNAL_GENERATION,
    NO_GO_BACKTEST_EXECUTION,
)

GO_ITEMS: List[Dict[str, Any]] = [
    {"decision_id": "GO-01", "decision": "GO", "topic": "proceed_to_phase_146_contract_planning", "allowed": True, "label": GO_CONTRACT_ONLY},
    {"decision_id": "GO-02", "decision": "GO", "topic": "proceed_to_backtest_contract_design", "allowed": True, "label": GO_CONTRACT_ONLY},
    {"decision_id": "GO-03", "decision": "GO", "topic": "proceed_to_transaction_cost_slippage_contract_design", "allowed": True, "label": GO_CONTRACT_ONLY},
    {"decision_id": "GO-04", "decision": "GO", "topic": "proceed_to_non_live_backtest_boundary_design", "allowed": True, "label": GO_CONTRACT_ONLY},
]

NO_GO_ITEMS: List[Dict[str, Any]] = [
    {"decision_id": "NOGO-01", "decision": "NO-GO", "topic": "live_trading", "allowed": False, "label": NO_GO_LIVE_TRADING},
    {"decision_id": "NOGO-02", "decision": "NO-GO", "topic": "broker_execution", "allowed": False, "label": NO_GO_BROKER_EXECUTION},
    {"decision_id": "NOGO-03", "decision": "NO-GO", "topic": "investment_advice", "allowed": False, "label": NO_GO_SIGNAL_GENERATION},
    {"decision_id": "NOGO-04", "decision": "NO-GO", "topic": "model_training", "allowed": False, "label": NO_GO_MODEL_TRAINING},
    {"decision_id": "NOGO-05", "decision": "NO-GO", "topic": "prediction", "allowed": False, "label": NO_GO_PREDICTION},
    {"decision_id": "NOGO-06", "decision": "NO-GO", "topic": "backtest_execution_in_phase_145", "allowed": False, "label": NO_GO_BACKTEST_EXECUTION},
    {"decision_id": "NOGO-07", "decision": "NO-GO", "topic": "model_registry_write", "allowed": False, "label": NO_GO_MODEL_REGISTRY_WRITE},
    {"decision_id": "NOGO-08", "decision": "NO-GO", "topic": "deployment", "allowed": False, "label": NO_GO_PRODUCTION_DEPLOYMENT},
    {"decision_id": "NOGO-09", "decision": "NO-GO", "topic": "production_approval", "allowed": False, "label": NO_GO_PRODUCTION_DEPLOYMENT},
    {"decision_id": "NOGO-10", "decision": "NO-GO", "topic": "broker_ready_approval", "allowed": False, "label": NO_GO_BROKER_EXECUTION},
    {"decision_id": "NOGO-11", "decision": "NO-GO", "topic": "signal_generation", "allowed": False, "label": NO_GO_SIGNAL_GENERATION},
]


def build_advanced_ml_go_no_go_boundary_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Go / No-Go boundaries."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for item in GO_ITEMS + NO_GO_ITEMS:
        row = dict(item)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": GO_NO_GO_BOUNDARY_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_boundaries": len(df),
        "go_count": len(GO_ITEMS),
        "no_go_count": len(NO_GO_ITEMS),
        "non_signal": True,
        "status": "SECURE",
    }
    return df, summary


def validate_advanced_ml_go_no_go_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate whether an action or request is Go (allowed) or No-Go (blocked)."""
    topic = request if isinstance(request, str) else request.get("topic", "")

    # Check against No-Go list
    for nogo in NO_GO_ITEMS:
        if nogo["topic"].lower() in topic.lower():
            return {
                "decision": "NO-GO",
                "topic": topic,
                "allowed": False,
                "reason": f"Action '{topic}' matches prohibited No-Go boundary '{nogo['topic']}'.",
                "label": nogo["label"],
            }

    # Check against Go list
    for go in GO_ITEMS:
        if go["topic"].lower() in topic.lower():
            return {
                "decision": "GO",
                "topic": topic,
                "allowed": True,
                "reason": f"Action '{topic}' permitted under contract-only research planning.",
                "label": go["label"],
            }

    # Default to No-Go if unrecognized
    return {
        "decision": "NO-GO",
        "topic": topic,
        "allowed": False,
        "reason": f"Action '{topic}' not explicitly permitted in Go registry.",
        "label": NO_GO_LIVE_TRADING,
    }


def summarize_advanced_ml_go_no_go_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Go / No-Go boundaries DataFrame."""
    return {
        "boundary_count": len(df),
        "go_count": int((df["decision"] == "GO").sum()) if not df.empty and "decision" in df.columns else 0,
        "no_go_count": int((df["decision"] == "NO-GO").sum()) if not df.empty and "decision" in df.columns else 0,
        "non_signal": True,
    }
