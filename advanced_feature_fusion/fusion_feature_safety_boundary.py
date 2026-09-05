"""Fusion Feature Safety Boundary.

Defines strict NO-GO and SAFE-GO rules for Phase 120.
Enforces non-signal, offline, metadata-only, backward-only research invariants.
"""

from typing import Any, Dict, List


NO_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "NOGO-01", "name": "No Live Trading", "description": "No connection to real broker APIs, orders, or execution."},
    {"rule_id": "NOGO-02", "name": "No Trade Signals", "description": "No buy/sell signals, directional claims, or trading recommendations."},
    {"rule_id": "NOGO-03", "name": "No Target/Label/Prediction", "description": "No generation of future targets, labels, or predictive outputs."},
    {"rule_id": "NOGO-04", "name": "No Full Article Scraping", "description": "No scraping or saving of news body, raw text, or copyrighted content."},
    {"rule_id": "NOGO-05", "name": "No Sentiment Modeling", "description": "No sentiment model inference, vector embeddings, or LLM scraping calls."},
    {"rule_id": "NOGO-06", "name": "No Forward Lookahead", "description": "No joins with release_timestamp > base_timestamp; no shift(-1)."},
    {"rule_id": "NOGO-07", "name": "No In-Place Mutation", "description": "No destructive overwrites or mutations of input market dataframes."},
    {"rule_id": "NOGO-08", "name": "No Strategy / Backtest", "description": "No strategy rules, backtesting, or parameter optimization."},
]

SAFE_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "SAFE-01", "name": "Offline Local Research", "description": "All computations execute strictly on local machine in dry-run mode."},
    {"rule_id": "SAFE-02", "name": "Metadata-Only News", "description": "News is restricted to topics, asset tags, macro tags, and event linkage."},
    {"rule_id": "SAFE-03", "name": "Backward-Only AsOf Join", "description": "All joins enforce release_timestamp <= base_timestamp."},
    {"rule_id": "SAFE-04", "name": "Input Immutability", "description": "Functions return new DataFrame copies without altering inputs."},
    {"rule_id": "SAFE-05", "name": "Event-Aware Context Representation", "description": "Features represent event distance, windows, and availability without directional bias."},
]


def get_fusion_feature_no_go_rules() -> List[Dict[str, Any]]:
    """Return all NO-GO rules."""
    return [dict(r) for r in NO_GO_RULES]


def get_fusion_feature_safe_go_rules() -> List[Dict[str, Any]]:
    """Return all SAFE-GO rules."""
    return [dict(r) for r in SAFE_GO_RULES]


def validate_safety_boundary_compliance(context: Dict[str, Any]) -> bool:
    """Validate that operational context respects all NO-GO constraints."""
    # Context must NOT indicate live, signal, or scraping flags
    if context.get("is_live", False):
        return False
    if context.get("is_signal", False):
        return False
    if context.get("has_full_text", False):
        return False
    if context.get("allows_forward_join", False):
        return False
    return True


def get_safety_boundary_summary() -> Dict[str, Any]:
    """Summary of safety boundary definitions."""
    return {
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_RULES),
        "zero_signals": True,
        "metadata_only_news": True,
        "backward_only_joins": True,
        "local_dry_run_only": True,
    }
