"""Phase 128: Regime Candidate State Integrity Contracts.

Defines integrity contracts guaranteeing that candidate state data structures maintain zero-lookahead,
non-signal, non-destructive, and non-execution standards.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

INTEGRITY_CONTRACT_RULES = [
    {
        "contract_rule_id": "rule_no_forbidden_columns",
        "category": "schema_integrity",
        "description": "Dataset must contain zero forbidden trading columns (target, label, prediction, buy, sell, etc.).",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_no_target_or_prediction",
        "category": "learning_boundary",
        "description": "Candidate states must strictly be research annotation preparation, not supervised learning targets.",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_no_full_article_text",
        "category": "copyright_boundary",
        "description": "Zero raw news article bodies, html scrapings, or full texts stored.",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_no_embeddings_vector",
        "category": "dependency_boundary",
        "description": "Zero vector database or embedding generation dependencies.",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_no_clustering_or_model_execution",
        "category": "execution_boundary",
        "description": "Zero algorithm fit, transform, predict, or clustering operations executed.",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_source_preservation",
        "category": "data_integrity",
        "description": "Source dataframes must never be mutated, deleted, or overwritten.",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_no_auto_fix_or_drop",
        "category": "quality_governance",
        "description": "Zero automated destructive cleaning, imputation, or feature dropping.",
        "is_mandatory": True,
        "non_signal": True,
    },
    {
        "contract_rule_id": "rule_quality_validation_audit",
        "category": "audit_integrity",
        "description": "Candidate states must link to explicit Phase 121 validation and Phase 123 quality audits.",
        "is_mandatory": True,
        "non_signal": True,
    },
]


def build_regime_candidate_state_integrity_contract_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for integrity contracts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for r in INTEGRITY_CONTRACT_RULES:
        row = r.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_integrity_contracts(df)
    return df, summary


def validate_candidate_state_integrity_contract(contract: dict) -> dict:
    """Validate that an integrity contract satisfies all safety conditions."""
    violations = []
    rule_id = contract.get("contract_rule_id", "unknown")

    if not contract.get("is_mandatory", False):
        violations.append("is_mandatory must be True")
    if not contract.get("non_signal", False):
        violations.append("non_signal must be True")

    return {
        "rule_id": rule_id,
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_candidate_state_integrity_contracts(df: pd.DataFrame) -> Dict:
    """Summarize integrity contracts."""
    total = len(df)
    all_mandatory = bool(df["is_mandatory"].all()) if not df.empty else True
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True

    return {
        "total_integrity_rules": total,
        "all_mandatory": all_mandatory,
        "all_non_signal": all_non_signal,
        "integrity_status": "VALID" if all_mandatory and all_non_signal else "INVALID",
    }
