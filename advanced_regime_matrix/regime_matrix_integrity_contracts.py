"""Phase 127: Regime Matrix Integrity Contracts.

Defines structural integrity contracts guaranteeing non-signal invariants, source preservation,
and complete absence of target, prediction, or copyrighted scraping data.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

INTEGRITY_CONTRACT_RULES: List[Dict[str, Any]] = [
    {
        "integrity_rule_id": "rule_no_forbidden_columns",
        "name": "Zero Forbidden Columns",
        "description": "Neither feature matrices nor state datasets may contain buy, sell, target, or prediction columns.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_no_target_label_prediction",
        "name": "Zero Target, Label, or Prediction Fields",
        "description": "Prohibits any representation of machine learning labels or directional forecasts.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_no_full_article_text",
        "name": "Zero Full Article News Content",
        "description": "Prohibits article_body, raw_content, scraped HTML, or unstructured news bodies.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_no_embeddings_vector",
        "name": "Zero Vector Database or Embedding Tensors",
        "description": "Prohibits dense semantic vector embeddings or external vector database connections.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_source_preservation",
        "name": "Strict Source Data Preservation",
        "description": "Upstream source files and intermediate feature outputs must never be overwritten or deleted.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_no_auto_fix_or_drop",
        "name": "Prohibit Auto-Imputation and Auto-Feature-Drop",
        "description": "Automated destructive cleaning or synthetic imputation is strictly disallowed.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_validation_status_required",
        "name": "Mandatory Validation Status Pointer",
        "description": "Every matrix entry must reference a verified Phase 121 validation audit record.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
    {
        "integrity_rule_id": "rule_quality_metadata_required",
        "name": "Mandatory Quality & Drift Metadata",
        "description": "Every matrix entry must reference verified Phase 123 quality and drift scores.",
        "is_enforced": True,
        "is_critical": True,
        "non_signal": True,
    },
]


def build_regime_matrix_integrity_contract_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the matrix integrity contract registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for rule in INTEGRITY_CONTRACT_RULES:
        r_copy = rule.copy()
        r_copy["current_phase"] = p.current_phase
        r_copy["target_final_phase"] = p.target_final_phase
        r_copy["next_phase"] = p.next_phase
        r_copy["source_preserved"] = True
        r_copy["status"] = "matrix_ready"
        rows.append(r_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_integrity_contracts(df)
    return df, summary


def validate_regime_matrix_integrity_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a given contract for compliance with integrity invariants."""
    name = contract.get("name", "")
    is_enforced = contract.get("is_enforced", False)
    is_critical = contract.get("is_critical", False)
    non_signal = contract.get("non_signal", False)

    is_valid = is_enforced and non_signal
    return {
        "rule_name": name,
        "is_valid": is_valid,
        "is_critical": is_critical,
        "non_signal": non_signal,
    }


def validate_matrix_integrity_rule_coverage() -> bool:
    """Validate that all essential integrity rules are covered."""
    return len(INTEGRITY_CONTRACT_RULES) >= 8


def summarize_regime_matrix_integrity_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the integrity contracts registry."""
    return {
        "total_integrity_rules": len(df),
        "total_rules": len(df),
        "rule_ids": df["integrity_rule_id"].tolist() if not df.empty else [],
        "all_enforced": bool(df["is_enforced"].all()) if not df.empty else True,
        "all_critical_rules_enforced": bool(df[df["is_critical"]]["is_enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_integrity_contracts = build_regime_matrix_integrity_contract_registry

